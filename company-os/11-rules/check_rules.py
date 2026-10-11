"""Check the CareKind rules that can be verified automatically.

	python company-os/11-rules/check_rules.py

LEGAL    PRD and specs contain a "法律依据" section linking company-os/03-legal-compliance/ (product-legal-rules L-2, L-3)
FORMAT   code is indented with tabs; YAML has no tabs (code-rules FMT-1, FMT-2)
SIZE     code files stay within MAX_FILE_LINES; WARN above WARN_FILE_LINES (code-rules SIZE-1, SIZE-2)
SECRET   no hard-coded secrets (CORE-03)
CATCH    no empty catch / except-pass (CORE-06)
PLACE    no TODO / FIXME / XXX / Lorem ipsum (CORE-09)
ANY      no `any` / `Any` unless whitelisted in any-whitelist.md (CORE-15)
CONTEXT  required folders have README.md + AGENTS.md + CLAUDE.md importing @AGENTS.md (ai-context-rules AC-1, AC-2)
ASSIGN   each PRD / spec has at most one Assignee line naming one team-roster member; WARN when unassigned (skill assign-prd)

Exits with code 1 when any check fails.
"""
import pathlib
import re
import sys
from collections.abc import Iterator

from rule_config import (
	MAX_FILE_LINES, TYPED_LANGUAGE_SUFFIXES, WARN_FILE_LINES, YAML_SUFFIXES,
	count_lines, is_config, is_exempt, is_source_code,
)

ROOT = pathlib.Path(__file__).resolve().parents[2]
SELF = pathlib.Path(__file__).resolve()
RULES_DIR = SELF.parent
LEGAL_DIR = (ROOT / 'company-os' / '03-legal-compliance').resolve()

LEGAL_HEADING = re.compile(r'^#{2,6} .*法律依据', re.M)
NEXT_HEADING = re.compile(r'^#{1,6} ', re.M)
LINK = re.compile(r'\]\(([^)#\s]+)(?:#[^)]*)?\)')

SECRET_PATTERNS = (
	re.compile(r'AKIA[0-9A-Z]{16}'),
	re.compile(r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----'),
	re.compile(r'\bsk-[A-Za-z0-9_-]{20,}'),
	re.compile(r'(?i)\b(?:api[_-]?key|secret|password|passwd|token)\b\s*[:=]\s*[\'"][^\'"\s]{8,}[\'"]'),
)
EMPTY_CATCH_PATTERNS = (
	re.compile(r'except[^\n:]*:[ \t]*(?:pass|\.\.\.)[ \t]*(?:#.*)?$', re.M),
	re.compile(r'except[^\n:]*:[ \t]*\n[ \t]*(?:pass|\.\.\.)[ \t]*(?:#.*)?$', re.M),
	re.compile(r'catch\s*(?:\([^)]*\))?\s*\{\s*\}'),
)
PLACEHOLDER = re.compile(r'\b(?:TODO|FIXME|XXX)\b|(?i:lorem ipsum)')
ANY_TYPESCRIPT = re.compile(r':\s*any\b|\bas\s+any\b|<any>|\bany\[\]')
ANY_PYTHON = re.compile(r'\bAny\b')
ANY_ALLOWED = re.compile(r'any-allowed:\s*(\S+)')
# Header field in either form: "| Assignee | Ahmad |" (table) or "- Assignee: Ahmad" (list).
ASSIGNEE_LINE = re.compile(r'^(?:\|\s*Assignee\s*\|(?P<cell>[^|\n]*)\||-\s*Assignee\s*[:：](?P<item>[^\n]*))', re.M)
ROSTER_NAME = re.compile(r'^\|\s*\*\*\[([^\]]+)\]\(team-members/', re.M)


def legal_section(text: str) -> str | None:
	match = LEGAL_HEADING.search(text)
	if not match:
		return None
	rest = text[match.end():]
	end = NEXT_HEADING.search(rest)
	return rest[:end.start()] if end else rest


def check_legal_references(doc: pathlib.Path) -> list[str]:
	section = legal_section(doc.read_text(encoding='utf-8'))
	if section is None:
		return ['missing "法律依据" section']
	errors = []
	legal_links = 0
	for target in LINK.findall(section):
		if target.startswith(('http://', 'https://', 'mailto:')):
			continue
		path = (doc.parent / target).resolve()
		if not path.exists():
			errors.append(f'broken link: {target}')
		elif path == LEGAL_DIR or LEGAL_DIR in path.parents:
			legal_links += 1
	if legal_links == 0:
		errors.append('no link into company-os/03-legal-compliance/')
	return errors


def documents_requiring_legal_references() -> list[pathlib.Path]:
	specs = ROOT / 'company-os' / '06-app-development' / 'specs'
	docs = [ROOT / 'docs' / 'PRD.md']
	docs += sorted(p for p in specs.glob('*.md') if p.name != 'README.md')
	return [d for d in docs if d.exists()]


def roster_names() -> set[str]:
	roster = ROOT / 'company-os' / '05-hr-teams' / 'team-roster.md'
	return set(ROSTER_NAME.findall(roster.read_text(encoding='utf-8')))


def check_assignee(doc: pathlib.Path, members: set[str]) -> tuple[list[str], list[str]]:
	"""Return (failures, warnings): a PRD has exactly one Assignee, who must be on the team roster."""
	matches = list(ASSIGNEE_LINE.finditer(doc.read_text(encoding='utf-8')))
	if not matches:
		return [], ['no Assignee — run skill assign-prd']
	if len(matches) > 1:
		return [f'{len(matches)} Assignee lines — keep exactly one'], []
	name = (matches[0].group('cell') or matches[0].group('item') or '').strip().strip('*').strip()
	if name not in members:
		return [f'Assignee "{name}" is not exactly one member of team-roster.md'], []
	return [], []


def check_formatting(path: pathlib.Path, lines: list[str]) -> list[str]:
	if path.suffix in YAML_SUFFIXES:
		return [f'line {n}: tab in YAML' for n, line in enumerate(lines, 1) if '\t' in line][:5]
	errors = []
	in_docstring = False
	for n, line in enumerate(lines, 1):
		if line.count('"""') % 2 == 1:
			in_docstring = not in_docstring
		if not in_docstring and re.match(r'^ +\S', line):
			errors.append(f'line {n}: indented with spaces')
	return errors[:5]


def check_size(lines: list[str]) -> tuple[list[str], list[str]]:
	if len(lines) > MAX_FILE_LINES:
		return [f'{len(lines)} lines > {MAX_FILE_LINES} — run skill refactor-large-file'], []
	if len(lines) > WARN_FILE_LINES:
		return [], [f'{len(lines)} lines > {WARN_FILE_LINES} — plan a refactor']
	return [], []


def line_number(text: str, offset: int) -> int:
	return text.count('\n', 0, offset) + 1


def check_secrets(text: str) -> list[str]:
	return [
		f'line {line_number(text, match.start())}: possible hard-coded secret — move it to .env / secrets manager'
		for pattern in SECRET_PATTERNS for match in pattern.finditer(text)
	]


def check_empty_catch(text: str) -> list[str]:
	return [
		f'line {line_number(text, match.start())}: empty catch — handle the error or re-raise with context'
		for pattern in EMPTY_CATCH_PATTERNS for match in pattern.finditer(text)
	]


def check_placeholders(lines: list[str]) -> list[str]:
	return [f'line {n}: placeholder ({PLACEHOLDER.search(line).group(0)})' for n, line in enumerate(lines, 1) if PLACEHOLDER.search(line)]


def whitelisted_any_ids() -> set[str]:
	whitelist = RULES_DIR / 'any-whitelist.md'
	rows = re.findall(r'^\|\s*([A-Za-z0-9_-]+)\s*\|', whitelist.read_text(encoding='utf-8'), re.M)
	return {row for row in rows if row != '编号'}


def check_any(path: pathlib.Path, lines: list[str], allowed_ids: set[str]) -> list[str]:
	pattern = ANY_PYTHON if path.suffix == '.py' else ANY_TYPESCRIPT
	errors = []
	for n, line in enumerate(lines, 1):
		if not pattern.search(line):
			continue
		allowed = ANY_ALLOWED.search(line)
		if not allowed:
			errors.append(f'line {n}: `any` without whitelist approval')
		elif allowed.group(1) not in allowed_ids:
			errors.append(f'line {n}: any-allowed id "{allowed.group(1)}" not in any-whitelist.md')
	return errors


def required_context_dirs() -> list[pathlib.Path]:
	company_os = ROOT / 'company-os'
	src = company_os / '06-app-development' / 'src'
	dirs = [ROOT, ROOT / 'docs', ROOT / 'changelog', company_os, src]
	dirs += [d for d in company_os.iterdir() if d.is_dir() and not d.name.startswith('.')]
	dirs += [d for d in (company_os / '05-hr-teams' / 'teams').iterdir() if d.is_dir()]
	dirs += [d for d in src.rglob('*') if d.is_dir() and not is_exempt(d.relative_to(ROOT)) and len(d.relative_to(src).parts) <= 2]
	return sorted(set(dirs))


def check_context_files(directory: pathlib.Path) -> list[str]:
	missing = [name for name in ('README.md', 'AGENTS.md', 'CLAUDE.md') if not (directory / name).is_file()]
	errors = [f'missing {name}' for name in missing]
	claude = directory / 'CLAUDE.md'
	if claude.is_file() and '@AGENTS.md' not in claude.read_text(encoding='utf-8'):
		errors.append('CLAUDE.md must import @AGENTS.md')
	return errors


def files_to_check() -> Iterator[pathlib.Path]:
	for path in ROOT.rglob('*'):
		if path.is_file() and (is_source_code(path.relative_to(ROOT)) or is_config(path.relative_to(ROOT))):
			yield path


def check_file(path: pathlib.Path, allowed_ids: set[str]) -> tuple[list[tuple[str, str]], list[str]]:
	"""Return (failures as (category, message), warnings) for one file."""
	text = path.read_text(encoding='utf-8', errors='replace')
	lines = text.splitlines()
	relative = path.relative_to(ROOT)
	failures = [('FORMAT', e) for e in check_formatting(path, lines)]
	failures += [('SECRET', e) for e in check_secrets(text)]
	if not is_source_code(relative):
		return failures, []
	size_errors, warnings = check_size(lines)
	failures += [('SIZE', e) for e in size_errors]
	# This file defines the patterns below, so it would match itself.
	if path.resolve() != SELF:
		failures += [('CATCH', e) for e in check_empty_catch(text)]
		failures += [('PLACE', e) for e in check_placeholders(lines)]
		if path.suffix in TYPED_LANGUAGE_SUFFIXES:
			failures += [('ANY', e) for e in check_any(path, lines, allowed_ids)]
	return failures, warnings


def main() -> int:
	sys.stdout.reconfigure(encoding='utf-8')	# Windows consoles default to cp1252
	failures = 0
	members = roster_names()
	for doc in documents_requiring_legal_references():
		for error in check_legal_references(doc):
			print(f'LEGAL   {doc.relative_to(ROOT)}: {error}')
			failures += 1
		assign_errors, assign_warnings = check_assignee(doc, members)
		for error in assign_errors:
			print(f'ASSIGN  {doc.relative_to(ROOT)}: {error}')
		for warning in assign_warnings:
			print(f'WARN    {doc.relative_to(ROOT)}: {warning}')
		failures += len(assign_errors)
	for directory in required_context_dirs():
		for error in check_context_files(directory):
			print(f'CONTEXT {directory.relative_to(ROOT).as_posix() or "."}: {error}')
			failures += 1
	allowed_ids = whitelisted_any_ids()
	for path in files_to_check():
		file_failures, warnings = check_file(path, allowed_ids)
		for category, message in file_failures:
			print(f'{category:<7} {path.relative_to(ROOT)}: {message}')
		for message in warnings:
			print(f'WARN    {path.relative_to(ROOT)}: {message}')
		failures += len(file_failures)
	print('OK: all rule checks passed' if failures == 0 else f'FAILED: {failures} problem(s)')
	return 1 if failures else 0


if __name__ == '__main__':
	sys.exit(main())
