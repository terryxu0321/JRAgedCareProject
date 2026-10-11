"""Claude Code PostToolUse hook: trigger a refactor when an edited code file exceeds the size limit.

Configured in .claude/settings.json for Edit|Write|MultiEdit. Reads the hook JSON from stdin.
- Over MAX_FILE_LINES: message on stderr + exit 2, so Claude is told to run the refactor-large-file skill.
- Over WARN_FILE_LINES: a warning is added to Claude's context; the edit is not blocked.
"""
import json
import pathlib
import sys

from rule_config import MAX_FILE_LINES, WARN_FILE_LINES, count_lines, is_source_code


def edited_path(payload: dict[str, object]) -> pathlib.Path | None:
	tool_input = payload.get('tool_input') or {}
	tool_response = payload.get('tool_response') or {}
	raw = tool_input.get('file_path') or tool_response.get('filePath')
	return pathlib.Path(raw) if raw else None


def main() -> int:
	sys.stdout.reconfigure(encoding='utf-8')
	sys.stderr.reconfigure(encoding='utf-8')
	try:
		payload = json.load(sys.stdin)
	except json.JSONDecodeError as error:
		# A malformed payload is a harness problem, not a size violation: report it but never block the edit.
		print(f'hook_file_size: could not parse hook input ({error})', file=sys.stderr)
		return 0
	path = edited_path(payload)
	if path is None or not path.is_file() or not is_source_code(path):
		return 0

	lines = count_lines(path)
	if lines > MAX_FILE_LINES:
		print(
			f'{path} has {lines} lines, over the {MAX_FILE_LINES}-line limit '
			f'(company-os/11-rules/code-rules.md SIZE-1). Run the refactor-large-file skill on this file now: '
			'split it by responsibility, remove duplication and dead code, keep behaviour unchanged and tests passing. '
			'Do not compress code onto fewer lines.',
			file=sys.stderr,
		)
		return 2
	if lines > WARN_FILE_LINES:
		print(json.dumps({
			'hookSpecificOutput': {
				'hookEventName': 'PostToolUse',
				'additionalContext': (
					f'{path} has {lines} lines (warning threshold {WARN_FILE_LINES}, limit {MAX_FILE_LINES}). '
					'Avoid growing it further; plan a refactor (code-rules.md SIZE-2).'
				),
			},
		}))
	return 0


if __name__ == '__main__':
	sys.exit(main())
