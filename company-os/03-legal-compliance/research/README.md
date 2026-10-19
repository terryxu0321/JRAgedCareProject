# CareKind AI — 法律合规研究（养老护理文档）

日期：2026-10-10 · 状态：内部研究草稿，**非法律意见** · ⚠️ = 待律师确认 / 未核实

## 索引

| 文件 | 内容 |
|---|---|
| [`federal-law-summary.md`](federal-law-summary.md) | 交付物 A：Aged Care Act 2024 / Rules 2025（记录保存、Statement of Rights、Quality Standards、SIRS、restrictive practices / BSP、AN-ACC、care minutes / 24/7 RN、QI、Support at Home）、Privacy Act / NDB / 2024 修订 / Tranche 2、TGA、Ahpra/NMBA、ACSQHC |
| [`state-by-state-comparison.md`](state-by-state-comparison.md) | 交付物 C：8 个州/领地的健康记录与隐私法、监听设备与工作场所监控法、RN/配比法、监护与 ACD、成人保护、记录保存、VAD 等；按主题对比表 + 分州摘要 |
| [`state-deep-dive-nsw-vic-act.md`](state-deep-dive-nsw-vic-act.md) | 2026-10-19 补充：NSW / VIC / ACT 健康隐私、录音法、药品记录、监护与同意的深挖与纠错建议 |
| [`state-deep-dive-qld-wa-sa-tas-nt.md`](state-deep-dive-qld-wa-sa-tas-nt.md) | 2026-10-19 补充：QLD / WA / SA / TAS / NT 同上；含五辖区对比表与对 `state-by-state-comparison.md` 的 15 条纠错建议（待人工采纳） |
| [`aged-care-documentation-workflows.md`](aged-care-documentation-workflows.md) | 2026-10-19 交付物 D：真实文档流程（入住、班次、事件/SIRS、care plan、限制性措施、恶化、QI、临终、投诉）Mermaid 流程图 + CareKind 介入点 + 临床/AI 文档 best practice |
| [`aged-care-paperwork-checklist.md`](aged-care-paperwork-checklist.md) | 2026-10-19 交付物 D 附表：约 60 种文档 × 时机 × 填写人 × 保存年限 × 依据 × 模板 × CareKind 能否起草 |
| [`paperwork-templates-index.md`](paperwork-templates-index.md) | 交付物 B：59 个已下载官方表格/模板/指南（约 80 MB）索引及下载失败的 URL |
| [`downloads/`](downloads/) | federal-aged-care、sirs-incidents、restrictive-practices、care-planning-assessment、quality-indicators、clinical-handover、privacy、ai-digital-scribes、state-specific |
| [`sources.md`](sources.md) | 来源汇总 |

## 执行摘要

1. **监管框架已全面换代**：*Aged Care Act 2024* 与 *Aged Care Rules 2025* 自 2025-11-01 生效。Rules 一年内已汇编 11 次（最新 2026-09-20），文档义务细节都在 Rules 中，需持续跟踪。
2. **7 年记录保存是联邦基线**（Rules s 154 系列：服务交付、事故、投诉、QI、申领、合规等）。NSW/VIC/ACT 健康记录法另有"最后一次服务后 7 年 / 未成年人至 25 岁"及删除登记要求。
3. **记录质量本身就是合规义务**：Quality Standards Outcome 2.7 要求记录"accurate and current"且可被本人理解；Outcome 3.3 要求关键信息与病情恶化有效沟通（交接班）。AI 错误会直接成为客户的合规风险，也正是 CareKind 的价值主张所在。
4. **高价值文档场景具备明确法定字段**：事故记录（s 164-25，13 项字段，SIRS P1 24h / P2 30d / final report 84 天）；限制性措施与 BSP（s 162-15~162-75，使用时间、持续、频率、替代策略、同意、监测）；care and services plan（s 148-80，每 12 个月复审，更新后提供副本）；24/7 RN 月报（月后 7 天内）。这些可直接变成产品模板。
5. **TGA 边界清晰但执法收紧**：仅转录/整理且不分析解释的 scribe 不是医疗器械；生成未口述的诊断/治疗建议即为医疗器械。TGA 2026 年 8 月宣布转入执法，重点是 scope creep。
6. **Ahpra 对产品的直接要求**：护士对 AI 记录负责；AI 转录软件"应在第一步包含明确同意环节"；告知居民 AI 的使用及数据去向。
7. **录音同意是最大的州际差异**：NSW、WA、SA、TAS、ACT 录制私人对话原则上需全体当事人同意（刑事责任）；VIC、QLD、NT 当事人可录但限制传播（⚠️ 需律师逐州复核）。→ 产品应采用"护士离开居民后 push-to-talk 口述"模式，而非房间内常开 ambient 录音。
8. **隐私改革进行中**：APP 1.7–1.9 自动化决策透明度 **2026-12-10** 生效；Tranche 2 exposure draft（2026-08-31）提议 controller/processor、72 小时 breach 通报、"fair and reasonable" 检验 —— 尚未立法，但应按其方向设计。NSW/VIC/ACT 健康记录法直接约束私营机构，VIC HPP 9 / NSW HPP 14 限制跨境传输 → **数据应托管在澳洲境内**（包括 LLM 推理）。
9. **同意来源须可记录**：restrictive practices 的替代决策人由各州监护法决定，Rules 层级仅为后备；文档模板应能记录 consent 来自本人 / supporter / SDM。

## 对 CareKind AI 的关键产品与合规含义

**产品设计（MVP 必须）**
- 书面 **intended purpose**：documentation-only；输出护栏禁止生成口述中未出现的诊断、治疗、用药或护理建议；新功能上线前做 TGA 定性复核并留档。
- **Push-to-talk 口述**为默认；首次使用及每位居民的同意/告知流程（Ahpra "explicit consent as initial step"）；UI 提示勿在居民私人对话中录音；ambient 模式暂不做。
- **人工审核必经**：AI 草稿须由护士审阅/编辑/确认后才推送；PCW 草稿可配置 RN 会签。
- **完整 audit trail**：口述者、AI 版本、修改差异、审核人、时间戳 —— 支持客户 7 年举证与 ACQSC 审核。
- **结构化模板**映射法定字段：progress note、ADL、incident（s 164-25）、restrictive practice 使用记录 → BSP（s 162-60）、handover（ISBAR / Outcome 3.3）。
- **SIRS 计时提醒**（24h/30d）及"可能属于 reportable incident，请按机构流程判定"的提示 —— 只提示、不判定。
- 原始音频**短期保留后删除**（可配置），最终记录以客户系统为 source of truth；删除可留日志（NSW s 25 / VIC HPP 4.3）。

**数据与隐私**
- 澳洲境内托管（含 LLM 推理区域）；子处理方零数据保留；**不使用客户数据训练模型**（Act s 168 用途限制 + OAIC AI 指南 + APP 6）。
- 按 processor 模式准备 DPA、子处理方清单、安全说明（APP 11、Cyber Security Act 2024）、PIA（OAIC 指南已下载）和 data breach response plan（为 72 小时通报预备）。
- 即使营业额 <$3m，也按 Privacy Act 完全适用设计。

**市场与销售**
- 合规卖点：减少文档时间（释放 care minutes）、提高 Outcome 2.7 记录质量、SIRS/BSP 完整性。避免以"提高 AN-ACC 资金"作营销。
- 公立客户（Vic PSRACS、Qld MPS 等）会附加州公共部门隐私法、档案法与安全标准（VPDSS），可作为第二阶段。

## 需律师确认的事项（优先级排序）

1. 各州监听/监控设备法对"护士口述可能录入他人声音"及 CareKind 作为软件提供方的适用性（尤其 NSW、WA、SA、TAS、ACT）。
2. CareKind 是否直接受 Privacy Act 约束（small business exemption）以及 NSW/VIC/ACT 健康记录法下的直接义务；Tranche 2 下的 processor 角色。
3. CareKind 侧音频、草稿、日志是否构成需保存 7 年（或至 25 岁）的 "records"/"health records"。
4. "缺失信息提示 / reportable incident 提示 / 恶化关键词标记"等功能是否越过 TGA 医疗器械边界。
5. 使用境外 LLM 子处理方的 APP 8、HPP 9（VIC）、HPP 14（NSW）合规。
6. NSW Public Health Act s 104 现行文本与新 Act 的关系；Vic Safe Patient Care Act 2025 修正案状态（影响较小）。
7. 客户合同中的责任分配：AI 错误导致的 Quality Standards / SIRS 违规、赔偿上限、保险（PI/cyber）。

## 已知局限

- 部分州立法网站（NSW、AustLII）被拦截，相关条文依赖二手资料 ⚠️。
- 部分已下载 ACQSC 指南（SIRS guidelines、incident management、BSP fact sheet）仍可能引用旧 *Aged Care Act 1997*，正在更新中。
- TGA 数字 scribe 审查结果与新开发者指南截至本日未核实是否已发布。
- 部分下载材料为 CC BY-NC-ND 或受版权限制（如 DSA BSP 模板、AN-ACC 手册中的量表），**不得直接复制进产品**，仅作结构参考。
