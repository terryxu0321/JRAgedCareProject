"""Sync CareKind skills from company-os/10-skills/ to the folders Claude Code and Codex auto-discover.

	python company-os/10-skills/sync_skills.py

Source of truth: company-os/10-skills/<name>/SKILL.md
Targets:         .claude/skills/<name>/  (Claude Code)
                 .agents/skills/<name>/  (Codex)

Only folders carrying the MARKER file (or empty folders) are overwritten or
removed, so skills added to the target folders by hand are left alone.
Files are replaced in place rather than deleting whole folders, because
OneDrive on Windows often refuses to remove directories.
"""
import pathlib
import re
import shutil
import sys

MARKER = '.synced-from-company-os'
SRC = pathlib.Path(__file__).resolve().parent
ROOT = SRC.parent.parent
TARGETS = [ROOT / '.claude' / 'skills', ROOT / '.agents' / 'skills']
FRONTMATTER = re.compile(r'\A---\s*\n(.*?)\n---\s*\n', re.S)


def validate(skill_dir: pathlib.Path) -> str | None:
	text = (skill_dir / 'SKILL.md').read_text(encoding='utf-8')
	frontmatter = FRONTMATTER.match(text)
	if not frontmatter:
		return 'missing YAML frontmatter'
	fields = dict(
		line.split(':', 1) for line in frontmatter.group(1).splitlines() if ':' in line
	)
	name = fields.get('name', '').strip()
	if name != skill_dir.name:
		return f'frontmatter name "{name}" must equal folder name "{skill_dir.name}"'
	if not fields.get('description', '').strip():
		return 'missing description'
	return None


def is_managed(folder: pathlib.Path) -> bool:
	return (folder / MARKER).exists() or not any(folder.iterdir())


def clear_files(folder: pathlib.Path, keep: set[str] | None = None) -> None:
	"""Delete files under folder (except relative paths in keep); try to prune empty dirs."""
	keep = keep or set()
	for entry in sorted(folder.rglob('*'), reverse=True):
		relative_path = entry.relative_to(folder).as_posix()
		if entry.is_file() and relative_path not in keep:
			entry.unlink()
		elif entry.is_dir() and not any(entry.iterdir()):
			try:
				entry.rmdir()
			except OSError as error:
				# OneDrive on Windows often refuses directory removal; an empty folder is harmless, so warn and continue.
				print(f'WARN     could not remove empty folder {entry.relative_to(ROOT)}: {error}')


def main() -> None:
	skills = sorted(path for path in SRC.iterdir() if (path / 'SKILL.md').is_file())
	errors = {skill.name: error for skill in skills if (error := validate(skill))}
	if errors:
		for name, error in errors.items():
			print(f'ERROR {name}: {error}')
		sys.exit(1)

	names = {s.name for s in skills}
	for target in TARGETS:
		target.mkdir(parents=True, exist_ok=True)
		for existing in target.iterdir():
			if existing.is_dir() and existing.name not in names and (existing / MARKER).exists():
				clear_files(existing)
				try:
					existing.rmdir()
				except OSError:
					print(f'WARN     {existing.relative_to(ROOT)} emptied but folder could not be removed (delete it manually)')
				else:
					print(f'removed  {existing.relative_to(ROOT)}')
		for skill in skills:
			dest = target / skill.name
			if dest.exists():
				if not is_managed(dest):
					print(f'SKIP     {dest.relative_to(ROOT)} (not managed by this script)')
					continue
				source_files = {f.relative_to(skill).as_posix() for f in skill.rglob('*') if f.is_file()}
				clear_files(dest, keep=source_files)
			shutil.copytree(skill, dest, dirs_exist_ok=True)
			(dest / MARKER).write_text(
				f'Generated from company-os/10-skills/{skill.name}/ - edit the source, then re-run sync_skills.py\n',
				encoding='utf-8',
			)
		print(f'synced   {len(skills)} skills -> {target.relative_to(ROOT)}')


if __name__ == '__main__':
	main()
