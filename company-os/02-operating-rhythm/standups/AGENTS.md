# AGENTS.md — 02-operating-rhythm/standups — 每日站会记录

> AI 助手在本目录工作前必读。全局规则：根目录 `AGENTS.md` 与 `company-os/11-rules/`。人类说明：同目录 `README.md`。完成任务后按 `changelog-rules.md` 写 `changelog/CHANGELOG.md`。

## 这个目录是什么
每位成员每天一份站会报告 `YYYY-MM-DD_<成员>.md`，由 skill `standup` 写入。

## 关键文件
- `README.md` —— 报告格式
- `company-os/11-rules/work-log-rules.md` WL-6 —— 规则
- `company-os/11-rules/standup.py` —— 提交前提醒、每日汇总（只读）

## 在这里工作的规则
- 只用 skill `standup` 写入；只写**当前成员**（`CAREKIND_MEMBER`）自己的报告，不代他人提交或修改他人报告
- 内容来自成员本人的口述；AI 只整理措辞，不编造进展、不替人判断 Blocker 是否解决
- 禁止写入居民可识别信息、健康信息、密钥；不做提交率、连续天数、排名等统计（WL-5）
- 站会文件很小，写入不单独记 CHANGELOG（WL-6）；hook 仍会写 `ai-edits.jsonl`
