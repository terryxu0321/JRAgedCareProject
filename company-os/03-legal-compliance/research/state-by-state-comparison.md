# 州/领地差异对比：Aged Care 与 CareKind AI（Deliverable C）

> 编写日期：2026-10-10 ｜ 性质：内部研究，**不构成法律意见** ｜ 标记说明：✅ 已通过官方/一手来源核实；⚠️ 未完全核实或 2026 年仍在变化，需律师确认。
>
> 背景：Aged care 的核心监管（Aged Care Act 2024、Aged Care Rules 2025、Strengthened Quality Standards、SIRS、24/7 RN、care minutes、restrictive practices 框架）是**联邦**层面的（见 `federal-law-summary.md`）。各州/领地的差异主要体现在：(1) 健康信息/隐私法（对私营 provider 及其承包商的双重适用）；(2) 监听/监控设备法（录音同意）；(3) 公立 aged care 的人员配比；(4) 监护、替代决策和 advance care directive（同意能力、restrictive practices 的 substitute decision-maker）；(5) 记录保存期限；(6) VAD；(7) 成人保护/虐待举报。

---

## 1. 健康记录 / 隐私法

| 州/领地 | 主要法律 | 是否适用于**私营** aged care provider | 是否适用于承包商 | 数据泄露通报 | 跨境/出州传输规定 |
|---|---|---|---|---|---|
| **NSW** | Health Records and Information Privacy Act 2002 (HRIP Act)，15 条 HPPs；公共部门另有 Privacy and Personal Information Protection Act 1998 (PPIP Act) | ✅ 是（HRIP 适用于私营 "organisations" 持有的 health information，与联邦 Privacy Act 并行） | 是（作为持有健康信息的 organisation 本身受约束） | PPIP Act 下的 MNDB 仅限公共部门（2023-11-28 起）；私营方走联邦 NDB | HPP 14 transborder data flows |
| **VIC** | Health Records Act 2001 (HRA)，11 条 HPPs；公共部门另有 Privacy and Data Protection Act 2014 (PDPA) + Victorian Protective Data Security Standards (VPDSS) | ✅ 是（适用于在 Victoria 收集/持有 health information 的私营 organisation） | 是；与州政府签约的 contracted service provider 另受合同条款约束 | 无州级私营方强制通报（走联邦 NDB）；公共部门向 OVIC 报告 incident | HPP 9 transborder data flows |
| **QLD** | Information Privacy Act 2009 (IPA)，经 Information Privacy and Other Legislation Amendment Act 2023 修订，**2025-07-01** 起统一为 QPPs + 强制数据泄露通报（MNDB） | ❌ 否（仅公共部门 agencies） | ✅ 被合同约束的 "bound contracted service provider" 需遵守 QPPs（⚠️ MNDB 对 CSP 的直接适用性需核实） | MNDB：agencies 2025-07-01；local government 2026-07-01 | QPP 相关条款 + IPA s33 境外传输 |
| **WA** | Privacy and Responsible Information Sharing Act 2024 (PRIS Act) | ❌ 否（仅公共部门） | ✅ 包括 contracted service providers | IPPs **2026-07-01** 生效；NDB 条款（Part 2 Div 6）**2027-01-01** 生效 | 有 |
| **SA** | 无隐私法规；公共部门适用 Cabinet 指令 "Information Privacy Principles (IPPS) Instruction"；Health Care Act 2008 保密条款 | ❌（私营方走联邦 Privacy Act） | 视政府合同 | 无法定 | — |
| **TAS** | Personal Information Protection Act 2004 (PIP Act)（公共部门） | ❌ | 是（政府合同方） | 无法定 | 有限 |
| **ACT** | Health Records (Privacy and Access) Act 1997 (HRPA Act)（公私均适用）；公共部门另有 Information Privacy Act 2014 | ✅ 是 | 是 | 私营走联邦 NDB | — |
| **NT** | Information Act 2002（公共部门 IPPs） | ❌ | 是（政府合同方） | 无法定 | IPP 9 |

**要点**：NSW、VIC、ACT 三地有**同时约束私营健康服务提供者**的州级健康记录法——在这三地运营的私营 aged care provider（以及作为其服务商处理健康信息的 CareKind AI）需同时满足联邦 APPs 与州 HPPs。联邦 Privacy Act 1988 s3 明确不排除可并行适用的州法。QLD、WA、TAS、NT、SA 的州隐私法主要约束公共部门及其承包商——当 CareKind AI 向**州立公立 aged care**（如 Vic PSRACS、Qld Health RACF、WA Country Health、SA/Tas/NT 的 MPS）销售时才直接相关。

---

## 2. 监听/监控设备法（录音同意）——对“口述录音”最关键

| 州/领地 | 法律 | 一方(参与者)可否录制私人对话 | 主要例外 |
|---|---|---|---|
| **NSW** | Surveillance Devices Act 2007 s7 | ❌ 原则上需**所有 principal parties** 同意 | 一方同意 + 为保护其 lawful interests 合理必要，或不为向非当事方传播 |
| **VIC** | Surveillance Devices Act 1999 s6 | ✅ 当事人可录（禁止的是非当事人录制） | s11 限制传播/发布录音内容；s9B–9C 禁止在 workplace toilets/washrooms 等处监控 |
| **QLD** | Invasion of Privacy Act 1971 s43 | ✅ 当事人可录 | s45 限制传播 |
| **WA** | Surveillance Devices Act 1998 s5 | ❌ 原则上需各 principal party 同意 | 公共利益/保护 lawful interests 等有限例外 |
| **SA** | Surveillance Devices Act 2016 s4 | ❌ 需各方同意 | 当事人为保护 lawful interests / 公共利益等例外 |
| **TAS** | Listening Devices Act 1991 s5 | ❌ 需各 principal party 同意 | 保护 lawful interests 等 |
| **ACT** | Listening Devices Act 1992 s4 | ❌ 需各方同意 | 类似 NSW 的 lawful interests 例外 |
| **NT** | Surveillance Devices Act 2007 s11 | ✅ 当事人可录 | 限制传播 |

⚠️ 二手资料在 NSW/VIC/SA/ACT 的“一方/全方”分类上互相矛盾；上表依据法条结构（是否覆盖“当事人本人的录制”）判断，**须律师逐州确认**。

**工作场所监控法**：
- **NSW Workplace Surveillance Act 2005**：对员工的 camera / computer / tracking surveillance 需提前 **14 天书面通知**；covert surveillance 需 Magistrate authority。若 CareKind AI 的使用日志、口述时间戳、位置信息被雇主用于监控员工，可能构成 "computer surveillance"。
- **ACT Workplace Privacy Act 2011**：optical / data / tracking surveillance 需通知与协商（14 天）。
- **VIC**：无专门 workplace surveillance 法；议会 Economy and Infrastructure Committee 2025-05-13 报告建议立法（18 条建议），政府 2025-11 回应表示支持。⚠️ 截至 2026-10 未确认已有法案——**需持续跟踪**。
- 其他州：无专门法，适用一般监控设备法。

---

## 3. 州级人员配置/RN 法律（主要影响公立/特定设施）

| 州 | 法律 | 内容 | 适用范围 | 状态 |
|---|---|---|---|---|
| **NSW** | Public Health Act 2010 s104 + Public Health (Nursing Homes) Regulation | "nursing home" 须**随时有 RN 在岗**；因联邦取消 high/low care 区分，regulation 对 2014-07-01 前分类为 nursing home 的设施 "grandfather" 保留 | 私营+公立 nursing homes（历史定义） | ⚠️ 2020/2022 私人议员法案（扩展到所有 RACF）**未通过**（2022-11-10 二读否决）。Aged Care Act 2024 后定义如何衔接未核实；实务上联邦 24/7 RN 要求已覆盖所有 RACF |
| **VIC** | Safe Patient Care (Nurse to Patient and Midwife to Patient Ratios) Act 2015（2019/2020 修订） | 公立 residential aged care：早班 **1:7**、晚班 **1:8**、夜班 **1:15**（另有 in-charge） | 仅 **public sector residential aged care services (PSRACS)** | ✅ 生效；⚠️ Safe Patient Care Amendment Bill 2025 状态待核 |
| **QLD** | Hospital and Health Boards Act 2011 + Regulation（经 Health Transparency Act 2019 修订） | Queensland Health RACF：平均 daily resident care hours ≥ **3.65**，RN ≥ **30%**、support workers ≤ 50% | 公立 RACF（自 2020-02-21） | ✅；私营 RACF 被要求报告人员/护理时数并在 performance.health.qld.gov.au 公开，**不报告者被点名**（非强制） |
| 其他州 | 无州级 aged care 配比法 | — | — | 依联邦 care minutes + 24/7 RN |

**州立公立 aged care 概况**：Victoria 是全国最大的公立 aged care 运营者——截至 2025-10-31 约 **156 个 PSRACS、68 家 provider、5,400+ 床位**，90% 以上在乡村地区（✅ Vic DH 向 IHACPA 的 submission）。QLD Health 运营约十余家 RACF（⚠️ 数量未核实）。NSW、WA、SA、TAS、NT 主要通过 **Multi-Purpose Services (MPS)**（联邦/州合作的乡村医院+aged care）提供公立服务。→ 公立客户意味着州隐私法、州公共档案法、州 ICT/安全标准（如 VPDSS）直接适用。

---

## 4. 监护、替代决策与 Advance Care Directive

| 州/领地 | 监护/行政法 | Advance care directive | 医疗“默认”决策者 | 审裁机构 |
|---|---|---|---|---|
| NSW | Guardianship Act 1987（Part 5 medical/dental treatment） | 普通法（common law）承认 ACD，无专门法规 | "person responsible" | NCAT |
| VIC | Guardianship and Administration Act 2019 | Medical Treatment Planning and Decisions Act 2016（instructional/values directive） | "medical treatment decision maker" | VCAT |
| QLD | Guardianship and Administration Act 2000；Powers of Attorney Act 1998 | Advance Health Directive (Powers of Attorney Act 1998) | "statutory health attorney" | QCAT |
| WA | Guardianship and Administration Act 1990（Part 9B AHD） | Advance Health Directive | 法定层级 (s110ZD) | SAT |
| SA | Guardianship and Administration Act 1993；Consent to Medical Treatment and Palliative Care Act 1995 | Advance Care Directives Act 2013 | "person responsible" | SACAT |
| TAS | Guardianship and Administration Act 1995（经 2023 修正法，**2024-09-01** 生效，强调 supported decision-making、will & preferences） | Advance Care Directive（G&A Act Part 5A，经 Advance Care Directives Act 2021 引入） | "person responsible" | TASCAT |
| ACT | Guardianship and Management of Property Act 1991；Powers of Attorney Act 2006 | Medical Treatment (Health Directions) Act 2006 | "health attorney" | ACAT |
| NT | Guardianship of Adults Act 2016 | Advance Personal Planning Act 2013 | 法定决策者 | NTCAT |

**与 aged care 的交汇**：联邦 Aged Care Act 2024 引入 **registered supporters**（支持性，不是替代决策）。**Restrictive practices 的同意**：须按服务所在州/领地法律确定 restrictive practices substitute decision-maker (RPSDM)；只有当州法没有途径、或审裁机构严重延误时，才可使用 **Aged Care Rules 2025 的联邦层级（hierarchy）**作为后备（✅ health.gov.au 2026-02 decision tree）。QCAT 2026 年已发布首个 Aged Care Act 2024 下的决定及 practice direction（⚠️ 二手来源）。→ 产品文档中需记录“谁给了同意、依据哪州法律/哪一层级”。

---

## 5. 成人保护 / 虐待举报 / 工作人员筛查

| 州/领地 | 法律/机构 | 是否有强制举报 |
|---|---|---|
| NSW | Ageing and Disability Commissioner Act 2019（Ageing and Disability Commission，主要针对 home/community 中的老人与残障成人） | 无一般强制举报（RACF 内走联邦 SIRS） |
| SA | Ageing and Adult Safeguarding Act 1995（Adult Safeguarding Unit） | 无一般强制举报，可自愿报告 |
| ACT | Crimes Act 1900 abuse of vulnerable people 罪名（含 failure to protect，2020 修订） | ⚠️ 对有权责者有保护义务，需核实具体适用 |
| NT | Domestic and Family Violence Act 2007 s124A | ⚠️ **所有成年人**须举报严重家暴（含家庭成员对老人）——需核实对 aged care 的适用 |
| 其他（VIC、QLD、WA、TAS） | 公共监护人/Public Advocate 等可接受举报 | 无一般强制举报 |

**工作人员筛查**：联邦 Aged Care Rules 2025 规定 aged care workers 需 police certificate 或 NDIS worker screening clearance；NDIS 筛查由各州 worker screening unit 执行。州之间的差异主要在 NDIS 筛查程序，对 CareKind AI（非直接护理员工）影响有限；但若公司员工可访问居民健康信息，建议参照 provider 要求完成 police check。

---

## 6. 记录保存期限（health records）

| 州/领地 | 私营健康服务提供者 | 公共部门 |
|---|---|---|
| NSW | HRIP Act s25：成人自最后一次服务起 **7 年**；未成年人至 **25 岁**；删除须保留删除记录 | State Records Act 1998 + NSW Health 的 General Retention and Disposal Authority（如 GDA17） |
| VIC | HRA HPP 4.2：成人最后服务后 **7 年**；儿童时收集的至 25 岁（取较晚者）；HPP 4.3 删除须记录 | Public Records Act 1973 + PROV 处置标准 |
| ACT | HRPA Act：成人自最后一次记录起 **7 年**；未成年人至 25 岁；不得更改/销毁记录（可附更正） | Territory Records Act 2002 |
| QLD / WA / SA / TAS / NT | 无私营方州级法定期限（依联邦 Aged Care Rules 记录保存要求 + 合同/专业指南，通常 ≥7 年） | 各州 Public/State Records Acts（Qld Public Records Act 2023 ⚠️ 生效日待核；WA State Records Act 2000；SA State Records Act 1997；Tas Archives Act 1983；NT Information Act 2002 Part 9） |

→ 产品默认保存策略应以**最长适用期限**设计（并支持 provider 自定义 + legal hold），且草稿/录音/转写是否构成“health record”需律师确认（见第 9 节）。

---

## 7. Voluntary Assisted Dying (VAD)

| 州/领地 | 法律 | 生效 | 对 RACF 的义务 | 禁止主动提起 |
|---|---|---|---|---|
| VIC | Voluntary Assisted Dying Act 2017 | 2019-06 | 无专门机构义务条款 | ✅ registered health practitioners 不得主动提起 (s8) |
| WA | Voluntary Assisted Dying Act 2019 | 2021-07 | 有限 | 医生/护士可提起但须同时告知其他选项 |
| TAS | End-of-Life Choices (Voluntary Assisted Dying) Act 2021 | 2022-10 | 有限 | 限制 |
| SA | Voluntary Assisted Dying Act 2021 | 2023-01 | 不参与的设施须安排转移 | ✅ 不得主动提起 |
| QLD | Voluntary Assisted Dying Act 2021 | 2023-01 | ✅ entity obligations：信息获取、医生到访、转移（区分 permanent/non-permanent resident） | 可提起（须同时告知治疗/姑息选项） |
| NSW | Voluntary Assisted Dying Act 2022 | 2023-11-28 | ✅ 不参与设施须允许合理获取信息、协助转移；须公开披露不提供 VAD | 可提起（附条件） |
| ACT | Voluntary Assisted Dying Act 2024 | **2025-11-03**（⚠️ 一说 scheme 11-08） | ✅ 须允许合理获取、促成转移、发布合规 policy；未通知 Oversight Board 等为 strict liability（20 penalty units） | 允许 |
| NT | Rights of the Terminally Ill Bill 2026 | ⚠️ 2026-08/09 **已通过**（二手来源），预计 **2028 年初**才可使用 | 待定 | clause 16 禁止 health worker 主动提起 |

→ 对 CareKind AI：AI 草稿**不得**生成主动提及 VAD 的内容（在 VIC/SA/NT 尤其敏感——若护理员是 registered health practitioner，AI 建议性文本可能被视为“提起”）；居民主动提及时应如实记录。VAD 正式表格由医生/VAD 系统完成，不在本产品范围。

---

## 8. 其他

- **Retirement Villages Acts**（各州均有，如 NSW Retirement Villages Act 1999、Vic Retirement Villages Act 1986、Qld Retirement Villages Act 1999 等）：规范 village operator 与居民合同，不规范护理文书。仅当 Support at Home 服务在 village 内交付时间接相关。**影响低**。
- **州数字健康要求**：私营 aged care 无州级强制数字健康标准；但向**州公立服务**销售时须满足州 ICT/信息安全要求，如 **Victoria VPDSS**（PDPA Part 4，适用于 PSRACS 及其承包商）、NSW Cyber Security Policy、QLD Information Security Policy (IS18)，以及 NSW Health/Queensland Health 的数据驻留（onshore hosting）和第三方 ICT 采购要求（⚠️ 具体政策条款未逐一核实）。My Health Record 为联邦体系。

---

## 9. 分州摘要

### NSW
HRIP Act 2002 适用于私营 provider 及处理健康信息的服务商（HPP 1–15，s25 保存 7 年/25 岁，HPP 14 出境）；Surveillance Devices Act 2007 原则上要求**所有当事人同意**录音；Workplace Surveillance Act 2005（14 天通知）；Public Health Act 2010 s104 历史 RN 要求（⚠️ 现行定义待核）；Guardianship Act 1987 "person responsible"，ACD 依普通法；Ageing and Disability Commissioner；VAD 2022 有 RACF 义务。**对口述录音风险最高的州之一。**

### VIC
HRA 2001 适用于私营方（HPP 4.2 保存期、HPP 9 出境）；Surveillance Devices Act 1999 当事人可录，但限制传播；工作场所监控立法**正在推进**（2025 委员会报告 + 政府支持）；Safe Patient Care Act 对 PSRACS 规定 1:7/1:8/1:15；全国最大公立 aged care 体系（~156 家）→ 采购需满足 VPDSS；Medical Treatment Planning and Decisions Act 2016；VAD 禁止 health practitioner 主动提起。

### QLD
IPA 2009（2025-07-01 起 QPPs + MNDB）仅约束 agencies 与 bound contracted service providers；Invasion of Privacy Act 1971 当事人可录；Queensland Health RACF 法定 3.65 小时 + 30% RN；Health Transparency Act 2019 公开私营 RACF 人员数据；Powers of Attorney Act 1998 / AHD / statutory health attorney；QCAT 2026 RPSDM 指引；VAD entity obligations。

### WA
PRIS Act 2024：IPPs 2026-07-01 生效（公共部门+承包商），NDB 2027-01-01；Surveillance Devices Act 1998 需各方同意；Guardianship and Administration Act 1990（AHD + 决策层级）；VAD 2019。

### SA
无私营隐私州法；Surveillance Devices Act 2016 需各方同意（有 lawful interests 例外）；Advance Care Directives Act 2013 + Consent to Medical Treatment and Palliative Care Act 1995；Ageing and Adult Safeguarding Act 1995（Adult Safeguarding Unit）；VAD 2021（不得主动提起，不参与设施须安排转移）。

### TAS
PIP Act 2004（公共部门）；Listening Devices Act 1991 需各方同意；Guardianship and Administration Act 1995 于 2024-09-01 重大修订（supported decision-making，第三阶段改革待定）；ACD 纳入 G&A Act；End-of-Life Choices (VAD) Act 2021。

### ACT
HRPA Act 1997 适用于公私（7 年/25 岁，不得销毁/更改）；Listening Devices Act 1992 需各方同意；Workplace Privacy Act 2011；Medical Treatment (Health Directions) Act 2006；VAD Act 2024 自 2025-11 生效，RACF 有可处罚义务；Crimes Act 弱势人士虐待罪。

### NT
Information Act 2002（公共部门）；Surveillance Devices Act 2007 当事人可录；Advance Personal Planning Act 2013；Guardianship of Adults Act 2016；DFV Act 普遍强制举报严重家暴（⚠️）；VAD 2026 通过、约 2028 实施（⚠️）。

---

## 10. 对 CareKind AI 的启示（Implications）

1. **口述录音与环境对话**：产品设计应为“**护理员在离开居民后对设备口述**”（nurse-only dictation），而非在房间内的 ambient scribe。若录到居民/家属/其他员工的私人对话：在 NSW、WA、SA、TAS、ACT 原则上需**所有当事人同意**，否则可能构成刑事犯罪（且 CareKind 作为提供设备/软件方可能涉及 "cause to be used"）；VIC、QLD、NT 当事人可录但限制传播（CareKind 服务器接收、AI 处理是否属“传播”需律师确认）。建议：默认 push-to-talk、不做常开监听、UI 提示“请勿在居民对话中录音”、ambient 模式（如未来提供）需记录每次同意并按州配置；录音转写后尽快删除原始音频。
2. **州健康记录法**：在 NSW / VIC / ACT，CareKind 作为处理健康信息的 organisation **直接受** HRIP Act / HRA / HRPA Act 约束（不仅是 provider 的承包商）——需要遵守收集、使用、披露、数据质量、安全、访问更正、出境（HPP 9 / HPP 14）等原则；合同中明确角色与责任。
3. **公立客户**：向 Vic PSRACS、Qld Health、WA/SA/Tas/NT 公立/MPS 销售时，还会触发州公共部门隐私法（QLD IPA、WA PRIS Act 2026、Tas PIP、NT Information Act）作为 **contracted service provider** 的直接义务、州公共档案法、以及 VPDSS 等安全标准与数据驻留要求。
4. **数据位置**：建议全部数据（音频、转写、草稿、日志）托管在**澳洲境内**，并确保 LLM 推理供应商在澳洲区域处理或满足 APP 8 / HPP 9 / HPP 14 / QLD IPA s33 的条件——这是 VIC/NSW 法定出境限制与公立采购的现实门槛。
5. **记录保存**：AI 草稿 → 审核后正式记录推送至 provider 系统；CareKind 自身保留的音频/草稿/审计日志是否属 "health record" 及需按 7 年/25 岁保存，还是“用后即删”，**需律师确认**；默认可配置、支持 legal hold，删除需留删除记录（NSW s25 / Vic HPP 4.3）。
6. **同意与替代决策**：文档模板需支持记录 consent 来源（居民本人 / registered supporter / 按州法律的 substitute decision-maker / Rules 层级），尤其 restrictive practices 文档。
7. **工作场所监控**：在 NSW/ACT，若 provider 用 CareKind 的使用数据监控员工，需 14 天通知；产品分析/审计日志功能应提示 provider 其义务。关注 Victoria 2026 年可能的 workplace surveillance 立法。
8. **VAD 与敏感内容**：AI 不得在草稿中主动建议 VAD；记录居民主动表达的意愿须忠实、不扩写。
9. **人员配比数据**：Vic/Qld 公立设施有州配比报告义务，可成为未来增值功能（班次/护理时数记录），但非 MVP 必需。

---

## 来源（Sources）

- NSW HRIP Act 2002：https://legislation.nsw.gov.au/view/html/inforce/current/act-2002-071
- NSW PPIP Act 1998：https://legislation.nsw.gov.au/view/html/inforce/current/act-1998-133
- NSW Surveillance Devices Act 2007：https://legislation.nsw.gov.au/view/html/inforce/current/act-2007-064
- NSW Workplace Surveillance Act 2005：https://legislation.nsw.gov.au/view/html/inforce/current/act-2005-047
- NSW Public Health Act 2010：https://legislation.nsw.gov.au/view/html/inforce/current/act-2010-127 （网站 Cloudflare 阻挡，未能直接读取 s104 现行文本 ⚠️）
- NSW LC Report 32 Registered nurses in NSW nursing homes：https://www.parliament.nsw.gov.au/lcdocs/inquiries/2275/Report%2032%20-%20Registered%20nurses%20in%20New%20South%20Wales%20n.pdf
- Public Health Amendment (Registered Nurses in Nursing Homes) Bill 2020：https://www.parliament.nsw.gov.au/bills/Pages/bill-details.aspx?pk=3779
- NSW Guardianship Act 1987：https://legislation.nsw.gov.au/view/html/inforce/current/act-1987-257
- NSW Ageing and Disability Commissioner Act 2019：https://legislation.nsw.gov.au/view/html/inforce/current/act-2019-007
- NSW VAD Act 2022：https://legislation.nsw.gov.au/view/html/inforce/current/act-2022-017
- Vic Health Records Act 2001：https://www.legislation.vic.gov.au/in-force/acts/health-records-act-2001
- Vic HCC health records guidance：https://hcc.vic.gov.au/providers/health-records-providers
- Vic Surveillance Devices Act 1999：https://www.legislation.vic.gov.au/in-force/acts/surveillance-devices-act-1999
- Vic Safe Patient Care Act 2015：https://www.legislation.vic.gov.au/in-force/acts/safe-patient-care-nurse-patient-and-midwife-patient-ratios-act-2015
- Vic workplace surveillance inquiry：https://www.parliament.vic.gov.au/get-involved/inquiries/inquiryintoworkplacesurveillance/reports ；政府回应 https://www.vic.gov.au/workplace-surveillance
- Vic DH submission (PSRACS 数量)：https://consultations.health.gov.au/aged-care-division/residential-aged-care-accommodation/supporting_documents/dept-of-health-vic-accompricingreview-submission-11nov25pdf
- VAGO State-managed aged care：https://www.audit.vic.gov.au/report/state-managed-aged-care
- Vic Medical Treatment Planning and Decisions Act 2016：https://www.legislation.vic.gov.au/in-force/acts/medical-treatment-planning-and-decisions-act-2016
- Vic Guardianship and Administration Act 2019：https://www.legislation.vic.gov.au/in-force/acts/guardianship-and-administration-act-2019
- Qld Information Privacy Act 2009：https://www.legislation.qld.gov.au/view/html/inforce/current/act-2009-014
- Qld CSP QPP fact sheet：https://www.families.qld.gov.au/_media/documents/about-us/right-to-information/information-privacy/contracted-service-providers-qpps.pdf
- Qld Invasion of Privacy Act 1971：https://www.legislation.qld.gov.au/view/html/inforce/current/act-1971-050
- Qld nurse-to-patient ratios (incl. RACF)：https://www.health.qld.gov.au/ocnmo/nursing/nurse-to-patient-ratios
- Qld aged care performance reporting：https://performance.health.qld.gov.au/statewide-performance/prevention-early-intervention-and-primary-health-care/aged-care
- Qld VAD entity obligations：https://www.health.qld.gov.au/__data/assets/pdf_file/0027/1196334/entity-obligations-quick-reference-guide.pdf
- WA OIC PRIS commencement：https://www.wa.gov.au/organisation/office-of-the-information-commissioner/understanding-my-privacy-rights-when-do-they-commence
- WA Surveillance Devices Act 1998：https://www.legislation.wa.gov.au/legislation/statutes.nsf/law_a810.html
- SA Surveillance Devices Act 2016：https://www.legislation.sa.gov.au/lz?path=/c/a/surveillance%20devices%20act%202016
- SA Ageing and Adult Safeguarding Act 1995：https://www.legislation.sa.gov.au/lz?path=/c/a/ageing%20and%20adult%20safeguarding%20act%201995
- SA Advance Care Directives Act 2013：https://www.legislation.sa.gov.au/lz?path=/c/a/advance%20care%20directives%20act%202013
- Tas Guardianship and Administration Amendment Act 2023 proclamation：https://www.legislation.tas.gov.au/view/whole/html/asmade/sr-2024-038 ；https://www.justice.tas.gov.au/about-us/news/articles/tasmanias-guardianship-and-administration-system-is-changing
- Tas Listening Devices Act 1991：https://www.legislation.tas.gov.au/view/html/inforce/current/act-1991-021
- ACT HRPA Act 1997：https://www.legislation.act.gov.au/a/1997-125/ ；ACT record-keeper guidance https://www.act.gov.au/__data/assets/pdf_file/0009/2219733/Health-Records-Privacy-and-Access-Act-1997-Information-for-record-keepers-February-2012.pdf
- ACT Listening Devices Act 1992：https://www.legislation.act.gov.au/a/1992-57/
- ACT Workplace Privacy Act 2011：https://www.legislation.act.gov.au/a/2011-4/
- ACT VAD：https://www.act.gov.au/health/end-of-life-and-palliative-care/voluntary-assisted-dying-in-the-act
- NT Surveillance Devices Act 2007 / Information Act 2002 / Advance Personal Planning Act 2013：https://legislation.nt.gov.au/
- NT VAD (Rights of the Terminally Ill Bill 2026) 二手：https://insightplus.mja.com.au/2026/35/the-northern-territory-has-just-voted-to-legalise-voluntary-assisted-dying-heres-how-it-will-work
- 联邦 restrictive practices / RPSDM decision tree：https://www.health.gov.au/topics/aged-care/providing-aged-care-services/working-in-aged-care/restrictive-practices-in-aged-care-a-last-resort ；https://www.health.gov.au/sites/default/files/2026-02/restrictive-practices-substitute-decision-maker-decision-tree_0.pdf
- 联邦 24/7 RN：https://www.health.gov.au/our-work/care-minutes-registered-nurses-aged-care/24-7-rns
- ELDAC VAD in RACFs (SA/QLD/NSW)：https://www.eldac.com.au/Portals/12/Documents/Factsheet/Legal/VAD-aged-care-RACFs-SA-QLD-NSW.pdf

> 注：部分 legislation 站点（NSW、AustLII）在研究时被 Cloudflare/403 阻挡；监控设备法的“当事人可否录音”分类主要基于法条结构与既有认知，二手来源互相矛盾，**须律师逐州复核**。
