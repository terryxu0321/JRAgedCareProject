# AGENTS.md — 10-skills — 技能库

> AI 助手在本目录工作前必读。全局规则：根目录 `AGENTS.md` 与 `company-os/11-rules/`。人类说明：同目录 `README.md`。完成任务后按 `changelog-rules.md` 写 `changelog/CHANGELOG.md`。

## 这个目录是什么
Skill 的唯一来源；同步到 `.claude/skills/`（Claude）与 `.agents/skills/`（Codex）。

## 关键文件
- `<name>/SKILL.md`
- `sync_skills.py`

## 在这里工作的规则
- 只在这里编辑 skill；**不要**直接改 `.claude/skills/` 或 `.agents/skills/` 中的副本
- 新增或修改后运行 `python company-os/10-skills/sync_skills.py`
- frontmatter 的 `name` 必须等于文件夹名，`description` 写清"做什么 + 何时用"（中英文关键词）
