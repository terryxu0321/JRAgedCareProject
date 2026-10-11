---
name: assign-prd
description: Assign a CareKind AI PRD (docs/PRD.md or a feature spec in company-os/06-app-development/specs/) to exactly one team member as its Assignee, reassign it, or list who owns which PRD. Use for "分配 PRD", "指派负责人", "PRD 分给谁", "改派", "assign PRD", "set assignee", "reassign spec", "PRD 负责人一览".
---

# assign-prd

每个 PRD **有且仅有一个** Assignee（负责推进该 PRD 落地的人）。Assignee 写在 PRD 文件头部，这一行是唯一来源；不另建登记表（DRY）。`check_rules.py` 的 `ASSIGN` 检查自动保证"最多一行、只有一个名字、且是名册成员"。

- **PRD 的范围**：`docs/PRD.md` 与 `company-os/06-app-development/specs/*.md`（`README.md` 除外）
- **Assignee ≠ Owner**：Owner 是对产品决策负责的人（目前都是 Terry）；Assignee 是负责实现与推进的那一个人，可以是 Terry、Ahmad、Matt 或 Dave

## 输入（缺少就问，不要猜）
- 操作：分配 / 改派 / 查看一览
- PRD：文件路径或功能名（含糊时列出候选让人选）
- Assignee：一个人名（必须在 `company-os/05-hr-teams/team-roster.md` 名册中）；没给就按步骤 3 给出建议，由人决定

## 写法（只用这两种之一，整份文件只出现一次）
- PRD 头部是表格（如 `docs/PRD.md`）：在 `Owner` 行下方加 `| Assignee | Ahmad |`
- PRD 头部是列表（specs 模板）：在 `- Owner / 状态 / 目标发布` 行下方加 `- Assignee: Ahmad`

## 步骤
1. 读 `team-roster.md`，得到可分配的成员名单；名字不在名单中 → 停下来，提示先用 skill `onboard-team-member`
2. 读目标 PRD 头部，找已有的 `Assignee` 行：
	- 没有 → 分配
	- 已有且是同一人 → 告知无需改动，结束
	- 已有且是另一人 → 这是**改派**，在输出中写明"原 Assignee → 新 Assignee"，进入 🛑 确认
3. 按 `company-os/11-rules/prd-assignment-rules.md` 匹配：
	- 判定 PRD 难度 L1/L2/L3（§2），依据 PRD 涉及的模块（PRD Part C、`06-app-development/src/` 各模块 `AGENTS.md`）；写明命中的条件，拿不准按高一级
	- 人**没指定** Assignee：扫描全部 PRD 现有的 Assignee，按"门槛 → 方向 → 负荷 → 轮换"（§3）给出**一个**建议人选并说明理由；级别与主方向只读名册，名册为 `[待填]` 时如实说明并按规范 §1 处理，不推断个人能力或偏好
	- 人**已指定** Assignee：检查级别门槛与负荷上限，不满足时在 🛑 确认前明确提示（如"Junior 担任 L3，违反 prd-assignment-rules §1"）；Junior 担任 L2 须写明导师 / 必审人（§4）
4. 🛑 人工确认：Product Owner（Terry）确认 Assignee（分配与改派都要确认）。非交互运行时在此停止，把待确认项写在输出顶部
5. 确认后用文件编辑工具写入或替换那**一行** Assignee；不得新增第二行，不得写多个名字（如 `Ahmad, Matt`、`Ahmad/Matt`），不得写"待定"之类占位
6. 运行 `python company-os/11-rules/check_rules.py`，必须通过（`ASSIGN` 无失败）
7. 按 `changelog-rules.md` 在 `changelog/CHANGELOG.md` 顶部追加记录（写明 PRD、Assignee、是否改派）

## 查看一览
不改文件：列出每份 PRD 的路径与 Assignee，未分配的标"⚠️ 未分配"，并统计每人负责数量。

## 输出
- 被修改的 PRD 文件头部的一行 `Assignee`
- 回复中给出：PRD、难度（L1/L2/L3 及命中条件）、Assignee 及其级别/主方向（改派时含原 Assignee）、各成员当前负责数量

## 禁止
- 一个 PRD 分给多人或"共同负责"—— 需要协作时，在 PRD 正文写协作者，Assignee 仍只有一人
- 自行决定 Assignee 而跳过 🛑 确认
- 修改 PRD 的其他内容（范围、法律依据、Owner 等）
- 对外通知被分配的人（邮件、Slack 等）—— 只在回复中给出可转发的通知草稿，由人发送
- 推断任何人的性别或代词（用姓名或"他们/they"）
