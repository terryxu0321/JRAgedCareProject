# 工作记录、待办提醒与每日站会规范 Work Log & Standup Rules

> Owner: Terry ｜ 适用：所有成员通过 AI（Claude Code、Codex）操作本仓库时 ｜ 决策：[DR-008](../02-operating-rhythm/decisions/DR-008-member-work-log-and-standup.md)（提议中）｜ 复审：每季度
>
> 学习项目说明：Ahmad、Matt、Dave 目前是**假设成员**。Terry 可以用 WL-1 的环境变量**扮演任一成员**来练习（如 `CAREKIND_MEMBER=Matt`）。WL-5 中的员工通知义务在有真实员工后才适用。

目的：每个人用 AI 做了什么**自动留下记录**；每个人被分配的工作**随时可查、自动提醒**；每天的站会在 AI 中提交并存档。

| # | 规则 | 机制 |
|---|---|---|
| WL-1 | **标明身份**：每位成员在自己电脑上设置环境变量 `CAREKIND_MEMBER=<名册中的名字>` | Claude Code：用户级 `~/.claude/settings.json` 加 `"env": {"CAREKIND_MEMBER": "Matt"}`；Codex / 终端：PowerShell `setx CAREKIND_MEMBER Matt`（新终端生效）|
| WL-2 | **自动记录**：每次 AI 编辑都记录成员名；每个任务的 CHANGELOG 条目"请求人"写当前成员 | Claude Code hook `hook_log_change.py` → `changelog/ai-edits.jsonl` 的 `member` 字段；Codex 没有 hook，CHANGELOG 是唯一记录（`changelog-rules.md`）。`CAREKIND_MEMBER` 未设置时，AI 先问"你是谁"再写 CHANGELOG |
| WL-3 | **分配的工作只有两个来源**，不另建待办清单（DRY） | ① PRD 头部 `Assignee`（[DR-006](../02-operating-rhythm/decisions/DR-006-prd-single-assignee.md)、[prd-assignment-rules.md](prd-assignment-rules.md)）② ADLC 任务文件 `06-app-development/adlc/tasks/T-*.md` 的 owner / executor / reviewer（[ADLC spec](../06-app-development/specs/2026-10-adlc-delivery-lifecycle.md) §6，目录建立后生效）|
| WL-4 | **自动提醒**：每次打开 Claude Code 会话，显示当前成员的未完成工作，以及今天是否已交站会；任何人可随时查看任何成员的未完成工作 | SessionStart hook：`work_items.py --me`；随时查：skill `work-status` 或 `python company-os/11-rules/work_items.py [--member Matt]` |
| WL-5 | **只为协作与审计，不做绩效监控** | 只列工作项和改动的文件，不统计数量、耗时、提交率、连续天数，不排名；不记录文件内容、按键、屏幕。工作记录（`--log`）只能按单人查看。⚖️ 有真实员工后：启用前须**提前 14 天书面通知**员工，并有书面政策（NSW Workplace Surveillance Act 2005，见下方法律依据，待律师确认）|
| WL-6 | **每日站会**：每位成员每个工作日在 AI 中提交一次（昨天完成 / 今天计划 / Blockers）| skill `standup`：先运行 `standup.py --context` 提醒"未完成的 PRD 与任务、上次站会后新分配的 PRD、上次计划是否完成、上次 Blocker 是否解决"，再写 `02-operating-rhythm/standups/YYYY-MM-DD_<成员>.md`。Terry 用 `standup.py --summary` 看全队与 Blocker。站会文件不单独写 CHANGELOG |
| WL-7 | **提醒他人只出草稿**：AI 不对外发送消息（根目录硬规则 3）| skill `work-status` 生成可转发的提醒文字，由人在 Slack / Teams 中发送 |
| WL-8 | **不写敏感信息**：记录、站会、提醒中不得出现居民可识别信息、健康信息、密钥 | 与 `code-rules.md` P-1、ADLC AS-6 一致 |

## Blocker 的处理

- 站会中的 Blocker 写清楚"卡在哪、需要谁"；需要 Terry 决定的，Terry 在当天回复或拉进周一例会
- 连续出现的同一个 Blocker，在周报（skill `weekly-update`）的"风险"中列出

## 法律依据 Legal References

- [00-company/setup-checklist.md](../00-company/setup-checklist.md) §F —— Workplace Surveillance Act 2005 (NSW)：对员工的电脑 / 设备监控须提前 14 天书面通知并有书面政策
- [03-legal-compliance/checks/2026-10-11_adlc.md](../03-legal-compliance/checks/2026-10-11_adlc.md) —— ADLC 工作记录是否构成 computer surveillance：⚠️ 待律师确认
- [03-legal-compliance/research/state-by-state-comparison.md](../03-legal-compliance/research/state-by-state-comparison.md) §2 —— 各州监控法对比

⚠️ 以上为内部工作底稿，不构成法律意见。
