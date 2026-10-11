"""Claude Code PostToolUse hook: append one JSON line per AI file edit to changelog/ai-edits.jsonl.

Configured in .claude/settings.json for Edit|Write|MultiEdit|NotebookEdit (changelog-rules.md CL-1).
Only metadata is logged (time, session, tool, path, member) — never file content, which could contain
health information (code-rules P-1).
"""
import datetime
import json
import os
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
LOG_FILE = ROOT / 'changelog' / 'ai-edits.jsonl'


def relative_to_root(raw_path: str) -> str:
	path = pathlib.Path(raw_path).resolve()
	if ROOT in path.parents:
		return path.relative_to(ROOT).as_posix()
	return path.as_posix()


def build_entry(payload: dict[str, object]) -> dict[str, object] | None:
	tool_input = payload.get('tool_input') or {}
	raw_path = tool_input.get('file_path') or tool_input.get('notebook_path')
	if not raw_path:
		return None
	return {
		'timestamp': datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds'),
		'agent': 'claude-code',
		'session_id': payload.get('session_id'),
		'tool': payload.get('tool_name'),
		'file': relative_to_root(str(raw_path)),
		'user': os.environ.get('USERNAME') or os.environ.get('USER'),
		# Team-roster name set on each member's machine (work-log-rules.md WL-1); None when not set.
		'member': os.environ.get('CAREKIND_MEMBER') or None,
	}


def main() -> int:
	sys.stderr.reconfigure(encoding='utf-8')
	try:
		payload = json.load(sys.stdin)
	except json.JSONDecodeError as error:
		# Logging must never block an edit: report the problem and continue.
		print(f'hook_log_change: could not parse hook input ({error})', file=sys.stderr)
		return 0
	entry = build_entry(payload)
	if entry is None:
		return 0
	LOG_FILE.parent.mkdir(exist_ok=True)
	with open(LOG_FILE, 'a', encoding='utf-8') as log:
		log.write(json.dumps(entry, ensure_ascii=False) + '\n')
	return 0


if __name__ == '__main__':
	sys.exit(main())
