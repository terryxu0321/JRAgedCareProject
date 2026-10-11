# PRD 分配规范 PRD Assignment Rules

> Owner: Terry ｜ 适用：分配或改派 PRD（`docs/PRD.md`、`06-app-development/specs/*.md`）的人和 AI 助手 ｜ 执行：skill `assign-prd` ｜ 决策：[DR-007](../02-operating-rhythm/decisions/DR-007-prd-assignment-by-level.md)（提议中）｜ 复审：每季度

[DR-006](../02-operating-rhythm/decisions/DR-006-prd-single-assignee.md) 规定"每个 PRD 只有一个 Assignee"；本规范规定"**该给谁**"：按 PRD 难度与成员级别、方向匹配，再看负荷。最终由 Terry 🛑 确认。

## 1. 成员属性（唯一来源：[团队名册](../05-hr-teams/team-roster.md) 的"级别""主方向"两列）

**级别**

| 级别 | 含义（只看可观察的工作表现） | 可担任 Assignee 的难度 |
|---|---|---|
| Junior | 在清晰的需求和评审下完成单模块任务 | L1；L2 仅作为"成长任务"（见 §4） |
| Mid | 独立交付端到端功能，能拆分任务、写测试 | L1、L2 |
| Senior | 能做架构设计、处理高风险模块、带新人 | L1–L3（优先 L2/L3） |
| Lead | Tech Lead（Terry），兼 Product Owner | L3 兜底：没有可用的 Senior 时才担任 |

**主方向**（可写一个或"全栈"）

| 主方向 | 对应模块（`06-app-development/src/`） |
|---|---|
| 移动端与前端 | `mobile-app`、`admin-web` |
| 后端与基础设施 | `api`、`review-service`、`record-store`、`integrations` |
| AI 管线 | `ai-pipeline` |
| 全栈 | 跨 2 个及以上模块的端到端功能 |

- 级别与方向由 **Terry 评定**，写入名册；每季度或成员申请时复审。AI 不得推断或修改
- 名册中级别为 `[待填]` 的成员，只能被建议为 L1 的 Assignee，并提示 Terry 先评定

## 2. PRD 难度（取命中的最高一级）

| 难度 | 命中任一条即属于该级 |
|---|---|
| **L3 高风险** | 改变 AI 输出（PRD C2–C3 管线，尤其是**归属** attribution、**护栏** guardrails；须跑临床评测、Clinical Lead 签字 A-2）· 审核状态机 / HITL / 事件快速通道（`review-service`）· 签字记录、保留与删除（`record-store`）· 认证授权、审计、加密、数据驻留（`api`、基础设施）· 回写外部护理系统（`integrations`）· 涉及 3 个及以上模块 · 需要新的架构或供应商决策 · 整份 `docs/PRD.md` |
| **L2 中等** | 跨 2 个模块的端到端功能（如 `mobile-app` + `api`），且不命中 L3 · 不改变 AI 输出的管线工具（如转写的性能、日志、评测脚本） |
| **L1 简单** | 单模块、需求清晰、不改变居民数据的处理路径：如 `admin-web` 页面、App 界面调整、导出格式、内部工具、补测试 |

判断依据：PRD 正文涉及的模块 + 各模块 `AGENTS.md` 中的 hard rules 与 clinical hazards。拿不准时按高一级处理（安全失败）。

## 3. 选人顺序

1. **门槛**：只保留"级别可担任该难度"的成员（§1 表）
2. **方向与技能**：优先主方向覆盖 PRD 主要模块的人；跨模块的 L2 优先"全栈"；再参考个人档案"技能"（如产品思维、审美 → 偏界面与用户流程的 PRD；DevOps → 部署与基础设施的 PRD）
3. **负荷**：优先当前负责未发布 PRD 最少的人。上限：Junior 1 份、Mid 2 份、Senior 2 份、Lead 1 份；到上限的人不建议
4. **轮换**：仍并列时，优先最近没负责过该模块的人（避免知识只在一个人身上）
5. 仍并列 → 列出并列者，由 Terry 决定

PRD 太大、找不到合适的单个 Assignee 时：把它拆成多份 spec，各自有 Assignee —— **不要**改成多人共同负责（DR-006）。

## 3a. 整份 PRD 归一人（含它的全部任务）

- PRD 拆出的**所有任务**（`adlc/tasks/`），`owner` 与 `executor` 都是该 PRD 的 Assignee；**不把同一份 PRD 的任务拆给不同成员**
- AI（Claude Code、Codex）可以作为执行者"代 Assignee 执行"，`owner` 仍是 Assignee（AI 不能当负责人，ADLC AS-1）
- 评审人必须是**另一位**人类（ADLC AS-2），默认 Terry；Terry 是 Assignee 时由一位 Developer 评审（§5）。评审不算"分配到的工作"
- 改派 PRD 时，它的全部未完成任务一并改派给新 Assignee
- 选人时（§3）把整份 PRD 的工作量当作一个单位来衡量；一个人做不完 → 拆 PRD（见上），而不是拆任务给别人

## 4. 成长任务（Junior 担任 L2）

- 须 Terry 明确同意，并在 PRD 正文写明一位 Senior 或 Lead 作为**导师 / 必审人**；Assignee 仍只有 Junior 一人
- L3 不作为成长任务。Junior、Mid 想参与 L3 工作 → 把可独立的部分拆成单独的 L1 / L2 spec 分给他们（§3a），而不是在 L3 PRD 里分任务

## 5. 制衡

- L3 的代码须由 Assignee 以外的 Senior 或 Lead 评审；影响 AI 输出的发布须 Clinical Lead 签字（code-rules A-2）
- Terry 担任 Assignee 时，生产/安全相关变更仍须 Ahmad、Matt 或 Dave 至少一人评审（[组织与角色](../05-hr-teams/org-and-roles.md)，四眼原则）

## 6. 公平与合规

- 只按**与工作相关的能力和负荷**分配；不得考虑年龄、性别、种族、残疾、签证身份、家庭状况等受保护属性（[行为准则](../05-hr-teams/code-of-conduct.md) 第 5 条；[招聘与入职](../05-hr-teams/hiring-and-onboarding.md) 所列反歧视法）
- 级别只描述工作能力，不记录薪酬或绩效评语（`05-hr-teams/AGENTS.md`）
- 成员可以看到自己的级别，并可向 Terry 申请复审
- ⚠️ 本节为内部工作底稿，不构成法律意见；反歧视法的适用尚未在 `03-legal-compliance/` 中做专门分析（未核实）

## 7. 执行

- 本规范管 PRD 的 Assignee，并通过 §3a 决定它全部任务的负责人与执行者；任务文件格式、状态流转、WIP 与评审规则按 [ADLC spec](../06-app-development/specs/2026-10-adlc-delivery-lifecycle.md) §6
- skill `assign-prd` 在"人没有指定 Assignee"时按 §3 给出**一个**建议，并写明 PRD 难度、命中的条件和理由
- `check_rules.py`（ASSIGN）只校验"唯一 Assignee 且在名册中"，**不**自动校验级别匹配 —— 由 Terry 🛑 确认把关
- 人指定的 Assignee 不满足 §1 门槛时，skill 须在确认前明确提示（例如"Junior 担任 L3，违反本规范 §1"），由 Terry 决定是否改人或拆分 PRD
