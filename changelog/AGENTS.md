# AGENTS.md — changelog — AI 变更记录

> AI 助手在本目录工作前必读。全局规则：根目录 `AGENTS.md` 与 `company-os/11-rules/`。人类说明：同目录 `README.md`。完成任务后按 `changelog-rules.md` 写 `changelog/CHANGELOG.md`。

## 这个目录是什么
记录 AI 对本仓库的每次修改，便于追溯、审计与分析。

## 关键文件
- `CHANGELOG.md` —— 任务级记录（AI 撰写，最新在上）
- `ai-edits.jsonl` —— 逐次编辑记录（Claude Code hook 自动生成）

## 在这里工作的规则
- 每完成一个任务，在 `CHANGELOG.md` 顶部追加一条（格式见 `company-os/11-rules/changelog-rules.md`）
- **不要手工修改 `ai-edits.jsonl`**；只追加，不改历史
- 禁止写入居民可识别信息、健康信息或密钥
