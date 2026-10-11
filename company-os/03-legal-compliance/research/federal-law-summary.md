# 交付物 A：与养老护理文档相关的澳大利亚联邦法律（截至 2026-10-10）

> 内部研究资料，**不构成法律意见**。凡标注 ⚠️ 的内容为未经一手来源核实或正处于变动中，需律师确认。
> 一手条文核对基于：*Aged Care Act 2024* Compilation No. 2（2026-07-01 生效，C2026C00301）及 *Aged Care Rules 2025* Compilation No. 11（2026-09-20 生效，F2026C00970，Volume 1）。条文编号以 legislation.gov.au 当前版本为准。

---

## 0. 一页结论（对 CareKind AI 最重要的 10 点）

1. **新法已生效**：*Aged Care Act 2024* 与 *Aged Care Rules 2025* 自 **2025-11-01** 起施行，取代 *Aged Care Act 1997*。客户（registered providers）的文档义务主要写在 Rules 里，而非 Act 本身。
2. **记录保存 7 年**：Rules 第 154 条系列对几乎所有法定记录（服务交付、事故、投诉、QI、照护连续性、补贴申领、合规记录等）规定 **自记录形成/收到之日起保存 7 年**（书面或电子形式均可），并注明州/领地法律可能另有要求（见交付物 C：NSW/VIC/ACT 为"最后一次服务后 7 年"或"至 25 岁"）。
3. **信息管理是质量标准硬指标**：Strengthened Quality Standards **Outcome 2.7 Information management** 要求个人记录"准确且最新"(accurate and current)，并能被本人、支持者、护理人员等"访问和理解"。AI 起草的记录若含幻觉/错误，直接威胁客户合规。
4. **沟通与交接**：**Outcome 3.3 Communicating for safety and quality** 要求关键信息在工作人员之间有效传递、病情恶化及时上报 —— handover note 是核心场景。
5. **SIRS 时限**：Priority 1 → **24 小时内**通知 Commissioner；Priority 2 → **30 天内**；有重大新信息须"尽快合理可行地"补报；Commissioner 要求时须在 **84 天内**提交 final report（Rules s 165A-25/30/40/45）。事故记录最少 13 项字段（Rules s 164-25）。
6. **限制性措施 / 行为支持计划（BSP）**：Rules Part 9（s 162-xx）详细规定 BSP 必须记录的内容（替代策略、评估、知情同意、每次使用的开始时间/持续时间/频率/结果、监测与复审等），属于高风险高价值的文档场景。
7. **24/7 RN 报告**：Act s 175 要求每个 approved residential care home 每时每刻至少 1 名 RN 在岗；Rules s 166-855 要求**每月结束后 7 天内**报告，并逐条列出 RN 缺岗 ≥30 分钟的时段、原因与替代安排。Care minutes 仍为全行业平均 **215 分钟/人/天（含 44 分钟 RN）**。
8. **隐私**：Act s 168 自带个人信息保护条件（用途限制、披露限制、合理安全保障），叠加 *Privacy Act 1988*/APPs、NDB 计划。**APP 1.7–1.9 自动化决策透明度义务 2026-12-10 生效**。**Tranche 2 exposure draft（*Privacy Amendment (Personal Data Protection) Bill 2026*，2026-08-31 发布）** 提议 controller/processor 模式、72 小时 NDB 通报、"fair and reasonable" 检验等 —— 尚未成为法律 ⚠️。
9. **TGA**：仅转录/整理临床对话、**不做分析或解释**的数字 scribe **不是医疗器械**；一旦生成"医生/护士未明确说出的"诊断、鉴别诊断或治疗建议，即成为医疗器械，须列入 ARTG。TGA 已于 2026 年转入**执法阶段**（HIC2026，2026 年 8 月）。CareKind 必须严守"documentation-only"产品边界并管理功能蔓延（scope creep）。
10. **AHPRA**：从业者对 AI 生成记录的准确性负责；Ahpra 明确写道"AI transcription software should include an **explicit consent requirement as an initial step**" —— 应作为产品默认功能。

---

## 1. Aged Care Act 2024 与 Aged Care Rules 2025

| 项目 | 内容 | 链接 |
|---|---|---|
| Act | *Aged Care Act 2024*（No. 104, 2024；Title ID C2024A00104），最新汇编 C2026C00301（2026-07-01） | https://www.legislation.gov.au/C2024A00104/latest/text |
| Rules | *Aged Care Rules 2025*（F2025L01173），最新汇编 No. 11 F2026C00970（2026-09-20 生效，2026-10-06 登记）。⚠️ 更新频繁（11 次汇编/一年），引用前务必查 "Latest version" | https://www.legislation.gov.au/F2025L01173/latest/text |
| 生效 | 2025-11-01（Rules 于 2025-09-24 登记） | |
| 官方解读 | Department of Health, Disability and Ageing — *Guide to Aged Care Law* | https://www.health.gov.au/resources/publications/guide-to-aged-care-law |
| Rules 变更摘要 | *Aged Care Rules 2025 – summary of key changes* | https://www.health.gov.au/sites/default/files/2025-10/aged-care-rules-2025-summary-of-key-changes.docx |

### 1.1 记录保存义务（record-keeping）

- **Act s 154**（注册条件）：registered provider 必须 (a) 按 Rules 规定保存并保留规定类别的记录，且 (b) 以符合 s 168（个人信息保护）的方式保存。
- **Act s 155**：须向个人提供并解释规定的记录和信息；Outcome 2.7 注释交叉引用 s 155、s 156(3)（独立 advocate 可访问记录）。
- **Rules Chapter 4/5 Division "Record keeping"（s 154-1 起）** 主要子分部（均为 **7 年**）：

| Rules 条款 | 记录类别 | 保存期 |
|---|---|---|
| s 154-2 | 证明遵守 Chapter 3 义务和注册条件的记录 | 自形成之日起 7 年 |
| s 154-3 | 非 APP entity 的 provider 也须**如同组织一样遵守 APP 13（更正个人信息）** | — |
| s 154-10 ~ 154-25 | 员工/住户流感、COVID-19 疫苗记录（residential） | 7 年 |
| s 154-110 | Quality indicators 报告及采集/测量记录 | 7 年 |
| s 154-150 | 事故详情（s 164-25(1) 所列字段） | 7 年 |
| s 154-205 | 投诉与反馈记录 | 7 年 |
| s 154-300 起 | 财务与审慎报告；CHSP / NATSIFACP / MPSP / TCP 项目记录 | 7 年 |
| s 154-9xx | Worker screening：responsible persons 和 aged care workers 记录；不当行为指控副本 | 自最后更新起 7 年 |
| s 154-1000 | 服务交付与连续性记录（含月度对账单等） | 7 年 |
| s 154-1200 | 补贴申领记录（含服务交付记录、员工考勤） | 7 年 |
| s 154-1300 | 合规记录 | 7 年 |

- **前 provider**：停止注册后须将其曾需保存的记录继续保存 **7 年**，除非转移给其他组织（Act Chapter 7 Part 3；见 Guide to Aged Care Law "Keeping records"）。
- Rules 多处注释："A registered provider may be required to comply with other Commonwealth, State or Territory laws in relation to the retention of records." → 州法律可能更长（见交付物 C）。

**对 CareKind 的含义**：产品推送到客户系统的笔记即构成客户的法定记录；CareKind 自身保留的音频/草稿/审计日志是否构成"health record"需律师判断 ⚠️。建议：最终版本以客户系统为"source of truth"，CareKind 侧提供可配置保留期（默认短保留原始音频）+ 完整 audit trail（谁口述、AI 草稿版本、谁审阅/修改/批准、时间戳），以便客户 7 年期内举证。

### 1.2 Statement of Rights（Act s 23；s 24 效力）

取代原 *Charter of Aged Care Rights*。与文档产品最相关的条款：
- s 23(5)：个人隐私受尊重、个人信息受保护；
- s 23(6)：有权查询并获得关于其服务的记录和信息；
- s 23(7)–(8)：以本人理解的方式被告知；以**偏好语言或沟通方式**交流，可使用口译员 —— 多语言 dictation/翻译功能可支持此项，但须保证翻译不改变临床含义；
- s 23(1)：自主决策、在需要时获得支持（与 supported decision-making / supporters 制度相关）；
- s 24(2)：provider 须采取"合理且相称"的步骤以与这些权利相符的方式行事（以注册条件形式执行）。
- 官方海报：https://www.health.gov.au/sites/default/files/2025-09/aged-care-act-2024-statement-of-rights-a3-poster.pdf

### 1.3 Act s 168 个人信息保护（独立于 Privacy Act）

provider 必须确保：(a) 个人信息仅用于向该个人提供 funded aged care service 或其提供信息时的目的；(b) 除非本人同意，仅为上述目的、为合规或向其他 provider 提供服务时披露；(c) 采取合理的安全保障防止丢失或滥用。
→ **对 CareKind**：客户须能证明供应商处理符合 s 168；**不得将住户数据用于模型训练或其他二次用途**（除非取得明确同意且法律允许）。合同中需写明。

### 1.4 Strengthened Aged Care Quality Standards（7 项标准）

已纳入 *Aged Care Rules 2025*（Chapter 1 Part 4，s 15-xx）。官方 PDF：https://www.health.gov.au/sites/default/files/2025-08/strengthened-aged-care-quality-standards-august-2025.pdf ；ACQSC 指导材料：https://www.agedcarequality.gov.au/providers/quality-standards

| Standard | 与文档最相关的 Outcomes |
|---|---|
| 1 The individual | 1.1 Person-centred care；1.2 Dignity, respect and privacy；1.3 Choice, independence and quality of life；1.4 Transparency and agreements |
| 2 The organisation | 2.3 Accountability, quality system…；2.4 Risk management；**2.5 Incident management**；2.6 Feedback and complaints；**2.7 Information management**（记录"accurate and current"、可访问可理解、保密并符合知情同意）；2.9 Human resource management |
| 3 The care and services | **3.1 Assessment and planning**（care and services plans 描述当前需求、目标、偏好，含风险管理与预防策略，定期复审并被工作人员用以指导服务）；3.2 Delivery；**3.3 Communicating for safety and quality**（关键信息在工作人员间有效沟通；风险、病情变化与恶化须上报）；3.4 Planning and coordination |
| 4 The environment | 4.1 Environment；4.2 Infection prevention and control |
| 5 Clinical care | **5.1 Clinical governance**；5.2 Infections；5.3 Safe and quality use of medicines；**5.4 Comprehensive care**（临床评估、预防、计划、治疗、管理与复审；及早识别变化的临床需求）；5.5 Safety of clinical care services（高影响高发生率风险）；5.6 Cognitive impairment；5.7 Palliative care and end-of-life care |
| 6 Food and nutrition（residential） | 6.1–6.4（营养评估、饮食偏好、用餐体验）—— ADL/进食记录相关 |
| 7 The residential community | 7.1 Daily living；7.2 Transitions（转院/出院交接文档） |

另：Rules **s 148-80** 规定 care and services plan 须在 start day 前（部分情况 28 天内）制定；居家类服务每 12 个月至少复审一次；每次制定或更新后及应要求向本人提供副本。

### 1.5 事故管理与 SIRS

| 项目 | 规定 | 出处 |
|---|---|---|
| 8 类 reportable incidents | 不合理使用武力；非法性接触/不当性行为；心理或情感虐待；意外死亡；工作人员盗窃或经济胁迫；疏忽；违规使用 restrictive practice；服务中不明原因缺席 | Act s 16(1) |
| Priority 1 | 24 小时内通知 Commissioner（造成或需医疗/心理治疗的伤害、有合理理由报警、含性内容的特定事件、意外死亡、不明缺席等） | Rules s 165A-25 |
| Priority 2 | 30 天内通知 | Rules s 165A-30 |
| 重大新信息 | 尽快合理可行地补报 | Rules s 165A-40 |
| Final report | Commissioner 要求时，首次通知后 **84 天**内（或 Commissioner 指定期限） | Rules s 165A-45 |
| 报警 | 有合理理由时 24 小时内报警 | Rules s 164-40 |
| 事故记录最少字段 | 事故描述及伤害后果、是否 reportable、时间地点、发现时间、涉事人及证人姓名联系方式、评估、采取的行动、与受影响者的沟通、调查结果、记录人姓名、报警详情等（13 项） | Rules s 164-25(1) |
| 保存 | 7 年 | Rules s 154-150、s 164-25(2) |

- 自 2025-11-01 起 SIRS 覆盖 **Support at Home（居家）**；Priority 1 定义已更新（去掉"could reasonably have been expected to"措辞，并强调认知障碍者无法表达不等于未受伤害 —— Rules s 165A-25(3)）。ACQSC 指南：https://www.agedcarequality.gov.au/providers/serious-incident-response-scheme
- ⚠️ 部分二手资料仍写"60 天 final report"——已被 Rules 84 天取代，以 Rules 为准。

**产品含义**：incident note 模板应映射 s 164-25 字段；AI 可**提示**"该事件可能属于 reportable incident，请按机构流程判定"，但不得自动作出 SIRS 分级决定（避免成为决策工具，也避免 APP 1.7 自动化决策披露问题）；计时提醒（24h/30d）是高价值功能。

### 1.6 限制性措施（Restrictive practices）与行为支持计划（BSP）

- 定义：Act s 17；Rules s 17-5（chemical, environmental, mechanical, physical restraint, seclusion）。
- 仅适用于 residential care 注册类别（Rules s 162-5）。
- **使用前提**（s 162-15）：最后手段；先采用并**在 BSP 中记录**已考虑/使用的替代策略；相称、最少限制、最短时间；本人或 **restrictive practices substitute decision-maker** 的知情同意（含持续时间、频率、预期结果）；符合 BSP、Quality Standards、Code of Conduct、Statement of Rights 及州/领地法律。
- 非化学约束（s 162-20）：须由熟悉该人的 approved health practitioner 评估，评估及与他人/外部支持服务（如 dementia support specialists）的沟通须记入 BSP。
- 化学约束（s 162-25）：须由医生或 NP 评估、开具处方并取得知情同意；BSP 需记录 9 项内容（评估、决定、相关行为、必要性理由、provider 提供给处方者的信息、处方详情——药名/剂量/何时可用等）。
- 使用期间监测（s 162-30）：困扰/伤害迹象、副作用、情绪行为变化、福祉、独立功能、ADL 能力；**必要性须定期监测、复审并记录**。
- 紧急使用（s 162-35）：事后尽快通知 SDM 并在 BSP 记录行为、替代策略、理由、后续照护等。
- BSP 要求（s 162-45 ~ 162-75）：BSP 须纳入 care and services plan；使用后须记录开始时间、每次持续时间、频率、结果、是否符合知情同意、参与人员、监测与复审结果（s 162-60）；须复审修订并咨询本人/SDM。
- 违规使用 = reportable incident（Act s 16(1)(g)）。
- 州法律决定谁可作为 SDM（见交付物 C）；Department 决策树：https://www.health.gov.au/topics/aged-care/providing-aged-care-services/working-in-aged-care/restrictive-practices

**产品含义**：RP 事件记录模板（时间戳、持续时间、触发行为、替代策略、监测观察）+ 自动汇入 BSP "use log" 是明确的 compliance pain point；AI 不得建议使用约束或剂量。

### 1.7 AN-ACC（Australian National Aged Care Classification）

- 住宿式照护资金分类由**独立评估员**使用 AN-ACC assessment tool 评定（Act Chapter 2 classification；Rules Part 2 Division "Classification assessments"，如 s 76-xx）。Provider 可在住户情况发生重大变化时申请 reclassification；Department 页面：https://www.health.gov.au/our-work/AN-ACC
- 文档关联：日常 progress notes、ADL、跌倒、行为、皮肤完整性等记录是支持 reclassification 申请和 ACQSC 审核的证据基础。⚠️ 2026 年 reclassification 证据要求的具体官方指引未能在本次检索中核实，需以 Department 最新 "AN-ACC reclassification" 指南为准。
- **风险提醒**：产品不应以"提高 AN-ACC 资金"为营销点或生成夸大的记录（资金欺诈/虚假记录风险）。

### 1.8 Care minutes 与 24/7 RN

- Act s 175：每个 approved residential care home 须 24/7 至少 1 名 RN 在场在岗（可申请豁免）。
- Rules s 166-855：每月结束后 **7 天内**报告；逐日说明是否全时有 RN；如无，列出每段 ≥30 分钟的缺岗时段、原因和替代安排。
- Care minutes：Act s 176 + Rules s 176-15/176-20；全行业平均 **215 分钟/住户/天，其中 RN 44 分钟**（自 2024-10-01 起，至 2026-10 未发现新调整）；按季度为每个 home 设定目标；年度财务报告含 care minutes performance statement（Rules s 166-335）。来源：https://www.health.gov.au/our-work/AN-ACC/providers/care-minutes
- **产品含义**：文档时间节省可直接转化为"直接照护分钟"，是 ROI 叙事核心；但"文档时间"本身一般不计入 direct care minutes（以 Care minutes guide Section 4 为准 ⚠️）。

### 1.9 National Aged Care Mandatory Quality Indicator Program（QI Program）

- 适用 residential；**14 项 QI**：pressure injuries、restrictive practices、unplanned weight loss、falls and major injury、medication management、activities of daily living、incontinence care、hospitalisation、workforce、consumer experience、quality of life、enrolled nursing、allied health、lifestyle officers（后三项以 Manual 为准 ⚠️）。季度报送（季度后次月 21 日）。
- 记录须保存 7 年（Rules s 154-110）。
- 页面：https://www.health.gov.au/our-work/qi-program ；Manual 下载见交付物 B。
- **产品含义**：结构化抽取（跌倒、压疮、体重、约束）可辅助 QI 数据采集——属于"文档汇总"而非临床决策，但需要准确性验证。

### 1.10 Support at Home（居家照护，2025-11-01 起）

- 取代 Home Care Packages 与 STRC；CHSP 预计不早于 2027-07-01 并入。
- 文档要求：care and services plan（Rules s 148-80/148-85，居家类每 12 个月至少复审）、服务交付记录、月度对账单（Rules s 155-40 monthly statements）、care management 活动记录（*Support at Home Program Manual* Chapter 8；本地已下载 2026-09 版本 v4.4，见 `downloads/federal-aged-care/`；旧版 v4.3 2026-07 链接已 404）。
- 页面：https://www.health.gov.au/our-work/support-at-home
- **产品含义**：居家护理员移动端 dictation（离线、低带宽）是第二市场；服务记录与补贴申领关联，准确性直接影响 claims（Rules s 154-1200 申领记录保存 7 年）。

### 1.11 其他相关

- **Aged Care Code of Conduct**（Rules Part 3）：适用于 workers 和 responsible persons —— 包括尊重隐私、及时报告。
- **Worker screening**：Rules Subdivision P（s 154-900 起）。
- **Aged care digital platform operators**（Act 相关章节、Rules s 189-xx，须保存记录 ≥7 年）：指撮合个人与工作人员的平台；CareKind 作为文档工具**通常不属于**此类 ⚠️ 需律师确认。
- **My Health Record**：*My Health Records Rules 2026* 自 2026-04-01 取代 2016 Rule；ADHA 推动 aged care 接入（transfer summary 等）。未来集成机会，非当前义务 ⚠️。

---

## 2. Privacy Act 1988 / APPs / NDB / 改革

| 项目 | 要点 | 链接 |
|---|---|---|
| *Privacy Act 1988* + 13 APPs | 健康信息为 sensitive information（APP 3 收集需同意，除例外）；APP 6 用途/披露；APP 8 跨境披露（provider 对海外接收方承担责任）；APP 11 安全与销毁；APP 12/13 访问与更正。**提供 health service 且持有健康信息的组织不适用 small business exemption**。 | https://www.legislation.gov.au/C2004A03712/latest/text ；https://www.oaic.gov.au/privacy/australian-privacy-principles |
| CareKind 自身适用性 | CareKind 年营业额 <$3m 时，是否因"持有健康信息/提供 health service"或作为 contracted service provider 而受 Privacy Act 约束需律师确认 ⚠️；**商业上应按完全适用来设计**（客户合同也会要求）。 | |
| NDB 计划（Part IIIC） | 怀疑 eligible data breach 时须在 **30 天内**完成评估；确认后"尽快可行"通知 OAIC 和受影响个人。2025 年健康服务提供者是通报最多的行业（225 起，19%）。 | https://www.oaic.gov.au/privacy/notifiable-data-breaches |
| *Privacy and Other Legislation Amendment Act 2024*（Tranche 1） | 新增分级民事罚款与 OAIC 侵权通知权；**严重侵犯隐私的法定侵权（statutory tort）自 2025-06-10 起生效**；APP 11 明确包括"技术和组织措施"；**APP 1.7–1.9 自动化决策透明度：2026-12-10 生效**（隐私政策须披露使用个人信息、由计算机程序作出或实质性辅助作出"可合理预期显著影响个人权益"的决策）。 | https://www.legislation.gov.au/C2024A00128/asmade/text ；OAIC APP 1 指南 |
| Tranche 2 exposure draft | *Privacy Amendment (Personal Data Protection) Bill 2026*，AGD **2026-08-31** 发布；~41 项改革；提案包括：personal information "relates to"定义、**"fair, reasonable and lawful"** 统一检验替代 APP 3/4/6、收集敏感信息原则上需同意、**controller/processor 模式**、**72 小时**向 OAIC 通报 eligible data breach、加强 APP 11（数据清点、销毁/去标识化、定期评估）、技术不可能的访问例外。**未纳入**：取消 small business exemption、employee records exemption 改革、直接诉权、高风险活动强制 PIA。咨询于 2026-09-17/18 截止（来源说法不一 ⚠️）；据报拟年内提交议会。**尚非法律** ⚠️ | AGD 咨询页（https://www.ag.gov.au/rights-and-protections/privacy）；McCullough Robertson 2026-08-31 摘要；HSF Kramer 2026-09 摘要 |
| OAIC AI 指南（2024-10-21） | 两份：使用商用 AI 产品；开发者训练/微调生成式 AI。要点：Privacy Act 适用于 AI 的输入与输出；生成的推断/错误信息也是个人信息；不要将敏感信息输入公共生成式 AI；二次用于训练须满足 APP 6（通常需同意）；引入新 AI 系统前做 PIA。 | https://www.oaic.gov.au/privacy/privacy-guidance-for-organisations-and-government-agencies/guidance-on-privacy-and-the-use-of-commercially-available-ai-products |

**对 CareKind 的含义**：
- 作为 processor 设计（Tranche 2 一旦通过将正式化）：DPA、数据仅按客户指示处理、子处理方清单（LLM API 提供商！）、澳洲境内托管（APP 8 + 州法 HPP 9/14）。
- 若使用海外 LLM API（如美国区域），即构成跨境披露/使用问题 → 优先选择**澳洲区域部署**及零数据保留（zero data retention）条款。
- 72 小时 breach 通报（若通过）→ 现在就建立 incident response plan（OAIC 指南见交付物 B）。
- APP 1.7：CareKind 本身不作"决策"，但若产品提供风险标记（如 SIRS 提示、恶化提示），客户可能需在隐私政策中披露 —— 保持"人工审核 + 不自动执行"可降低风险。

---

## 3. TGA：AI / 数字 scribe 的监管立场

- TGA 页面 "Digital scribes"（最后更新 **2026-01-30**）：https://www.tga.gov.au/node/513526
  - **仅转录、翻译临床对话为书面记录、不进行分析或解释的数字 scribe 不是医疗器械**；
  - 若分析/解释对话，例如**生成从业者未明确陈述的诊断、鉴别诊断或治疗建议**，即为医疗器械，须先列入 ARTG；
  - 开发者须定期评估更新是否改变 intended purpose；若新增治疗用途，须停止供应直至获批，或移除该功能；
  - 非器械 scribe 仍受 Privacy Act、*Cyber Security Act 2024*、Ahpra 体系、Australian Consumer Law 约束。
- **2026 年最新动态**：TGA 产品质量部门负责人 Tracey Duffy 在 **HIC2026（2026-08-03/04，悉尼）** 表示数字 scribe 审查"已转入合规执法"，发现 scope creep、AI 影响临床决策、缺乏透明度与上市后监测等问题；"未来 12 个月"可能有执法行动；将"在未来几周"发布审查结果与更新的开发者指南（⚠️ 截至 2026-10-10 未核实是否已发布）。TGA 认为现行法律框架适用，不另立新法。来源：Medical Republic 报道 https://www.medicalrepublic.com.au/tga-flags-compliance-action-on-ai-scribes-as-review-finds-safety-concerns/127888
- 相关：TGA "How we regulate software-based medical devices"；clinical decision support software exemption（*Therapeutic Goods (Excluded Goods) Determination*，CDSS 豁免条件）。

**对 CareKind 的含义（高优先级）**：
1. 书面 **intended purpose statement**："将护理人员口述内容整理为其审阅的文档草稿，不提供诊断、治疗或护理建议"。
2. 提示词/输出护栏：禁止生成口述中未出现的临床判断（如"可能为 UTI"、"建议 PRN 用药"）；"缺失信息提示"仅限于模板字段完整性（如"未记录时间"），不涉及临床推断。
3. 营销材料与 UI 文案不得暗示临床决策支持。
4. 变更管理：每次新增功能做 TGA 定性复核并留档。
5. 若未来想做恶化识别/跌倒风险等，需走 SaMD 路径（分类、QMS、ARTG）。

---

## 4. Ahpra / NMBA：护士使用 AI 与文档标准

| 文件 | 要点 | 链接 |
|---|---|---|
| Ahpra & National Boards，*Meeting your professional obligations when using Artificial Intelligence in healthcare*（2024，适用所有注册职业含护士） | **Accountability**：从业者对使用 AI 的护理负责；须对 AI 输出施加人工判断；使用 AI scribe 时"practitioner is responsible for checking the accuracy and relevance of records"。**Understanding**：了解工具训练/测试人群、预期用途、限制、数据位置与是否用于再训练。**Transparency**：告知患者；录音型工具需更多说明。**Informed consent**：生成式 AI scribe 一般需知情同意，最好在记录中注明；录制私人对话**未经同意可能涉及刑事责任**；"AI transcription software should include an **explicit consent requirement as an initial step** before proceeding"。另：注意偏见、遵守州/领地法律和雇主治理。 | https://www.ahpra.gov.au/Resources/Artificial-Intelligence-in-healthcare.aspx |
| NMBA *Code of conduct for nurses*（2018-03-01 生效） | 包括保密与隐私、健康记录应准确、及时、清晰（Principle 3/4 相关条款）⚠️ 具体条款号需核对原文；2026 年未发现新版。 | https://www.nursingmidwiferyboard.gov.au/Codes-Guidelines-Statements/Professional-standards.aspx |
| *Registered nurse standards for practice*（2016）、*Enrolled nurse standards for practice* | RN Standard 6/7 等涉及计划、记录、评估与沟通 ⚠️ 核对 EN 标准是否已有新版 | 同上 |
| NMBA *Decision-making framework*（DMF） | 委派与监督（RN 委派给 EN/PCW 的护理及其文档） | 同上 |
| ACMHN *AI Scribes Position Statement*（非监管机构） | 临床判断不可外包；应保留非 AI 文档路径 | https://acmhn.org/ |

注意：aged care 一线大量为 **personal care workers（PCW/AIN），不受 Ahpra 注册监管**，但受 *Aged Care Code of Conduct* 约束；RN 审核/会签 PCW 文档的流程设计是产品机会。

---

## 5. ACSQHC（Australian Commission on Safety and Quality in Health Care）

| 文件 | 要点 | 链接 |
|---|---|---|
| *AI Clinical Use Guide*（v1.0，2025-08） | 使用前（评估证据、TGA 状态、隐私）、使用中（知情同意、审核输出、注意自动化偏差）、使用后（监测性能、报告问题） | https://www.safetyandquality.gov.au/sites/default/files/2025-08/ai-clinical-use-guide.pdf |
| *AI Safety Scenario – Ambient Scribe*（v1.0，2025-08） | Ambient scribe 用生成式 AI 摘要而非逐字转录；需取得同意、审核每份笔记、警惕遗漏/幻觉/错误归因；若 scribe 建议未向患者提及的诊断或治疗，可能触发 ARTG 要求；指出 scribe 软件普遍缺乏严谨安全与性能证据 | https://www.safetyandquality.gov.au/resources/ai-safety-scenario-ambient-scribe |
| *AI and safe patient care: Automation bias* 等其它 AI 资源 | — | https://www.safetyandquality.gov.au/our-work/digital-health/artificial-intelligence |
| *Communicating for Safety* 标准 / clinical handover（ISBAR） | 虽针对医院（NSQHS Standard 6），是 handover 结构的权威参考 | 见交付物 B |
| 州级：Safer Care Victoria *Ambient AI Scribes Advisory*（2025-05）；Vic DH *ambient AI scribes advisory*（2026-06） | 公共卫生服务采用 scribe 的治理要求 —— 销售给 Vic 公立 aged care 时相关 | https://www.safercare.vic.gov.au/ |

注：ACSQHC 的 NSQHS Standards 主要约束医院；aged care 由 ACQSC 监管。ACSQHC AI 指南对 aged care 非强制，但被 TGA、Ahpra 引用，属于事实上的行业基准。

---

## 6. 需要律师确认的问题清单（联邦层面）

1. CareKind 是否直接受 *Privacy Act* 约束（small business exemption 是否因处理健康信息而不适用）；Tranche 2 controller/processor 模式下的义务分配。
2. CareKind 保留的音频、AI 草稿、编辑历史是否属于客户的"records"（Rules s 154 系列）并需 7 年保存，抑或仅最终笔记需保存。
3. 产品"缺失信息提示"、"可能为 reportable incident 提示"、"恶化关键词标记"等功能是否会被 TGA 视为分析/解释（医疗器械边界）。
4. 使用境外 LLM 子处理方的 APP 8 合规、以及 Act s 168 对"披露"的影响。
5. APP 1.7（2026-12-10）对客户隐私政策的影响以及 CareKind 需提供的信息。
6. 合同中关于不当记录导致客户违反 Quality Standards / SIRS 时的责任与赔偿限制。
7. 是否属于"aged care digital platform operator"（预计否）。

---

## 7. 主要来源

见 `sources.md`。核心一手来源：
- Aged Care Act 2024：https://www.legislation.gov.au/C2024A00104/latest/text
- Aged Care Rules 2025：https://www.legislation.gov.au/F2025L01173/latest/text
- Guide to Aged Care Law：https://www.health.gov.au/resources/publications/guide-to-aged-care-law
- ACQSC：https://www.agedcarequality.gov.au/
- TGA Digital scribes：https://www.tga.gov.au/node/513526
- Ahpra AI：https://www.ahpra.gov.au/Resources/Artificial-Intelligence-in-healthcare.aspx
- OAIC：https://www.oaic.gov.au/
- ACSQHC AI：https://www.safetyandquality.gov.au/our-work/digital-health/artificial-intelligence
