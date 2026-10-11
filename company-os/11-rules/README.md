# 11 · Rules 规范

> Owner: Terry ｜ 适用：全体成员（Terry、Ahmad、Matt、Dave 及以后的成员）**和所有 AI 助手（Claude、Codex）** ｜ 复审：每季度

规范是"必须这样做"。其他文档（政策、手册、PRD）描述"是什么"和"为什么"，规范规定"怎么做"。

| 规范 | 适用于 | 一句话 |
|---|---|---|
| [company-rules.md](company-rules.md) | 所有人、所有工作 | 公司规范：保密、数据、沟通、决策、文档、使用 AI 工具 |
| [operations-rules.md](operations-rules.md) | 运营、销售、客户成功、市场、财务 | 运营规范：客户、试点、支持、宣传、供应商、支出、事件 |
| [code-rules.md](code-rules.md) | 所有代码 | 代码规范：**核心 15 条**、SOLID / DRY / KISS、Tab 缩进宽度 4、安全失败、隐私、AI 管线、测试、单文件 ≤ 1000 行自动重构、性能底线、类型 |
| [any-whitelist.md](any-whitelist.md) | 配合代码规范 | 获批允许使用 `any` 的场景（当前为空） |
| [product-legal-rules.md](product-legal-rules.md) | 产品设计、PRD、spec | **产品设计和写 PRD 必须参考本地法律文件** |
| [legal-reference-index.md](legal-reference-index.md) | 配合上一条使用 | 产品话题 → 应查阅的本地法律文件 |
| [work-log-rules.md](work-log-rules.md) | 所有成员通过 AI 操作仓库时 | 按成员自动记录工作、随时提醒未完成工作、在 AI 中提交每日站会（[DR-008](../02-operating-rhythm/decisions/DR-008-member-work-log-and-standup.md)，提议中） |
| [prd-assignment-rules.md](prd-assignment-rules.md) | 分配 / 改派 PRD | PRD 按难度（L1–L3）与成员级别、主方向、负荷匹配，Terry 确认（[DR-007](../02-operating-rhythm/decisions/DR-007-prd-assignment-by-level.md)，提议中） |
| [ai-context-rules.md](ai-context-rules.md) | 所有目录层级 | 每层都有 README / AGENTS / CLAUDE 三件套 |
| [changelog-rules.md](changelog-rules.md) | 所有 AI 修改 | AI 每次修改自动记录到 `changelog/ai-edits.jsonl`，每个任务写一条 `changelog/CHANGELOG.md` |

自动化脚本：[check_rules.py](check_rules.py)（全部可自动检查的规则）· [rule_config.py](rule_config.py)（阈值与文件分类，唯一定义处）· [hook_file_size.py](hook_file_size.py) 与 [hook_log_change.py](hook_log_change.py)（Claude Code hooks，配置在 `.claude/settings.json`）· [work_items.py](work_items.py)（成员未完成工作、工作记录；SessionStart hook）· [standup.py](standup.py)（站会提醒与汇总）

## 优先级（冲突时）

1. 法律法规（以 `03-legal-compliance/` 中的本地文件和律师意见为准）
2. 已决定的决策记录（DR）
3. 本文件夹的规范
4. 其他文档与个人习惯

规范与 DR 冲突时，以 DR 为准，并在 2 周内修订规范。

## 如何执行

| 机制 | 作用 |
|---|---|
| 根目录 `AGENTS.md`（Claude 通过 `CLAUDE.md` 引用） | 要求 AI 助手在对应任务前阅读并遵守这些规范 |
| skill `spec-writer`、workflow `new-feature-gate` | 写 PRD/spec 时强制查阅本地法律文件并填写"法律依据" |
| `python company-os/11-rules/check_rules.py` | 自动检查：法律依据（LEGAL）、Tab 格式（FORMAT）、文件大小（SIZE）、硬编码密钥（SECRET）、空 catch（CATCH）、占位/TODO（PLACE）、未登记 any（ANY）、上下文三件套（CONTEXT）、PRD 唯一 Assignee（ASSIGN，见 [DR-006](../02-operating-rhythm/decisions/DR-006-prd-single-assignee.md)） |
| Claude Code hooks（`.claude/settings.json`） | 每次编辑后：记录到 changelog、检查文件大小并触发重构 |
| 代码评审（PR 检查清单） | 按 code-rules 评审 |

## 修改规范

- Type 2 小修改（措辞、补例子）：直接改，在周报中说明
- 新增或删除"必须"类条款：写 DR，Terry 批准
- 规范中的"必须 / 禁止"是硬性要求；"建议"可在说明理由后偏离
