# Tasks 任务

> 格式：[ADLC spec](../../specs/2026-10-adlc-delivery-lifecycle.md) §6.1 ｜ 状态流转：§6.2 ｜ 分配规则：§6.3（AS-1 至 AS-6）

一任务一文件：`T-0001-<slug>.md`。头部 YAML 字段：`id`、`title`、`prd`、`requirements`、`type`、`status`、`priority`、`owner`（必须是人）、`executor`、`reviewer`（必须是人，≠ 执行者）、`safety_related`、`hazards`、`rdti`、`rnd_log`、`due`、`created`、`updated`。

状态：`backlog → ready → in-progress → in-review → done`（另有 `blocked`、`cancelled`）。`backlog → ready` 由 Terry 在周一例会确认。

## 当前任务

| 任务 | PRD | 执行 | 状态 |
|---|---|---|---|
| T-0001 至 T-0009 | [SPEC-003 Design System](../../specs/2026-10-design-system.md) | 见 spec §9 | ready（Terry 2026-10-11 确认） |

谁还有什么没做：`python company-os/11-rules/work_items.py`；站会会自动提醒（skill `standup`）。
