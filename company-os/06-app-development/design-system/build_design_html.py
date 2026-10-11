"""Build design-system.html — a single, offline, human-readable page — from DESIGN.md and components/.

	python company-os/06-app-development/design-system/build_design_html.py

DESIGN.md stays the source of truth: tokens come from its YAML front matter, the guide from its
markdown body, and each component card from components/<Name>.md + components/<Name>.preview.html.
Re-run after any change to those files; never edit design-system.html by hand.
Needs PyYAML (`pip install pyyaml`).
"""
import html
import pathlib
import re
import sys

try:
	import yaml
except ImportError:
	sys.exit('build_design_html: PyYAML is required — run `pip install pyyaml`')

HERE = pathlib.Path(__file__).resolve().parent
DESIGN_MD = HERE / 'DESIGN.md'
COMPONENTS = HERE / 'components'
OUTPUT = HERE / 'design-system.html'

GROUP_ORDER = ('Actions', 'Inputs', 'Containers', 'Navigation', 'Feedback', 'Data display', 'Safety-critical', 'Web')
GROUP_TITLES = {
	'Actions': '操作', 'Inputs': '输入', 'Containers': '容器', 'Navigation': '导航', 'Feedback': '反馈',
	'Data display': '数据展示', 'Safety-critical': '安全关键（Clinical Lead 审阅前不得用于生产）', 'Web': '营销网站',
}
COLOR_GROUPS = (
	('强调色', ('primary',)),
	('表面', ('canvas', 'surface', 'scrim')),
	('文字', ('ink', 'on-', 'body')),
	('线条', ('divider', 'hairline', 'border')),
	('状态色（只表示系统状态，绝不表示临床严重程度）', ('status-',)),
)
MARKER = re.compile(r'^<!--\s*@dsCard(?P<attrs>[^>]*)-->\s*\n?')
MARKER_ATTR = re.compile(r'(\w+)=(?:"([^"]*)"|(\S+))')
HEX = re.compile(r'^#[0-9a-fA-F]{6}$')


# ---------- tokens ----------

def load_design() -> tuple[dict[str, object], str]:
	text = DESIGN_MD.read_text(encoding='utf-8')
	_, front, body = text.split('---\n', 2)
	return yaml.safe_load(front), body


def tokens_css(data: dict[str, object]) -> str:
	"""CSS custom properties with the same names the component previews use (--primary, --spacing-md…)."""
	lines = [f'--{name}: {value};' for name, value in data['colors'].items()]
	typography = data['typography']
	lines += [f'--font-display: {typography["font-display"]};', f'--font-text: {typography["font-text"]};']
	for family, prefix in (('spacing', 'spacing'), ('rounded', 'rounded'), ('size', 'size')):
		lines += [f'--{prefix}-{name}: {value};' for name, value in data[family].items()]
	lines += [f'--elevation-hairline: {data["elevation"]["hairline"]};', f'--elevation-media: {data["elevation"]["media"]};']
	return ':root {\n\t' + '\n\t'.join(lines) + '\n}'


def luminance(hex_colour: str) -> float:
	channels = [int(hex_colour[i:i + 2], 16) / 255 for i in (1, 3, 5)]
	linear = [c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4 for c in channels]
	return 0.2126 * linear[0] + 0.7152 * linear[1] + 0.0722 * linear[2]


def contrast(a: str, b: str) -> float:
	light, dark = sorted((luminance(a), luminance(b)), reverse=True)
	return (light + 0.05) / (dark + 0.05)


# ---------- markdown (the subset DESIGN.md and the component guides use) ----------

def inline(text: str) -> str:
	codes: list[str] = []

	def keep(match: re.Match[str]) -> str:
		codes.append(f'<code>{html.escape(match.group(1))}</code>')
		return f'\x00{len(codes) - 1}\x00'

	text = re.sub(r'`([^`]+)`', keep, text)
	text = html.escape(text, quote=False)
	text = re.sub(r'\[([^\]]+)\]\(([^)\s]+)\)', r'<a href="\2">\1</a>', text)
	text = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', text)
	text = re.sub(r'(?<![\w*])\*([^*\s][^*]*?)\*(?![\w*])', r'<em>\1</em>', text)
	text = re.sub(r'~~([^~]+)~~', r'<del>\1</del>', text)
	return re.sub(r'\x00(\d+)\x00', lambda m: codes[int(m.group(1))], text)


def table(rows: list[str]) -> str:
	cells = [[inline(c.strip()) for c in row.strip().strip('|').split('|')] for row in rows]
	head, body = cells[0], cells[2:]
	out = ['<div class="table"><table><thead><tr>', *[f'<th>{c}</th>' for c in head], '</tr></thead><tbody>']
	out += ['<tr>' + ''.join(f'<td>{c}</td>' for c in row) + '</tr>' for row in body]
	return ''.join(out) + '</tbody></table></div>'


def markdown(text: str, headings: list[tuple[str, str]] | None = None) -> str:
	"""Render headings, paragraphs, lists, tables, quotes and code fences; collect h2s for the side nav."""
	out: list[str] = []
	lines = text.splitlines()
	i = 0
	while i < len(lines):
		line = lines[i]
		stripped = line.strip()
		if not stripped:
			i += 1
		elif stripped.startswith('```'):
			end = next((j for j in range(i + 1, len(lines)) if lines[j].strip().startswith('```')), len(lines))
			out.append('<pre><code>' + html.escape('\n'.join(lines[i + 1:end])) + '</code></pre>')
			i = end + 1
		elif heading := re.match(r'^(#{1,4})\s+(.*)$', stripped):
			level, title = len(heading.group(1)), heading.group(2)
			if level == 1:
				i += 1
				continue
			anchor = f'g-{len(out)}'
			if level == 2 and headings is not None:
				headings.append((anchor, title))
			out.append(f'<h{level + 1} id="{anchor}">{inline(title)}</h{level + 1}>')
			i += 1
		elif stripped.startswith('|'):
			end = i
			while end < len(lines) and lines[end].strip().startswith('|'):
				end += 1
			out.append(table(lines[i:end]))
			i = end
		elif stripped.startswith('>'):
			end = i
			while end < len(lines) and lines[end].strip().startswith('>'):
				end += 1
			quote = ' '.join(l.strip().lstrip('>').strip() for l in lines[i:end])
			out.append(f'<blockquote>{inline(quote)}</blockquote>')
			i = end
		elif re.match(r'^(-|\d+\.)\s', stripped):
			tag = 'ol' if stripped[0].isdigit() else 'ul'
			items: list[str] = []
			while i < len(lines) and re.match(r'^\s*(-|\d+\.)\s', lines[i]):
				items.append(re.sub(r'^\s*(-|\d+\.)\s+', '', lines[i]))
				i += 1
			out.append(f'<{tag}>' + ''.join(f'<li>{inline(item)}</li>' for item in items) + f'</{tag}>')
		else:
			end = i
			while end < len(lines) and lines[end].strip() and not re.match(r'^(#|\||>|-\s|\d+\.\s|```)', lines[end].strip()):
				end += 1
			out.append('<p>' + inline(' '.join(l.strip() for l in lines[i:end])) + '</p>')
			i = max(end, i + 1)
	return '\n'.join(out)


# ---------- sections ----------

def colour_section(colours: dict[str, str]) -> str:
	canvas, tile = colours['canvas'], colours['surface-tile-1']
	placed: set[str] = set()
	parts = ['<section id="colors"><h2>颜色</h2><p class="lede">对比度在生成时按 WCAG 2 公式计算：正文需 ≥ 4.5:1，大字、控件边界与图标需 ≥ 3:1。</p>']
	for title, prefixes in COLOR_GROUPS:
		names = [n for n in colours if n not in placed and any(n.startswith(p) for p in prefixes)]
		placed.update(names)
		cards = []
		for name in names:
			value = str(colours[name])
			ratios = (f'canvas {contrast(value, canvas):.2f}:1 · tile-1 {contrast(value, tile):.2f}:1'
				if HEX.match(value) else '半透明，叠在背景上使用')
			cards.append(f'<div class="swatch"><div class="chip" style="background:var(--{name})"></div>'
				f'<code>{name}</code><span class="value">{html.escape(value)}</span><span class="ratio">{ratios}</span></div>')
		parts.append(f'<h3>{title}</h3><div class="swatches">{"".join(cards)}</div>')
	return ''.join(parts) + '</section>'


def type_section(typography: dict[str, object]) -> str:
	rows = []
	for name, spec in typography.items():
		if not isinstance(spec, dict):
			continue
		family = 'var(--font-display)' if name in ('hero-display', 'display-lg', 'display-md', 'tagline') else 'var(--font-text)'
		style = (f'font-family:{family};font-size:{spec["size"]};font-weight:{spec["weight"]};'
			f'line-height:{spec["line-height"]};letter-spacing:{spec["letter-spacing"]}')
		scope = '<span class="scope">仅营销网站</span>' if spec.get('scope') == 'web' else ''
		rows.append(f'<div class="type-row"><div class="type-meta"><code>{name}</code>{scope}'
			f'<span>{spec["size"]} / {spec["weight"]} / {spec["line-height"]}</span></div>'
			f'<div class="type-sample" style="{style}">Assisted with breakfast in the dining room.</div></div>')
	return (f'<section id="typography"><h2>字体</h2><p class="lede">字体栈：<code>{html.escape(str(typography["font-text"]))}</code></p>'
		+ ''.join(rows) + '</section>')


def scale_section(data: dict[str, object]) -> str:
	spacing = ''.join(f'<div class="bar-row"><code>spacing-{n}</code><span>{v}</span><div class="bar" style="width:{v}"></div></div>'
		for n, v in data['spacing'].items())
	radius = ''.join(f'<div class="radius"><div class="radius-box" style="border-radius:{v}"></div><code>rounded-{n}</code><span>{v}</span></div>'
		for n, v in data['rounded'].items())
	size = ''.join(f'<li><code>size-{n}</code> — {v}</li>' for n, v in data['size'].items())
	motion = ''.join(f'<li><code>{n}</code> — {html.escape(str(v))}</li>' for n, v in data['motion'].items())
	return ('<section id="scales"><h2>间距、圆角与尺寸</h2>'
		f'<h3>间距</h3>{spacing}<h3>圆角</h3><div class="radii">{radius}</div>'
		f'<h3>尺寸</h3><ul>{size}</ul><h3>层次</h3><div class="elev">'
		'<div class="elev-box" style="box-shadow:var(--elevation-hairline)"><code>elevation-hairline</code>卡片、顶栏分隔</div>'
		'<div class="elev-box" style="box-shadow:var(--elevation-media)"><code>elevation-media</code>只用于营销图片</div></div>'
		f'<h3>动效</h3><ul>{motion}</ul></section>')


def read_component(path: pathlib.Path, tokens: str) -> tuple[dict[str, str], str]:
	"""Return the card marker attributes and the preview document with the tokens injected."""
	source = path.read_text(encoding='utf-8')
	marker = MARKER.match(source)
	attrs = {k: (a or b) for k, a, b in MARKER_ATTR.findall(marker.group('attrs'))} if marker else {}
	document = source[marker.end():] if marker else source
	document = document.replace('<head>', f'<head><style>{tokens}</style>', 1)
	return attrs, document


def components_section(tokens: str) -> tuple[str, list[tuple[str, str]]]:
	cards: dict[str, list[str]] = {}
	for preview in sorted(COMPONENTS.glob('*.preview.html')):
		name = preview.name.removesuffix('.preview.html')
		if name == 'Cover':
			continue
		attrs, document = read_component(preview, tokens)
		guide_path = COMPONENTS / f'{name}.md'
		guide = markdown(guide_path.read_text(encoding='utf-8')) if guide_path.exists() else ''
		subtitle = f'<span class="subtitle">{html.escape(attrs["subtitle"])}</span>' if attrs.get('subtitle') else ''
		frame = (f'<iframe title="{name} preview" sandbox="allow-scripts" loading="lazy" '
			f'style="height:{attrs.get("height", "160")}px" srcdoc="{html.escape(document, quote=True)}"></iframe>')
		cards.setdefault(attrs.get('group', 'Other'), []).append(
			f'<article class="component" id="c-{name}"><h4>{name}{subtitle}</h4>{frame}<div class="guide">{guide}</div></article>')
	nav: list[tuple[str, str]] = []
	parts = ['<section id="components"><h2>组件</h2>']
	for group in [g for g in GROUP_ORDER if g in cards] + [g for g in cards if g not in GROUP_ORDER]:
		anchor = 'grp-' + re.sub(r'\W+', '-', group.lower())
		nav.append((anchor, f'{GROUP_TITLES.get(group, group)}（{len(cards[group])}）'))
		parts.append(f'<h3 id="{anchor}">{GROUP_TITLES.get(group, group)}</h3>' + ''.join(cards[group]))
	return ''.join(parts) + '</section>', nav


# ---------- page ----------

PAGE_CSS = """
*, *::before, *::after { box-sizing: border-box; }
body { margin: 0; background: var(--canvas); color: var(--ink); font: 400 17px/1.47 var(--font-text); letter-spacing: -0.374px; }
a { color: var(--primary); }
a:focus-visible, iframe:focus-visible { outline: 2px solid var(--primary-focus); outline-offset: 2px; }
code { font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; font-size: 0.85em; background: var(--canvas-parchment); padding: 1px 6px; border-radius: 6px; letter-spacing: 0; }
.layout { display: grid; grid-template-columns: 260px minmax(0, 1fr); min-height: 100vh; }
nav { position: sticky; top: 0; height: 100vh; overflow-y: auto; background: var(--canvas-parchment); padding: 24px 16px; font-size: 14px; letter-spacing: -0.224px; }
nav .brand { font: 600 21px/1.19 var(--font-display); margin: 0 8px 4px; letter-spacing: 0.231px; }
nav .version { color: var(--ink-muted); margin: 0 8px 16px; }
nav h5 { font: 600 14px/1.29 var(--font-text); color: var(--ink-muted); margin: 16px 8px 4px; }
nav a { display: block; padding: 6px 8px; border-radius: var(--rounded-sm); color: var(--ink); text-decoration: none; }
nav a:hover { background: var(--canvas); }
main { padding: 32px 48px 80px; max-width: 1120px; min-width: 0; }
.cover { position: relative; width: 100%; aspect-ratio: 960 / 288; overflow: hidden; border-radius: var(--rounded-lg); margin-bottom: 32px; }
.cover iframe { position: absolute; top: 0; left: 0; width: 960px; height: 288px; border: 0; transform-origin: 0 0; }
h2 { font: 600 34px/1.18 var(--font-display); margin: 56px 0 8px; text-wrap: balance; }
h3 { font: 600 21px/1.19 var(--font-display); margin: 32px 0 12px; letter-spacing: 0.231px; }
h4 { font: 600 17px/1.24 var(--font-text); margin: 0 0 12px; display: flex; gap: 12px; align-items: baseline; flex-wrap: wrap; }
.subtitle { font: 400 14px/1.43 var(--font-text); color: var(--ink-muted); }
.lede { color: var(--ink-muted); max-width: 70ch; }
p, li { max-width: 72ch; }
blockquote { margin: 16px 0; padding: 12px 16px; background: var(--canvas-parchment); border-radius: var(--rounded-sm); }
.table { overflow-x: auto; margin: 16px 0; }
table { border-collapse: collapse; font-size: 14px; letter-spacing: -0.224px; min-width: 480px; }
th { text-align: left; color: var(--ink-muted); font-weight: 600; }
th, td { padding: 8px 12px 8px 0; border-bottom: 1px solid var(--hairline); vertical-align: top; }
pre { background: var(--canvas-parchment); padding: 16px; border-radius: var(--rounded-sm); overflow-x: auto; font-size: 13px; }
pre code { background: none; padding: 0; }
.guide-body h3 { font-size: 24px; }
.swatches { display: grid; grid-template-columns: repeat(auto-fill, minmax(190px, 1fr)); gap: 12px; }
.swatch { display: grid; gap: 2px; font-size: 14px; letter-spacing: -0.224px; }
.swatch .chip { height: 64px; border-radius: var(--rounded-sm); border: 1px solid var(--hairline); margin-bottom: 6px; }
.swatch code { justify-self: start; }
.swatch .value, .swatch .ratio { color: var(--ink-muted); }
.type-row { display: grid; grid-template-columns: 200px minmax(0, 1fr); gap: 16px; padding: 12px 0; border-bottom: 1px solid var(--hairline); align-items: baseline; }
.type-meta { display: grid; gap: 2px; font-size: 14px; color: var(--ink-muted); letter-spacing: -0.224px; }
.type-meta code { justify-self: start; color: var(--ink); }
.scope { color: var(--status-attention); }
.type-sample { overflow-wrap: anywhere; }
.bar-row { display: grid; grid-template-columns: 150px 60px 1fr; align-items: center; gap: 12px; padding: 4px 0; font-size: 14px; }
.bar { height: 12px; background: var(--primary); border-radius: 2px; }
.radii, .elev { display: flex; flex-wrap: wrap; gap: 24px; }
.radius { display: grid; gap: 4px; justify-items: start; font-size: 14px; color: var(--ink-muted); }
.radius-box { width: 96px; height: 64px; background: var(--canvas-parchment); border: 1px solid var(--border-input); }
.elev-box { width: 220px; padding: 24px 16px; border-radius: var(--rounded-lg); background: var(--canvas); display: grid; gap: 8px; font-size: 14px; }
.component { border: 1px solid var(--hairline); border-radius: var(--rounded-lg); padding: 20px; margin: 0 0 20px; }
.component iframe { width: 100%; border: 1px solid var(--hairline); border-radius: var(--rounded-sm); background: var(--canvas); display: block; }
.guide { margin-top: 12px; font-size: 15px; line-height: 1.5; letter-spacing: -0.2px; }
.guide p, .guide ul { margin: 8px 0; }
.foot { margin-top: 64px; color: var(--ink-muted); font-size: 14px; }
@media (max-width: 900px) {
	.layout { grid-template-columns: 1fr; }
	nav { position: static; height: auto; }
	main { padding: 24px 16px 64px; }
	.type-row { grid-template-columns: 1fr; gap: 4px; }
	.bar-row { grid-template-columns: 120px 48px 1fr; }
}
"""

COVER_SCRIPT = """
(function () {
	var box = document.querySelector('.cover'), frame = box && box.querySelector('iframe');
	if (!frame) return;
	function fit() { frame.style.transform = 'scale(' + box.clientWidth / 960 + ')'; }
	fit();
	window.addEventListener('resize', fit);
})();
"""


def build() -> str:
	data, body = load_design()
	tokens = tokens_css(data)
	guide_headings: list[tuple[str, str]] = []
	guide = markdown(body, guide_headings)
	components, component_nav = components_section(tokens)
	cover_path = COMPONENTS / 'Cover.preview.html'
	cover = ''
	if cover_path.exists():
		_, document = read_component(cover_path, tokens)
		cover = f'<div class="cover"><iframe title="Cover" sandbox="" srcdoc="{html.escape(document, quote=True)}"></iframe></div>'
	nav_link = lambda anchor, title: f'<a href="#{anchor}">{inline(title)}</a>'
	nav = (f'<p class="brand">{html.escape(str(data["name"]))}</p><p class="version">v{data["version"]} · {data["updated"]}</p>'
		'<h5>规范（DESIGN.md）</h5>' + ''.join(nav_link(a, t) for a, t in guide_headings)
		+ '<h5>Tokens</h5>' + nav_link('colors', '颜色') + nav_link('typography', '字体') + nav_link('scales', '间距、圆角与尺寸')
		+ '<h5>组件</h5>' + ''.join(nav_link(a, t) for a, t in component_nav))
	return f"""<!doctype html>
<!-- GENERATED by build_design_html.py from DESIGN.md v{data['version']} and components/ — do not edit by hand. -->
<html lang="zh-Hans">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>CareKind Design System</title>
<style>
{tokens}
{PAGE_CSS}
</style>
</head>
<body>
<div class="layout">
<nav aria-label="Contents">{nav}</nav>
<main>
{cover}
<section id="guide" class="guide-body">{guide}</section>
{colour_section(data['colors'])}
{type_section(data['typography'])}
{scale_section(data)}
{components}
<p class="foot">由 <code>build_design_html.py</code> 从 DESIGN.md v{data['version']} 生成。规范以 DESIGN.md 为准；修改后重新运行脚本。</p>
</main>
</div>
<script>{COVER_SCRIPT}</script>
</body>
</html>
"""


def main() -> int:
	sys.stdout.reconfigure(encoding='utf-8')
	page = build()
	OUTPUT.write_text(page, encoding='utf-8', newline='\n')
	print(f'wrote {OUTPUT.relative_to(HERE.parents[2]).as_posix()} ({len(page) // 1024} KB)')
	return 0


if __name__ == '__main__':
	sys.exit(main())
