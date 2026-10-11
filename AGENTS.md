# AGENTS.md — CareKind AI

Instructions for AI coding agents (Codex, Claude Code, others) working in this folder. `CLAUDE.md` points here — keep this file as the single copy.

## What this repo is

The Company OS of **CareKind AI** — an Australian (Sydney, NSW) pre-seed startup building an AI documentation assistant for aged care nurses. Team: Terry (Product Owner + Tech Lead), Ahmad, Matt, Dave (Developers). This is a **learning project**: Ahmad, Matt and Dave are hypothetical members — Terry may act as any of them (set `CAREKIND_MEMBER`); design rules as for a real team. Documents are written in Simplified Chinese with English legal/industry terms; reply to the user in Chinese unless asked otherwise.

The product requirements document is **`docs/PRD.md`** — the single source for product scope, logic and workflows. Read it before any product or engineering task; changes to product boundaries (TGA, recording mode, HITL, data residency) need a decision record first.

Company material lives under `company-os/`:

| Folder | Content |
|---|---|
| `00-company` … `05-hr-teams` | Company basics, strategy/OKRs, operating rhythm, legal & compliance, finance, HR & team |
| `06-app-development` | Product principles, clinical safety, AI governance, security, specs |
| `07-marketing-operations` | Brand, sales, pilots, competitor research |
| `08-feedback` | **Raw** user feedback — human-entered only |
| `09-workflows` | Multi-step workflows (run with the `run-workflow` skill) |
| `10-skills` | Skill source of truth (synced to `.claude/skills/` and `.agents/skills/`) |
| `11-rules` | **Mandatory rules** — company, operations, code, product/PRD legal references, AI context files, changelog |
| `templates` | DR, weekly update, meeting notes, postmortem |

Root-level folders besides `company-os/`: `docs/` (PRD) and `changelog/` (AI change records).

## Commands

| Command (run from repo root) | Purpose |
|---|---|
| `python company-os/11-rules/check_rules.py` | All automated rule checks — LEGAL, FORMAT, SIZE, SECRET, CATCH, PLACE, ANY, CONTEXT, ASSIGN (each PRD/spec has exactly one roster Assignee — skill `assign-prd`). Must pass after changing the PRD, a spec, code or folder structure; exit 1 on failure |
| `python company-os/10-skills/sync_skills.py` | Copy skills from `company-os/10-skills/` to `.claude/skills/` and `.agents/skills/` after adding or editing a skill |
| `python company-os/11-rules/work_items.py [--member Matt] [--log]` | Open work per member (PRD Assignee + ADLC tasks), or one member's work record (work-log-rules) |
| `python company-os/11-rules/standup.py --context \| --summary [--date YYYY-MM-DD]` | Standup reminders for the current member, or the team's standups and blockers for a day |
| `echo '{"tool_input":{"file_path":"<abs path>"}}' \| python company-os/11-rules/hook_file_size.py` | Manually exercise a hook script (exit 2 = over the size limit) |

There is **no build, lint or test command yet**: product code has not started — `company-os/06-app-development/src/` holds only module docs. The stack is proposed (not decided) in `company-os/06-app-development/engineering-standards.md`. When code starts, formatter/linter config must match `.editorconfig` (tabs, width 4) and add its commands here.

Environment notes: Windows + OneDrive; a git repository (branch `main`) with a **public** GitHub remote `origin` (https://github.com/terryxu0321/JRAgedCareProject, public since 2026-10-11) — everything committed is world-readable: never commit secrets, real resident or personal data, local absolute paths, or licensed PDFs from `research/downloads/`. `.gitignore` excludes secrets, caches, local Claude settings, `.claude/worktrees/` and `research/downloads/` PDFs; `.gitattributes` keeps LF line endings per `.editorconfig`. Commit or push only when the user asks. Python printing Chinese needs `PYTHONIOENCODING=utf-8` (scripts here call `sys.stdout.reconfigure`). OneDrive may refuse directory removal, and in-place shell edits (`perl -pi`, Python rewrites from Bash) have silently failed here before — prefer the file edit tools and re-read to confirm.

## How the pieces fit

- **Product → code**: `docs/PRD.md` Part C defines the architecture (mobile-app → api → ai-pipeline's 7 steps: transcription → segmentation → attribution → classification → extraction → drafting → guardrails → review-service → record-store → integrations; plus admin-web). `company-os/06-app-development/src/` mirrors it one folder per module; each module's `AGENTS.md` lists its PRD requirement IDs, hard rules, clinical hazards and required tests. Attribution (which resident an utterance is about) is the highest-risk module — its hard rules are in PRD C3.
- **Law → product**: local legal files in `company-os/03-legal-compliance/` → topic lookup in `11-rules/legal-reference-index.md` → the "法律依据" section required in the PRD and every spec → verified by `check_rules.py` (LEGAL). Product boundary changes go through a DR in `02-operating-rhythm/decision-log.md`.
- **Automation**: rules (`11-rules/*.md`) are enforced by `check_rules.py`; thresholds and file classes live only in `11-rules/rule_config.py`. Skills (`10-skills/`) are reusable steps; workflows (`09-workflows/`) chain skills with 🛑 human checkpoints and are run by the `run-workflow` skill. Claude Code hooks (`.claude/settings.json`) call `11-rules/hook_log_change.py` (→ `changelog/ai-edits.jsonl`) and `11-rules/hook_file_size.py` (→ refactor trigger) after every edit.

## Folder context — read before working in a folder

Every level (root, `docs/`, `changelog/`, each `company-os/` module, each team, the code repo `company-os/06-app-development/src/` and each code module/sub-module) has `README.md` (humans), `AGENTS.md` (AI guidance) and `CLAUDE.md` (imports `@AGENTS.md`). **Before reading or changing files in a folder, read that folder's `AGENTS.md` and its parents'.** Claude Code loads nested `CLAUDE.md` automatically; Codex must open the nested `AGENTS.md` itself. When you create or split a folder, add the three files in the same change (`company-os/11-rules/ai-context-rules.md`).

## Rules — read the matching file before the task

| Task | Must read and follow |
|---|---|
| Any task | `company-os/11-rules/company-rules.md` |
| Customers, pilots, support, marketing, vendors, spending | `company-os/11-rules/operations-rules.md` |
| Writing or reviewing code | `company-os/11-rules/code-rules.md` — KISS > DRY > premature abstraction; SOLID for boundaries; fail safe; **indent with tabs, width 4 (YAML: 2 spaces)** per root `.editorconfig` |
| Product design, PRD (`docs/PRD.md`), specs | `company-os/11-rules/product-legal-rules.md` + `legal-reference-index.md` — **consult the local legal files in `company-os/03-legal-compliance/` first, and include a "法律依据 Legal References" section linking them** |
| Any UI work (mobile-app, admin-web, web pages, prototypes, design docs) | `company-os/06-app-development/design-system/DESIGN.md` — the design source of truth: use only its `{token}`s and components; no inline colours or font sizes; no colours or badges for clinical risk/severity (TGA) |
| Every session (who is working, open work, daily standup) | `company-os/11-rules/work-log-rules.md` — the member is `CAREKIND_MEMBER` (ask if unset) and is the CHANGELOG 请求人; open work comes only from PRD Assignee + ADLC tasks; standups via skill `standup`; reminders to others are drafts only; no per-person stats or rankings |
| Assigning or reassigning a PRD / spec | `company-os/11-rules/prd-assignment-rules.md` — difficulty L1–L3 × member level/direction (from `team-roster.md`) × load; Terry confirms (skill `assign-prd`) |
| Creating or restructuring folders | `company-os/11-rules/ai-context-rules.md` |
| **Finishing any task that changed files** | `company-os/11-rules/changelog-rules.md` — **append an entry to the top of `changelog/CHANGELOG.md`** (request, files changed, reasons, checks run, open questions). Claude Code edits are also logged automatically to `changelog/ai-edits.jsonl`; Codex has no hook, so the CHANGELOG entry is its only record. Never edit `ai-edits.jsonl` by hand |
| Code: core 15 rules | Single responsibility · clear naming · no hard-coded secrets (`.env`, never committed) · "why" comment before complex logic · tests first for key logic · no empty catch · validate only at boundaries · secure by default · no TODO/placeholder/fake data · performance floors (interactive API > 2 s = fail) · minimal dependencies · YAGNI · code for the reader · explicit types on exports · no `any` unless whitelisted (`code-rules.md` §0) |

After changing the PRD, a spec or any code, run `python company-os/11-rules/check_rules.py`; it must pass.

**File size limit:** a code file over **1000 lines** must be refactored immediately — when `check_rules.py` prints `SIZE` (or the Claude Code hook reports it), run the `refactor-large-file` skill (Claude: `/refactor-large-file`; Codex: `$refactor-large-file`) before doing anything else. Reduce lines by splitting responsibilities, removing duplication and dead code — never by compressing formatting. Over 800 lines is a warning: don't add new responsibilities to that file.

## Workflows and skills

- To run a workflow: when the user says "运行 workflow X" / "run workflow X", use the `run-workflow` skill (Claude: `/run-workflow X`; Codex: `$run-workflow X`). It reads `company-os/09-workflows/X.md` and executes the steps.
- Skills are edited **only** in `company-os/10-skills/<name>/SKILL.md`. After adding or changing a skill, run:
  `python company-os/10-skills/sync_skills.py`
  Never edit `.claude/skills/` or `.agents/skills/` copies directly.
- 🛑 Human checkpoints in workflows are mandatory. In non-interactive runs (`claude -p`, `codex exec`), stop at the first checkpoint and write the pending items at the top of the output file.

## Hard rules (all agents, all tasks)

1. **Never create, edit, rename, delete, summarise into, translate or "clean up" files in `company-os/08-feedback/raw/`.** Read-only. Analysis goes to `company-os/07-marketing-operations/feedback-insights/`.
2. **No resident-identifiable information** (names, room numbers, DOB, record numbers) in any file.
3. **Do not send anything externally** (email, forms, publishing, regulator notifications). Draft only; a human sends.
4. **Product boundary:** documentation-only. Never design features that generate diagnoses, treatment/medication advice or risk scores (TGA medical-device boundary). AI output always requires nurse review (HITL). Data and AI processing stay in Australia.
5. Legal/compliance output is an internal working draft, **not legal advice** — say so, cite sources, mark unverified claims.
6. Do not edit policies or the compliance register on your own initiative; propose changes and wait for approval.
7. Do not invent metrics, customers, people's details, or anyone's pronouns.
8. Keep relative Markdown links working when moving files.
9. Product decisions must be grounded in the local legal files (`company-os/03-legal-compliance/`), not memory or ad-hoc web search; if the local files don't cover a question, add the finding there first (skill `regulatory-watch`), then cite it.
