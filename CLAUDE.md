# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

@AGENTS.md

## Claude Code only

`AGENTS.md` above is shared with Codex; this section covers behaviour only Claude Code has (ai-context-rules AC-2).

- **Hooks** (`.claude/settings.json`, PostToolUse on Edit|Write|MultiEdit|NotebookEdit) run after every file edit:
	- `hook_log_change.py` appends a metadata line to `changelog/ai-edits.jsonl` automatically — don't write that file yourself. Edits made through Bash are not captured; list them in the `changelog/CHANGELOG.md` entry.
	- `hook_log_change.py` also records `member` from `CAREKIND_MEMBER` (work-log-rules WL-1/WL-2).
	- SessionStart runs `work_items.py --me`: it prints the current member's open work and whether today's standup is submitted — relay it to the user at the start of the session.
	- `hook_file_size.py`: if it reports a file over 1000 lines (blocking message, exit 2), run `/refactor-large-file` on that file before continuing; an 800+ line warning means don't add new responsibilities to it.
- Nested `CLAUDE.md` files load automatically when you read files in a folder; each imports that folder's `AGENTS.md`.
- Skills appear as `/<name>` (e.g. `/run-workflow`, `/spec-writer`, `/compliance-check`); their source is `company-os/10-skills/` — edit there, then run the sync command.
