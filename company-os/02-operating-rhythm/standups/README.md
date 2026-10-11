# Standups 每日站会记录

> Owner: Terry ｜ 规范：[work-log-rules.md](../../11-rules/work-log-rules.md) WL-6 ｜ 提交方式：在 Claude Code / Codex 中说"提交站会"（skill `standup`）

每位成员每个工作日一份：`YYYY-MM-DD_<成员>.md`（成员名与[团队名册](../../05-hr-teams/team-roster.md)一致）。当天再次提交即更新同一份。

## 报告格式

```markdown
# Standup · 2026-10-12 · Matt

- 成员：Matt
- 提交：2026-10-12 09:05（经 Claude Code）

## 昨天完成
- …
## 今天计划
- …
## Blockers
- 无
## 负责的 PRD（自动）
- docs/PRD.md
## 未完成任务（自动）
- 无
```

"（自动）"两节由 skill 根据 PRD Assignee 与 ADLC 任务填写；下一次站会用它们判断"新分配的 PRD"。

## 查看

- 某天全队：`python company-os/11-rules/standup.py --summary --date 2026-10-12`
- 我的提醒：`python company-os/11-rules/standup.py --context`

## 不要

- 写入居民可识别信息、健康信息、密钥
- 修改别人的站会报告；统计提交率、连续天数或排名（WL-5）
