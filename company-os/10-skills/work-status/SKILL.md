---
name: work-status
description: Show what work a CareKind AI team member still has open (assigned PRDs, ADLC tasks, reviews waiting), show one member's work record, or draft a reminder message to a member about unfinished work. Use for "我还有什么没做", "Matt 还有什么工作", "提醒 Dave", "待办", "工作记录", "谁负责什么", "work status", "what's left", "remind".
---

# work-status

规则：`company-os/11-rules/work-log-rules.md`（WL-3 工作来源、WL-4 提醒、WL-5 不做绩效监控、WL-7 提醒只出草稿）。

## 输入
- 哪位成员：没说 → 用 `CAREKIND_MEMBER`；"全队"→ 所有人
- 要做什么：查未完成工作（默认）/ 查工作记录 / 起草提醒

## 步骤
1. **未完成工作**：运行 `python company-os/11-rules/work_items.py [--member <成员>]`（不带 `--member` = 全队）。结果来自 PRD Assignee 与 ADLC 任务，不要另外推测别的待办
2. **工作记录**（只按单人）：运行 `python company-os/11-rules/work_items.py --member <成员> --log [--days N]`，列出该成员请求的 CHANGELOG 任务与 AI 改过的文件
3. **起草提醒**：根据第 1 步结果，为对方写一段简短、友好的提醒（有哪些 PRD / 任务未完成，有截止日的写截止日）。只放在回复中，由人发送
4. 需要看今天谁交了站会 → 改用 skill `standup` 的"查看站会汇总"

## 输出
- 每位成员的未完成工作列表（无则写"无"）
- 起草提醒时：一段可转发的文字

## 禁止
- 统计或比较个人的完成数量、耗时、排名（WL-5）
- 对外发送提醒（根目录硬规则 3）
- 修改 PRD、任务或站会文件 —— 本 skill 只读
