"""Shared limits and file classes for CareKind rule checks (code-rules.md). Defined once here (DRY)."""
import pathlib

MAX_FILE_LINES: int = 1000	# SIZE-1: above this a refactor is mandatory
WARN_FILE_LINES: int = 800	# SIZE-2: above this, plan a refactor

SOURCE_SUFFIXES: frozenset[str] = frozenset({
	'.py', '.ts', '.tsx', '.js', '.jsx', '.mjs', '.cjs',
	'.swift', '.kt', '.kts', '.java', '.go', '.rs', '.cs',
	'.sql', '.sh', '.ps1', '.vue', '.svelte', '.css', '.scss',
})
CONFIG_SUFFIXES: frozenset[str] = frozenset({'.json', '.yml', '.yaml', '.toml', '.ini', '.env'})
YAML_SUFFIXES: frozenset[str] = frozenset({'.yml', '.yaml'})
TYPED_LANGUAGE_SUFFIXES: frozenset[str] = frozenset({'.py', '.ts', '.tsx'})

# SIZE-4 and generally: generated, vendored and tool-managed files are not checked.
EXEMPT_DIRS: frozenset[str] = frozenset({
	'.git', 'node_modules', 'vendor', 'dist', 'build', 'coverage', '.venv', '__pycache__',
	'migrations', '__snapshots__', 'fixtures', 'generated', 'downloads',
	'.claude', '.agents',
})
EXEMPT_NAME_PARTS: tuple[str, ...] = ('.generated.', '.min.', '.pb.', '.lock')


def is_exempt(path: pathlib.Path) -> bool:
	if EXEMPT_DIRS.intersection(path.parts):
		return True
	return any(part in path.name for part in EXEMPT_NAME_PARTS)


def is_source_code(path: pathlib.Path) -> bool:
	return path.suffix in SOURCE_SUFFIXES and not is_exempt(path)


def is_config(path: pathlib.Path) -> bool:
	is_env_example = path.name.startswith('.env')
	return (path.suffix in CONFIG_SUFFIXES or is_env_example) and not is_exempt(path)


def count_lines(path: pathlib.Path) -> int:
	with open(path, encoding='utf-8', errors='replace') as handle:
		return sum(1 for _ in handle)
