---
name: standup
description: Submit a CareKind AI team member's daily standup through the AI (yesterday / today / blockers), with automatic reminders of unfinished PRDs and tasks, newly assigned PRDs and previous blockers, and save the report; or show the team's standup summary for a day. Use for "提交站会", "早会", "站会", "standup", "daily standup", "今天站会", "站会汇总", "谁还没交站会", "有什么 blocker".
---

# standup

规则：`company-os/11-rules/work-log-rules.md` WL-6。报告存放在 `company-os/02-operating-rhythm/standups/YYYY-MM-DD_<成员>.md`，格式见该目录 `README.md`。

## 操作 A：提交站会（默认）

1. **确定成员**：读环境变量 `CAREKIND_MEMBER`（PowerShell `$env:CAREKIND_MEMBER`）。未设置 → 问"你是哪位成员？"（必须是 `05-hr-teams/team-roster.md` 中的名字），并提示按 WL-1 设置。学习项目中 Terry 可以说"以 Matt 身份提交站会"来扮演成员
2. **先提醒**：运行 `python company-os/11-rules/standup.py --context --member <成员>`，把结果原样告诉成员：
	- 未完成的 PRD 与任务
	- 上次站会后**新分配**的 PRD（和不再负责的 PRD）
	- 上次的"今天计划" → 逐条问是否完成
	- 上次的 Blockers → 逐条问是否已解决
3. **收集三项**（成员没说的就问，不要替人编）：
	- 昨天完成
	- 今天计划（提醒对照第 2 步的未完成 PRD / 新分配 PRD）
	- Blockers：卡在哪、需要谁；没有写"无"
4. **写报告**：用文件编辑工具写 `standups/<今天日期>_<成员>.md`，按 README 格式；"负责的 PRD（自动）""未完成任务（自动）"两节照抄第 2 步的脚本输出（PRD 一行一个路径）。当天已存在 → 更新同一份，不新建
5. **回复**：一段可直接贴到 Slack / Teams 站会频道的文字（昨天 / 今天 / Blockers），由成员自己发送。有 Blocker 需要 Terry 决定时，在回复中单独标出

## 操作 B：查看站会汇总

运行 `python company-os/11-rules/standup.py --summary [--date YYYY-MM-DD]`，列出谁已提交、每个 Blocker。需要细节时再读对应报告。

## 禁止

- 代他人提交，或修改他人的站会报告（Terry 扮演成员练习时以该成员身份提交，属于正常使用）
- 编造进展；替成员判断 Blocker 已解决
- 写入居民可识别信息、健康信息、密钥
- 统计提交率、连续天数、排名（WL-5）
- 对外发送消息（根目录硬规则 3）—— 只给可转发的文字
- 为站会单独写 CHANGELOG 条目（WL-6）
