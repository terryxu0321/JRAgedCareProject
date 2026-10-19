# 产品功能与解决方案地图 Product Feature Map（MVP）

> Owner：Terry ｜ v0.1 草稿 · 2026-10-19 ｜ 状态：🟡 待 Terry 审阅
> ⚠️ 法律相关内容为内部工作底稿，非法律意见。产品范围以 [docs/PRD.md](../../docs/PRD.md) 为唯一来源；本文件只把 2026-10-19 的调研结果映射到 MVP 功能，并汇总 best practice。学习项目 MVP：只列 P0 与必要的 P1。

## 1. 依据（本次调研）

| 调研 | 文件 | 对产品最重要的结论 |
|---|---|---|
| 竞品如何解决 | [how-competitors-solve-it.md](../07-marketing-operations/competitor-research/how-competitors-solve-it.md) | voize（德国）已做"口述→自动归属居民"，澳洲无人提供；"澳洲托管 + 音频即删 + 不训练"已是入场券；没有产品做居民级同意；TGA 2026-10 审查：12 款 scribe 中 8 款可能属器械，免责声明无效 |
| 真实流程与 paperwork | [aged-care-documentation-workflows.md](../03-legal-compliance/research/aged-care-documentation-workflows.md)；[aged-care-paperwork-checklist.md](../03-legal-compliance/research/aged-care-paperwork-checklist.md) | 4 个 HITL 闸门；约 18 类一线文档 CareKind 可起草；SIRS P1 24h / P2 30 天；ISBAR 的 A/R 含临床判断，只能用护士原话 |
| 各州法规 | [state-by-state-comparison.md](../03-legal-compliance/research/state-by-state-comparison.md)；[NSW/VIC/ACT 深挖](../03-legal-compliance/research/state-deep-dive-nsw-vic-act.md)；[QLD/WA/SA/TAS/NT 深挖](../03-legal-compliance/research/state-deep-dive-qld-wa-sa-tas-nt.md) | 护士单人口述一般不算"私人对话"→ 模式 A 风险最低；环境录音多数辖区实际需全体同意；NSW/VIC/TAS/NT 隐私法管"出州"，"留在澳洲"不够；州法与 Aged Care Act 2024 叠加适用；CareKind 不得被配置成药品登记册 |

## 2. 问题 → 解决方案 → 功能

| 一线问题（假设，待访谈验证） | 竞品现状 | CareKind 解决方案 | MVP 功能 spec |
|---|---|---|---|
| 一个班次几十位居民，下班补记录 | 通用 scribe 以"一次问诊"为单位；Notive 等为单条 note | 班次会话 + 按键口述，离线可录 | [SPEC-004 班次语音采集](specs/2026-10-shift-voice-capture.md) |
| 每次先选居民再录音 = 摩擦 | 澳洲产品都要求先定对象 | 系统按名册自动归属，不确定就"待归属"，绝不猜测 | [SPEC-005 居民归属引擎](specs/2026-10-resident-attribution.md) |
| 写英文、写规范记录难（PCW、CALD） | 多为通用格式；ShiftCare 走向风险标签 | 按记录类型起草，只写说过的内容，禁止诊断/建议/风险评分 | [SPEC-006 草稿生成与护栏](specs/2026-10-draft-generation-guardrails.md) |
| AI 记录的责任与可信度 | HITL 多为"一句话" | 逐居民审核、关键项逐项确认、签字后只追加、逐句回听 | [SPEC-007 审核签字](specs/2026-10-review-and-sign-off.md) |
| 事件记录不全、SIRS 时限 | 通用 incident 表单或"flag" | 事件草稿按 Rules s 164-25 字段 + 自观察起计时，只提醒不判定 | [SPEC-008 事件快速通道](specs/2026-10-incident-fast-track.md) |
| 录音与 AI 处理的同意 | 多数推给机构（PCC 合同最极端） | 居民级同意状态、替代决策人来源、未同意即丢弃 | [SPEC-009 同意管理](specs/2026-10-consent-management.md) |
| 买单的是养老公司老板，旗下多家、多地点养老院；要管员工、老人和流程 | 澳洲 CMS 各管各院，AI 记录工具不管多院运营 | 养老院管理端：公司总览、多院管理、完整员工名册、老人生命周期、审核与上报流程、上线闸门 | [SPEC-011 养老院管理端](specs/2026-10-provider-admin-console.md) |
| 平台方要开通多家客户公司，但不能接触居民数据 | — | 独立 Super Admin App：开通/配置客户公司、公司管理员账号、去标识用量 | [SPEC-010 Super Admin](specs/2026-10-super-admin-console.md) |
| 双录、记录不在正式系统 | 澳洲 CMS 均无 AI 记录 | MVP 导出（复制/PDF）+"已转入机构系统"标记；回写放 H2 | PRD E6 E-01、S-08（暂不单独 spec） |

暂不做（P1/P2，见 PRD G2）：多语言回译、PCW→RN 复核队列、交接摘要、时间线增强、CMS 回写、限制性措施记录。

## 3. Best Practice 汇总（我们的做法）

由三份调研合并而成，每条后标来源与落地位置。

### 3.1 合规与边界

1. **用功能边界证明 documentation-only，不靠免责声明**：TGA 已明确声明不能决定定性 → 护栏阻止诊断/治疗/用药建议/风险评分，并用评测证据证明（[竞品 §5](../07-marketing-operations/competitor-research/how-competitors-solve-it.md)；[TGA 自评](../03-legal-compliance/tga-samd-assessment.md)）→ SPEC-006
2. **按键口述，不做环境录音**：多数州录私人对话须全方同意，违反为刑事犯罪（[recording-consent.md](../03-legal-compliance/recording-consent.md)；PRD B4）→ SPEC-004
3. **同意做进产品，而不是推给机构**：居民级状态 + 来源（本人 / supporter / SDM）+ 撤回即生效（ACSQHC ambient scribe 场景）→ SPEC-009
4. **澳洲驻留、不训练、原音短期删除**是入场券，必须做到并写进 DPA，但不作为卖点宣传
5. **只提醒，不判定**：SIRS 计时、缺失字段提示只针对记录字段；是否上报由机构人员决定（TGA 灰区，待监管顾问确认）→ SPEC-008

### 3.2 临床文档质量（来自 NMBA / SQS / ACSQHC，见 [流程文件 §11](../03-legal-compliance/research/aged-care-documentation-workflows.md)）

6. 准确：草稿每句都能对应到来源语句，否则删除
7. 及时：保留观察时间与签字时间；事件立即提醒审核
8. 客观、以人为本：可观察描述，不加"不合作""wanderer"等标签；居民原话加引号
9. 完整：护理行动 + 结果 + 通知了谁、何时
10. 不复制粘贴：每条草稿只来自本次口述
11. 身份两要素：审核界面始终显示第二标识（房号/照片）
12. 更正只追加：签字后新版本 + 原因 + 签字，原版本保留

### 3.3 AI 文档（来自 ACSQHC / Ahpra，见 [流程文件 §12](../03-legal-compliance/research/aged-care-documentation-workflows.md)）

13. 护士对最终记录负全部责任 → 签字 = 作者确认
14. 每份输出都要审核，关键项（药名、剂量、数字、姓名、事件）逐项确认，防 automation bias
15. 记录标注"AI 辅助起草，由 X 审核"
16. 一键报告 AI 错误；影响 AI 输出的发布须 Clinical Lead 抽样

### 3.4 应避免（竞品反面教材）

- 严重度/风险标签与 detects/predicts 式宣传
- 用客户音频或转写调优模型
- 在居民房间用员工手机做 ambient 录音
- 无证据的"节省 X% 时间"宣称（ACL）

## 4. 真实流程中的位置

完整流程图见 [aged-care-documentation-workflows.md §1](../03-legal-compliance/research/aged-care-documentation-workflows.md)（全景图，含 4 个 HITL 闸门）。MVP 覆盖其中：日常班次口述 → 归属 → 草稿 → 🛑审核签字 → 导出；事件快速通道 → 🛑事件签字。交接摘要（🛑 H4）与 RN 复核（🛑 H3）为 P1。

## 5. Paperwork 模板

可复制使用的 Markdown 模板在 [templates/paperwork/](../templates/paperwork/README.md)：progress note、事件记录、ISBAR 交接、care plan 复审记录、限制性措施使用记录、居民 AI 告知与同意书、员工监控通知、机构上线清单。

## 6. 待确认

- 访谈前所有"一线问题"均为假设（`08-feedback/raw/` 为空）
- SPEC-008 计时提醒、缺失字段提示是否越过 TGA 边界 —— 监管顾问
- 同意书与员工通知措辞 —— 律师
- 6 份 spec 的 Assignee —— Terry 用 skill `assign-prd` 分配
