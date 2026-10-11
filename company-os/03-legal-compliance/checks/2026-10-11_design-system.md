# 合规检查：CareKind Design System spec v0.1

> 2026-10-11 · 检查对象：[specs/2026-10-design-system.md](../../06-app-development/specs/2026-10-design-system.md)（类型：feature，产品基础设施）· 检查方式：skill `compliance-check` · ⚠️ **内部工作底稿，非法律意见**

## 结论：有条件通过

设计系统不生成任何 AI 输出，不处理居民数据，不改变产品边界。它把 HITL 与多项 hazard 缓解措施（H-01、H-02、H-03、H-06、H-07、H-08、H-09）做成统一组件，整体降低风险。条件：无障碍相关法律须先补充到本地文件（T-0009）；安全关键组件须 Clinical Lead 审阅后才能用于生产。

## 逐项结果

| 领域 | 结果 | 说明 |
|---|---|---|
| TGA | ✅ | 不生成诊断 / 治疗 / 用药建议；明确禁止风险等级、临床预警、严重程度色标组件（[tga-samd-assessment.md](../tga-samd-assessment.md) 功能闸门表："跌倒风险评分" = 器械）；文案规范列入禁用词 |
| 隐私（APPs + NSW HRIP） | ✅ | 无新数据类型；隐私遮罩、锁屏通知不含健康信息；设计稿与文档只用合成数据（[privacy-program.md](../privacy-program.md) §2、§3）；无需新 PIA |
| 录音同意 | ➖ | 不涉及（不改变按键口述默认） |
| HITL | ✅ | AI 内容以草稿呈现，逐段确认，无"全部一键确认"；强化 Ahpra 关于护士对 AI 记录负责的要求（[federal-law-summary.md](../research/federal-law-summary.md) §4） |
| 临床安全 | ⚠️ | 建议新增 H-17（草稿与已确认记录区分不清）、H-18（组件被误用表示临床严重程度）；须 Clinical Lead 审阅 |
| 无障碍 / 残障歧视 | ⚠️ | 本地法律文件未覆盖 DDA 1992 与数字无障碍要求；WCAG 2.2 AA 目前是 PRD E7 的产品决定，非经核实的法律结论 → T-0009 补充（L-4） |
| ACL / 营销 | ✅ | token 若用于对外物料，发布前走[市场合规](../../07-marketing-operations/marketing-compliance.md)清单；图片不用真实居民照片 |
| 子处理方 | ⚠️ | 设计工具若为新 SaaS：不放个人信息，但须按运营规范审批支出，并决定是否登记子处理方清单 |
| Aged Care | ✅ | 支持 Quality Standards 2.7（记录准确、可理解）与 3.3（安全沟通）（[aged-care-alignment.md](../aged-care-alignment.md)） |

## 修改建议

1. 已并入 spec：§4 明确"不做"临床严重程度类组件；§5.3 草稿卡三态不只靠颜色
2. 已并入 spec：§6 "无障碍"一行标为本地文件未覆盖，并建任务 T-0009
3. 建议：组件评审清单加一条"是否表达了临床判断或风险等级？"（T-0003 / T-0005 执行时加入）

## 需律师确认

1. CareKind 作为软件供应商在 Disability Discrimination Act 1992 下的义务范围；客户采购是否要求 WCAG 合规声明（T-0009 补充本地文件后提出）

## 需更新的文档（只建议，不直接修改）

| 文档 | 建议 |
|---|---|
| [hazard log](../../06-app-development/clinical-safety-framework.md) | 建议 H-17、H-18，待 Clinical Lead 审阅后由人加入 |
| [legal-reference-index.md](../../11-rules/legal-reference-index.md) | T-0009 完成后新增"无障碍"话题 |
| [合规登记册](../compliance-register.md) | 视 T-0009 结论决定是否新增 DDA / 无障碍一行（由 Terry 批准） |
