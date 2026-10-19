# 养老护理 Paperwork 总表 Aged Care Paperwork Checklist（Deliverable D 附表）

> **内部工作底稿，非法律意见、非临床意见。** 核查日期：**2026-10-19**。Owner：Terry ｜ 复审：每季度。
> 配套流程文件：[aged-care-documentation-workflows.md](aged-care-documentation-workflows.md)（第 2–10 节流程编号对应下表"流程"列）。已下载模板的本地路径见 [paperwork-templates-index.md](paperwork-templates-index.md)，本表不重复其内容，只按"文档"维度汇总。
> 标记：【未核实】= 未在一手官方来源核实或依机构/州而异。

## 读表说明

- **保存年限**：联邦基线为 Aged Care Rules 2025 s 154 系列"自形成之日起 7 年"（https://www.legislation.gov.au/F2025L01173/latest/text ）；NSW / VIC / ACT 健康记录法另有"最后一次服务后 7 年"（见 [state-by-state-comparison.md](state-by-state-comparison.md) §6）。下表写"7 年 +州"表示两者取较长。
- **官方模板**："无"表示法规只规定内容、不提供统一表格，由机构系统（eCase、Leecare、AutumnCare 等）自带。
- **CareKind 起草**：✅ = 可从护理人员口述生成草稿，经 🛑HITL 审核签字后进入机构系统；⚠️ = 只能整理护士亲口陈述的部分 / 需 Clinical Lead 审定模板；❌ = 不起草（超出 documentation-only 边界、由他人完成或属于决策/提交行为）。
- 缩写：SQS = Strengthened Aged Care Quality Standards（https://www.health.gov.au/sites/default/files/2026-08/strengthened-aged-care-quality-standards_0.pdf ）；Rules = Aged Care Rules 2025；Act = Aged Care Act 2024（https://www.legislation.gov.au/C2024A00104/latest/text ）。

## 1. 入住与协议（流程 2）

| 文档 | 何时产生 | 谁填写 | 保存年限 | 法规 / 标准依据 | 官方模板链接 | CareKind 起草 |
|---|---|---|---|---|---|---|
| Service agreement | 入住前 | 机构行政 + 居民 / Supporter | 7 年 | Act / Rules（服务协议条款）；SQS 1.4 | 无统一模板；说明页 https://www.health.gov.au/our-work/residential-aged-care/managing/service-agreements | ❌ |
| Accommodation agreement | 入住前（新法下）【未核实宽限期】 | 机构行政 + 居民 | 7 年 | Act / Rules | 无；https://www.health.gov.au/our-work/residential-aged-care/managing/managing-accommodation-costs | ❌ |
| Entry record（新居民入住记录） | 入住时 | 机构行政 | 7 年 | Rules s 154-1200（申领记录） | 政府系统提交【未核实入口】 | ❌ |
| AN-ACC assessment | 入住后，独立评估员到访 | 独立 AN-ACC assessor | Department 保存；机构留存相关证据 7 年 | Act Ch 2；Rules classification 部分 | AN-ACC Reference Manual（本地）https://www.health.gov.au/sites/default/files/documents/2021/04/an-acc-reference-manual-and-an-acc-assessment-tool.pdf | ❌ |
| AN-ACC Assessor Pre-Entry Checklist | 评估员到访前约 5 天 | RN / 行政 | 7 年 | Department 指引 | https://www.health.gov.au/our-work/single-assessment-system/funding/before-providing-services | ❌ |
| 入住评估（各分项：跌倒、皮肤、营养、吞咽、疼痛、认知、行为、continence、口腔） | 入住时及评估期 | RN（部分由 EN / allied health） | 7 年 +州 | SQS 3.1.1、5.4.2 | 无统一模板（标准化量表多有版权，见索引说明） | ⚠️ 仅整理 RN 口述的观察；不计算评分 |
| 过敏 / 不良反应记录 | 服务开始时，新发时更新 | RN / GP | 7 年 +州 | SQS 5.3.3 | 无 | ⚠️ 仅护士口述的"居民 A 自述对 X 过敏"；须在用药系统确认 |
| 用药清单 / Medication chart（NRMC / eNRMC） | 入住、每次处方变更 | GP / NP 开具；RN / EN 给药签名 | 7 年 +州 | SQS 5.3.1(e)；州药品法【未核实】 | ACSQHC National Residential Medication Chart https://www.safetyandquality.gov.au/our-work/medication-safety/medication-charts 【URL 未核实】 | ❌ |
| Advance care directive / Statement of Choices / Advance health directive | 居民自愿完成；入住时收集副本，定期复审 | 居民（及证人 / 医生，依州） | 随记录保存 7 年 +州 | SQS 3.1.6、5.7.2；各州 ACD 法 | 各州表格见 [paperwork-templates-index.md](paperwork-templates-index.md) §9（NSW、VIC、QLD、SA、WA、TAS、ACT） | ❌ |
| SDM / Supporter / Enduring guardian 登记 | 入住时、变更时 | 机构行政 + RN | 7 年 | Act（supporters 制度）；州监护法 | 无（州监护文件为来源） | ❌ |
| 信息收集 / 共享同意、照片同意 | 入住时 | 居民 / SDM | 7 年 | SQS 2.7.2(c)；Privacy Act APP 3 | 无 | ❌ |
| AI 处理 / 录音同意（CareKind 场景） | 上线前 / 入住时 | 机构取得；管理员录入状态 | 按客户政策【需律师确认】 | Ahpra AI 指南；ACSQHC Scenario；[recording-consent.md](../recording-consent.md) | CareKind 告知模板（待做） | ❌（同意状态只读） |
| Care and services plan（初稿） | start day 前（部分 28 天内） | RN 主导，与居民 / Supporter partnership | 7 年 +州 | Rules s 148-80；SQS 3.1 | 无 | ⚠️ RN 口述内容放入草稿字段，RN 在机构系统定稿 |

## 2. 日常班次（流程 3）

| 文档 | 何时产生 | 谁填写 | 保存年限 | 法规 / 标准依据 | 官方模板链接 | CareKind 起草 |
|---|---|---|---|---|---|---|
| Progress notes | 每班 / 有变化时（频率依机构政策【未核实】） | PCW、EN、RN | 7 年 +州 | SQS 2.7、3.2；NMBA RN 1.6、EN Std 7 | 无 | ✅ 核心场景 |
| ADL chart（洗浴、穿衣、如厕、活动） | 每班 | PCW | 7 年 +州 | SQS 3.2；QI ADL 指标 | 无 | ✅ |
| Fluid / food intake chart | 按 care plan | PCW | 7 年 +州 | SQS 6.x、5.5 | 无 | ✅ 只记录数值，不判断"不足" |
| Bowel / continence chart | 按 care plan | PCW | 7 年 +州 | SQS 5.5.3 | 无 | ✅ |
| Repositioning / skin chart | 按 care plan | PCW / EN | 7 年 +州 | SQS 5.5；QI 压伤指标 | 无 | ✅ |
| Sleep chart | 按 care plan / 评估期 | PCW（夜班） | 7 年 +州 | SQS 3.2 | 无 | ✅ |
| 观察 / 生命体征记录 | 按 care plan、变化时 | RN / EN | 7 年 +州 | SQS 5.4.5 | 无 | ⚠️ 只录入护士口述数值，不标"异常" |
| PRN 用药效果、拒药记录 | 给药后 | RN / EN | 7 年 +州 | SQS 5.3.1(e) | 无 | ⚠️ 只进 progress note；给药签名在用药系统 |
| Handover sheet / 报告（ISBAR / ISOBAR） | 每次交接班 | 交班 RN / EN | 依机构政策【未核实是否属法定记录】 | SQS 3.3.2(d) | ACSQHC ISBAR poster（本地）https://www.safetyandquality.gov.au/sites/default/files/resources/attachments//ISBAR-Poster.pdf | ✅ 只用已签字记录；A / R 只用护士原话 |
| PCW 记录的 RN 复核 / 会签 | 班末 | RN | 7 年 | NMBA Decision-making framework | 无 | ❌（复核动作由 RN 完成；CK 提供队列） |

## 3. 事件与 SIRS（流程 4）

| 文档 | 何时产生 | 谁填写 | 保存年限 | 法规 / 标准依据 | 官方模板链接 | CareKind 起草 |
|---|---|---|---|---|---|---|
| Incident form（IMS） | 事件后尽快 | 发现人 + 值班 RN | 7 年 | Rules s 164-25（13 项字段）、s 154-150；SQS 2.5 | 无统一表格；ACQSC IMS 指南与 checklist（本地）https://www.agedcarequality.gov.au/sites/default/files/media/effective-incident-management-system-checklist.pdf | ✅ 事件快速通道 + 计时提醒 |
| Post-incident 观察记录（如跌倒后 neuro obs） | 事件后按机构频率 | RN / EN | 7 年 +州 | SQS 5.4.5；机构政策 | 无 | ⚠️ 只录入数值 |
| SIRS notification（Priority 1 / 2） | P1：24 小时内（5 天内补充）；P2：30 天内 | CM / SIRS 负责人 | 7 年 | Act s 16；Rules s 165A-25/30 | ACQSC SIRS 页面 https://www.agedcarequality.gov.au/providers/serious-incident-response-scheme ；quick guide https://www.agedcarequality.gov.au/sites/default/files/media/reportable-instances-sirs-guide.pdf | ❌（判定与提交均由机构人员） |
| SIRS final report | ACQSC 要求时，84 天内 | CM | 7 年 | Rules s 165A-45 | 同上 | ❌ |
| 报警记录 | 有合理理由时 24 小时内 | CM / RN | 7 年 | Rules s 164-40 | 无 | ❌ |
| GP / 家属通知记录 | 事件 / 变化后及时 | RN | 7 年 +州 | SQS 5.4.4(d) | 无 | ✅（"X 时已通知 Y"） |
| Open disclosure 记录 | 事件后尽快 | RN / CM | 7 年 | SQS 2.3.6 | ACQSC Open disclosure 资源 https://www.agedcarequality.gov.au/resources/open-disclosure | ⚠️ 只记录已发生的沟通，不写话术 |
| 调查 / RCA 报告、整改 | 事件后 | CM / 质量经理 | 7 年 | SQS 2.5.1、2.5.6 | ACQSC IMS best practice guidance（本地） | ❌ |

## 4. Care plan 复审与沟通（流程 5）

| 文档 | 何时产生 | 谁填写 | 保存年限 | 法规 / 标准依据 | 官方模板链接 | CareKind 起草 |
|---|---|---|---|---|---|---|
| Care and services plan（更新版） | 定期 + SQS 3.1.5 触发事件；居家至少每 12 个月 | RN + 居民 / Supporter | 7 年 +州 | SQS 3.1.4、3.1.5；Rules s 148-80 | 无 | ⚠️ RN 口述要点进草稿；不自动改写计划 |
| Case conference / 家属会议记录 | 复审时 | RN / CM | 7 年 | SQS 3.1.2、3.4.2 | 无 | ✅ |
| Care plan 副本提供记录 | 每次制定 / 更新后 | 行政 / RN | 7 年 | Rules s 148-80；SQS 3.1.4(d) | 无 | ❌ |
| Medication review 记录 | 入住、转院、每年、变化时 | GP / 药剂师 / RN | 7 年 +州 | SQS 5.3.2 | 无 | ❌ |
| Monthly care statement | 每月（目前自愿） | 机构 | 7 年【未核实】 | SQS 3.3.4(b)【与自愿安排关系未核实】 | Voluntary monthly care statements guide https://www.health.gov.au/sites/default/files/2026-05/voluntary-monthly-care-statements-guide.pdf | ⚠️ 未来可从已签字记录汇总草稿，需单独评估 |
| Monthly statement（Support at Home） | 每月 | 居家 provider | 7 年 | Rules s 155-40 | Support at Home Program Manual v4.4（本地） | ❌（财务/服务对账） |

## 5. 限制性措施（流程 6）

| 文档 | 何时产生 | 谁填写 | 保存年限 | 法规 / 标准依据 | 官方模板链接 | CareKind 起草 |
|---|---|---|---|---|---|---|
| Behaviour assessment / ABC chart | 行为出现时 | PCW / RN | 7 年 +州 | Rules s 162-15；NSW Health BPSD 手册 | NSW Health BPSD handbook（本地）https://www.health.nsw.gov.au/mentalhealth/resources/Publications/assessment-mgmt-people-bpsd-2022-summary-handbook.pdf | ✅ 只记录描述，不判断原因 |
| Behaviour support plan（BSP） | 考虑或使用 RP 时；定期复审 | RN（与 GP / 专科、居民 / RPSDM） | 7 年 | Rules s 162-45 ~ 162-75 | DSA BSP 模板（第三方版权，仅结构参考）https://www.dementia.com.au/hubfs/HCA-471_EDITABLE_DSA_Behaviour-Support-Plan.pdf ；ACQSC BSP fact sheet https://www.agedcarequality.gov.au/sites/default/files/media/fact-sheet-behaviour-support-plans.pdf | ⚠️ 只汇总已签字的使用记录；策略内容由 RN 撰写 |
| 知情同意记录（居民 / RPSDM，含拒绝） | 使用前；变更时须另行同意 | RN / GP（化学约束） | 7 年 | Rules s 162-15、s 6-20 | DoHDA RPSDM fact sheet（本地）https://www.health.gov.au/sites/default/files/2026-02/consent-for-restrictive-practices-information-for-aged-care-providers.pdf | ❌ |
| RPSDM 书面同意担任 | 使用联邦层级时 | 机构 + RPSDM | 7 年 | Rules s 6-20 | 同上 | ❌ |
| 化学约束评估与处方 | 使用前 | 医生 / NP | 7 年 +州 | Rules s 162-25 | 无 | ❌ |
| RP 使用记录 / 监测记录 | 每次使用 / 使用期间 | RN / EN | 7 年 | Rules s 162-30、162-60 | 无 | ✅ 字段对齐 s 162-60 |
| 紧急使用记录 + RPSDM 通知 | 紧急使用后尽快 | RN | 7 年 | Rules s 162-35 | 无 | ⚠️ 记录行动与通知，不判断合规 |

## 6. 恶化、转院、临终、离院（流程 7、9）

| 文档 | 何时产生 | 谁填写 | 保存年限 | 法规 / 标准依据 | 官方模板链接 | CareKind 起草 |
|---|---|---|---|---|---|---|
| 升级 / GP 联系记录（含医嘱） | 状况变化时 | RN | 7 年 +州 | SQS 3.3、5.4.4 | ACSQHC ISBAR（本地） | ✅ 只记录行动与沟通 |
| Hospital transfer 文件 | 转院时 | RN | 7 年 +州 | SQS 7.2.1(d)、5.3.1(b) | 各州 / ADHA transfer 资料【未核实】；ACSQHC C4S portal https://c4sportal.safetyandquality.gov.au/ | ⚠️ 只附已签字记录的近期变化摘要 |
| 医院 / 急诊使用记录 | 每次转院 | RN / 行政 | 7 年 | SQS 7.2.1(a)；QI 住院指标 | QI Manual Part A（本地） | ✅ |
| Discharge summary 接收与用药核对 | 返院时 | RN / GP | 7 年 +州 | SQS 7.2.1(e)、5.3.2(a) | 无 | ❌ |
| End-of-life / palliative care plan | 识别 palliative 需求时 | RN + GP + 居民 / SDM | 7 年 +州 | SQS 5.7 | 无 | ⚠️ 只整理护士陈述与居民原话 |
| 末期护理观察记录 | 末期每班 | RN / EN / PCW | 7 年 +州 | SQS 5.7.3 | 无 | ✅ |
| 死亡确认 / 死亡医学证明 | 死亡时 | RN（依州）/ 医生 | 依州法【未核实】 | 州法 | 州 BDM 表格【未核实】 | ❌ |
| Coroner 报告（如须） | 须报告死亡时 | 医生 / 机构 | 依州法 | 州 Coroners Act【未核实】 | — | ❌ |
| Departure 记录（死亡 / 永久离院） | 离院后 | 机构行政 | 7 年 | Rules s 154-1200【时限未核实】 | 政府系统【未核实】 | ❌ |

## 7. 质量与人力报告（流程 8）

| 文档 | 何时产生 | 谁填写 | 保存年限 | 法规 / 标准依据 | 官方模板链接 | CareKind 起草 |
|---|---|---|---|---|---|---|
| QI 数据采集记录与季度报告 | 季度内采集；季度后次月 21 日前提交 GPMS | RN / 质量经理 | 7 年 | Rules s 166（QI）、s 154-110 | QI Manual Part A（2026-10）https://www.health.gov.au/sites/default/files/2026-10/national-aged-care-quality-indicator-program-manual-part-a.pdf ；Part B 采集工具 https://www.health.gov.au/sites/default/files/2025-10/national-aged-care-quality-indicator-program-manual-part-b.pdf | ❌（未来或可汇总已签字记录供核对，需单独评估） |
| 24/7 RN 月报 | 每月结束后第 7 个日历日 23:59 前 | 机构 | 7 年 | Act s 175；Rules s 166-855 | 24/7 RN guide（本地）https://www.health.gov.au/sites/default/files/2026-03/247_registered_nurse_requirements_-_guides_for_registered_providers_of_residential_care_homes.pdf | ❌ |
| QFR（含 care minutes） | 每季度（法定截止日【未核实】） | 机构财务 | 7 年 | Act s 176；Rules s 166-340 | Care minutes guide（本地）https://www.health.gov.au/sites/default/files/2026-05/care-minutes-and-24-7-registered-nurse-requirements-guides-for-registered-providers-of-residential-care-homes.pdf | ❌ |

## 8. 投诉与反馈（流程 10）

| 文档 | 何时产生 | 谁填写 | 保存年限 | 法规 / 标准依据 | 官方模板链接 | CareKind 起草 |
|---|---|---|---|---|---|---|
| 投诉 / 反馈登记 | 收到时（含口头） | 接收员工 | 7 年 | SQS 2.6.1；Rules s 154-205 | ACQSC better practice guide（2025-07）https://www.agedcarequality.gov.au/sites/default/files/media/better_practice_guide_to_complaints_handling_in_aged_care_services_v4.pdf | ✅ 保留原话、标注来源 |
| 确认收到、调查与结果记录 | 3–5 天内确认（better practice）；及时解决 | CM | 7 年 | SQS 2.6.4 | 同上 | ❌ |
| 投诉数据分析报告 | 定期 | 质量经理 | 7 年 | SQS 2.6.5 | 无 | ❌ |

## 统计（按 CareKind 起草能力）

- ✅ 可直接起草（HITL 后入记录）：progress notes、ADL / 观察类 charts、handover 摘要、incident form、通知记录、case conference 记录、ABC chart、RP 使用记录、升级记录、医院使用记录、末期观察记录、投诉登记——约 18 项，覆盖一线护理人员**日常书写量的绝大部分**（推论，待访谈验证）。
- ⚠️ 只能整理护士原话 / 需 Clinical Lead 审定：入住评估、过敏、care plan、BSP、open disclosure 记录、transfer 附件、末期护理计划等。
- ❌ 不起草：协议与财务、AN-ACC、同意与 ACD、给药记录、SIRS 判定与提交、死亡证明、监管报告（QI / 24/7 RN / QFR）。
