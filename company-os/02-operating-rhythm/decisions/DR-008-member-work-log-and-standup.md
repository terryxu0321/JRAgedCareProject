# DR-008: 成员工作记录、待办提醒与 AI 每日站会

- **日期**：2026-10-11
- **决策人**：Terry
- **类型**：Type 2（双向门）—— 内部工作方式，可随时撤回
- **状态**：提议中
- **评论截止**：

## 背景
Terry 要求：每位成员用 AI 操作仓库时，自动记录每个人的工作；可以随时提醒每个人还有什么分配的工作没做；每位成员都在 AI 中提交每日站会（提醒未完成 PRD、新分配 PRD、Blocker），并存档每份站会报告。[运作节奏](../operating-cadence.md)已有"每日异步站会：昨天 / 今天 / 阻碍"，此前没有记录。本项目是学习项目，Ahmad、Matt、Dave 为假设成员。

## 选项
| 选项 | 优点 | 缺点 |
|---|---|---|
| A. 环境变量标明成员 + 现有 hook 记录成员名；待办只读 PRD Assignee 与 ADLC 任务；站会用 skill 写入仓库文件 | 复用现有 hook、Assignee 与 ADLC 设计，无新供应商；Claude 与 Codex 都可用 | 依赖每人正确设置环境变量；Codex 无 hook，只靠 CHANGELOG |
| B. 另建个人待办清单与站会表格 | 一眼看全 | 与 PRD / ADLC 重复（违反 DRY），容易不一致 |
| C. 用外部工具（Jira、Slack 机器人） | 功能现成 | 新子处理方与支出（[运营规范](../../11-rules/operations-rules.md)）；ADLC 第一阶段已决定不引入 |

## 推荐与理由
选 A，细则见 [work-log-rules.md](../../11-rules/work-log-rules.md)。脚本 `work_items.py`、`standup.py` 只读现有来源；skill `standup`、`work-status` 负责交互；SessionStart hook 自动提醒。不做数量、耗时、提交率、排名统计，以降低员工监控风险。

## 影响检查
- [x] 居民安全 / 临床：无影响
- [x] 隐私 / 合规：⚠️ 有真实员工后，记录员工的计算机工作活动可能构成 NSW Workplace Surveillance Act 2005 下的 computer surveillance，须提前 14 天书面通知并有书面政策（[setup-checklist.md](../../00-company/setup-checklist.md) §F）—— 待律师确认；学习项目阶段不适用
- [x] 安全：只记录元数据（时间、文件路径、成员），不记录文件内容
- [x] TGA 判定是否改变：否
- [x] 成本 / 现金跑道：无

## 决定
待 Terry 确认。确认后：状态改为"已决定"，在 `decision-log.md` 追加 DR-008 一行。

## 复审
出现第一位真实员工时（先完成书面通知），或运行一个季度后。

## 附：员工书面通知草稿（有真实员工后使用，由 Terry 发送，AI 不发送）

> 自 [日期，至少 14 天后] 起，CareKind AI 在你使用公司代码仓库中的 AI 工具（Claude Code、Codex）时，会记录：编辑的时间、文件路径、你的姓名，以及你提交的每日站会内容。记录持续进行，存放在公司仓库 `changelog/` 与 `company-os/02-operating-rhythm/standups/`。用途仅限团队协作、变更审计与研发记录，不用于绩效排名，不记录文件内容、按键或屏幕。政策全文：`company-os/11-rules/work-log-rules.md`。如有疑问请联系 Terry。
