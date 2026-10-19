# 州/领地深度核查：QLD · WA · SA · TAS · NT（Aged Care 文档相关）

> **内部工作底稿，非法律意见。** 核查日期：2026-10-19 ｜ 编写：法规研究（AI 辅助）｜ Owner：Terry ｜ 复审：每季度或法规变动时
>
> 定位：补充、核实、纠错 [`state-by-state-comparison.md`](state-by-state-comparison.md)（下称 STATE）中五个辖区的内容；不重复 STATE 与 [`federal-law-summary.md`](federal-law-summary.md)（下称 FED）已有结论。
>
> 标记：✅ = 已读到官方法条/官方页面原文；🔎 = 官方页面经搜索结果摘要核实（直接抓取被 403 阻挡）或仅有官方二级资料（法律援助手册、解释性备忘录）；⚖️ = 律所等二手来源；【未核实】= 未能找到官方来源，不得作为结论使用。罚则金额以法条所载 penalty units 为准，penalty unit 的现行金额未核实。
>
> 产品背景（见 [`docs/PRD.md`](../../../docs/PRD.md) B4）：MVP 为**模式 A 按键口述**（护理人员对设备口述，建议离开居民房间后口述）；环境录音（模式 C）不进入 MVP，需 DR-006。

---

## 0. 本次核查的核心结论（摘要）

1. **"私人对话"要件是录音法的前提**：五辖区的 listening device 罪名都以 "private conversation"（一人对另一人说话、且有不被他人听到的期望）为要件。护理人员**独自**对设备口述，一般不构成"对话"——这是模式 A 在全方同意州（WA/SA/TAS）可行的法律基础；但一旦录入居民/家属/同事的话语，就进入各州规则。（法条依据见各辖区 §2；该解释本身需律师确认。）
2. **QLD 与 NT 是"当事人可录"，但"录完之后的传播"受限**：QLD s45、NT s15 限制把录音或其报告"communicate/publish"给他人；上传给 CareKind 做转写、生成记录供其他员工阅读是否落入例外（lawful interests / 履行职责 / 有合理利益的人），**需律师意见**。
3. **TAS 有一个 STATE 未列出的例外**：Listening Devices Act 1991 s5(3)(b)(ii)——一名 principal party 同意、且录音"不是为了向非当事人传播"即可录。但护理记录本身要给其他员工看，**该例外大概率不适用于 CareKind 场景**。
4. **TAS 与 NT 公共部门隐私法的"出境"是出州/出领地**：TAS PIPP 9 是 "outside Tasmania"，NT IPP 9 是 "outside the Territory"。若向 TAS/NT 公立机构（含 MPS）销售，**数据托管在悉尼也属于跨境传输**，须满足例外（通常靠合同约束 + 合理措施）。STATE 未写明这一点。
5. **QLD MNDB 不直接适用于承包商**（OIC 官方指引）——但 OIC 要求 agency 在合同里写入 breach 通报条款；STATE 中的 ⚠️ 可关闭。
6. **州药品法本身就有记录保存期限**：QLD 药品记录 2 年（Medicines and Poisons (Medicines) Regulation 2021 s224）；WA S4 给药记录 2 年、S8 给药记录与 S8 登记册 **5 年**（Medicines and Poisons Regulations 2016 r143、r144）。STATE §6 "五辖区无私营方州级法定期限"需修正为"无一般健康记录期限，但药品记录有法定期限"。
7. **NT 家暴强制报告可能覆盖付费照护关系**：Domestic and Family Violence Act 2007 s124A（所有成年人须向警方报告严重身体伤害）+ s9(g)/s12 "carers relationship" 明确包括 "paid or unpaid care"。是否适用于机构内员工-居民关系需律师确认，但不能再写成"⚠️ 需核实是否存在"。

---

## 1. Queensland（QLD）

### 1.1 健康/信息隐私法

| 项目 | 结论 | 来源 |
|---|---|---|
| 适用对象 | Information Privacy Act 2009（IPA），经 Information Privacy and Other Legislation Amendment Act 2023（IPOLA）修订，自 **2025-07-01** 起 agencies 适用统一的 **Queensland Privacy Principles (QPPs)** 并实行强制数据泄露通报（MNDB）；local government 的 MNDB 自 2026-07-01 起。**不适用于私营 aged care provider**——私营 provider 及 CareKind 走联邦 Privacy Act 1988 / APPs 与 NDB | 🔎 OIC：https://www.oic.qld.gov.au/government/privacy/mandatory-data-breach-scheme ；https://www.oic.qld.gov.au/government/ipola ；法条 ✅ https://www.legislation.qld.gov.au/view/html/inforce/current/act-2009-014 |
| 对承包商（CareKind 向 Queensland Health 公立 RACF 销售时） | agency 须用合同把 contracted service provider **约束（bind）**于 QPPs、s33（境外披露）、s41（QPP code）。**MNDB 及其规则不直接适用于承包商**，但承包商的泄露可能构成 agency 的泄露；OIC 建议合同写入：及时报告、遏制与缓解、配合 agency 评估。OIC 还提醒 agency **不得依赖承包商的联邦 Privacy Act 义务**，必须在合同中写明 | 🔎 OIC "Contracting and privacy"：https://www.oic.qld.gov.au/government/privacy/contractors-privacy |
| OIC 页面日期矛盾 | OIC MNDB 主页面标注 "In effect from: 1 July 2026"，与 OIC 年报和其他页面"agencies 2025-07-01、local government 2026-07-01"不一致；以多数来源为准，**需人工打开页面复核** | 🔎 同上；OIC Annual Report 2024-25：https://www.oic.qld.gov.au/__data/assets/pdf_file/0020/4754/AL-2024-25.pdf |
| 公立卫生机构保密义务 | Hospital and Health Boards Act 2011 Part 7：s142 禁止 "designated person" 披露 confidential information；据解释性备忘录，designated person 包括在公立卫生设施工作的 Queensland Health 员工、**承包商**、志愿者。→ CareKind 若承接 QH RACF，其人员可能成为 designated person。现行 s139 定义原文【未核实】 | 🔎 explanatory note sl-2017-0107：https://legislation.qld.gov.au/view/pdf/published.exp/sl-2017-0107 ；法条：https://www.legislation.qld.gov.au/view/html/inforce/current/act-2011-032 |
| 公共档案 | **Public Records Act 2023 已于 2024-12-05 生效**，取代 2002 年法（STATE 中"生效日待核"可关闭）。仅约束公共机构；承接 QH 时需按其 retention & disposal schedule 配合 | 🔎 OIC 新闻：https://www.oic.qld.gov.au/about/news/commencement-of-the-public-records-act-2023 ；QSA：https://www.qld.gov.au/recreation/arts/heritage/archives/about-us/news-and-events/new-public-record-legislation |

### 1.2 录音/监听设备法 —— Invasion of Privacy Act 1971 ✅

来源：https://www.legislation.qld.gov.au/view/whole/html/inforce/current/act-1971-050 （现行版本 2024-07-01）

- **s4 "private conversation"**：一人对另一人说话、且情形表明双方希望只有彼此听到；**不包括**任何一方"ought reasonably to expect"会被他人听到/录下的话语。
- **s43(1)** 用 listening device 偷听/录制私人对话为罪（最高 40 penalty units 或 2 年监禁）；**s43(2)(a)** 使用者**是对话当事人**时不适用 → **一方（当事人）可录**。
- **s42** "party" 包括经说话者同意而录音/收听的人。
- **s45(1)** 当事人录音后，**传播或发布**录音或据其制作的陈述为罪（同上罚则）。**s45(2) 例外**：(a) 向其他当事人，或经**所有其他当事人明示或默示同意**；(b) 法律程序；(c) 为公共利益、**履行职责（performance of a duty）**或保护其 lawful interests 合理必要的范围内；(d) 向对该对话有合理利益的人。
- **对录音模式的影响**：
	- 模式 A（独自口述）：通常不是"对话"，不触发。
	- 护理人员在房间内与居民交谈时录音：护理人员是当事人，**录制本身合法**；但把录音上传给 CareKind 转写、生成供其他员工阅读的记录，属"communicate"——可主张 s45(2)(c)"履行职责"或 (d)"有合理利益的人"，**需律师意见**。最稳妥是取得居民（或其授权人）同意，满足 s45(2)(a)。
	- 模式 C（环境录音、CareKind 设备无人值守）：设备持有人若不是当事人，则不能依赖 s43(2)(a) → 高风险。

### 1.3 药品/毒麻药品记录 —— Medicines and Poisons Act 2019 + Medicines and Poisons (Medicines) Regulation 2021 ✅

来源：https://www.legislation.qld.gov.au/view/whole/html/inforce/current/sl-2021-0140 （in-force 版本 2026-10-05）

- **S8 medicine register（ch 8 pt 2 div 3）**：S8 safe/approved store 的 manager 须保存 register（s206）；**电子 register 允许**（s208），条件：需安全系统标识登录、每条记录录入人标识、**已确认条目不可删除**、可打印纸质报告；条目须在交易后 **24 小时内**录入（s211）；更正不得删除/遮盖原条目（s214）；至少每月对账（s217）。
- **记录保存（s224）**：凡本 Regulation 要求保存的记录，一般**自形成起 2 年**（纸质 register 自最后一条起 2 年）；须可检索、安全、不可被不留痕迹地修改/删除；电子记录须符合行业安全标准并定期备份（各项最高 40 penalty units）。
- **给药授权（Schedule 7）**：RN 可按 prescription/standing order 给药（Sch 7 Pt 3 Div 2 item 11）；EN 须在 RN/医生等监督下给药（Sch 7 Pt 4 item 19）。
- **对 CareKind**：CareKind **不是**也不应充当 S8 medicine register 或 medication chart；口述"已给药"仅生成叙述性护理记录草稿，正式给药记录/S8 登记须在 provider 的合规系统完成。草稿中不得补全剂量、不得建议给药（TGA 边界，PRD 硬规则）。
- Regulation 中未发现专门针对 "residential aged care" 的条款（全文检索，Schedules 16 以后未完整读取）【部分未核实】。

### 1.4 监护/代理决策与州级人员配比

- 监护框架（Guardianship and Administration Act 2000；Powers of Attorney Act 1998 的 Advance Health Directive 与 statutory health attorney）STATE §4 已列，本次未发现需纠正之处。
- **录音/AI 使用的同意不是 "health matter"**：州监护法下 statutory health attorney 的权限针对 health care；代理人能否代为同意"录音/AI 转写"属于 personal matter 还是 health matter【未核实】→ 依赖 QLD 一方可录规则时，此问题对模式 A 影响有限。
- **公立 RACF 人员配比**：Hospital and Health Boards Regulation **2023** 对公立 RACF 规定最低平均 daily resident care hours **3.65 小时/24 小时**，直接护理 skill mix **≥30% RN、≥50% nursing（RN+EN）**；自 2019-12 引入、2020-02 起报告；2025-04 起数据发布方式改变但 Regulation 与合规计量不变。（🔎 Queensland Health performance site：https://www.performance.health.qld.gov.au/statewide-performance/prevention-early-intervention-and-primary-health-care/aged-care ；Regulation 原文条号【未核实】）→ STATE 写的 "support workers ≤ 50%" 应改为 "nursing（RN+EN）≥ 50%"。

### 1.5 员工筛查、强制报告

- 无州级 aged care 专门筛查；联邦 Aged Care Rules 2025 要求 police certificate 或 NDIS worker screening clearance（FED）。QLD NDIS 筛查由州 worker screening unit 执行【未核实具体机构现名】。
- 无州级一般性成人虐待强制报告（STATE 已列）；RACF 内走联邦 SIRS。

### 1.6 与联邦法的交互

- 联邦 Aged Care Act 2024（2025-11-01 生效）与 Rules 2025 的 7 年记录保存是基线；QLD 州法不为私营方增加一般健康记录期限，但药品记录（2 年）可能与之并存——以较长者为准，实务即 7 年。
- Strengthened Quality Standards 的信息管理与记录准确性要求（FED §1.4）对 QLD 私营/公立设施一致适用；公立 RACF 额外受 IPA/QPPs、HHB Act 保密和 Public Records Act 2023。

### 1.7 QLD：对 CareKind 的影响 / 必须做的事 / paperwork

- [ ] 产品：模式 A 默认；UI 提示"离开房间后口述"；如录到居民话语，记录"已告知/已同意"状态（支持 s45(2)(a)）。
- [ ] 合同（私营 provider）：数据处理协议（DPA）写明 CareKind 作为 provider 的服务商，仅按指示处理、澳洲境内、零保留 LLM、NDB 协作（联邦）。
- [ ] 合同（Queensland Health 公立 RACF）：QPP 约束条款（含 s33 境外、s41 code）、**合同化的 breach 通报条款**（及时报告/遏制/配合评估）、HHB Act Part 7 保密承诺、Public Records Act 2023 retention 配合、分包商同样约束。
- [ ] 文件：居民/家属告知书（AI 文档工具、录音用途、数据位置）；员工使用协议；药品记录免责说明（"非 medication chart / S8 register"）。

---

## 2. Western Australia（WA）

### 2.1 健康/信息隐私法 —— Privacy and Responsible Information Sharing Act 2024（PRIS Act）

| 项目 | 结论 | 来源 |
|---|---|---|
| 生效 | IPPs 自 **2026-07-01** 起适用；IPP 1（收集）、7（unique identifiers）、8（匿名）、**10（automated decision-making）**仅适用于 2026-07-01 后收集的信息；**notifiable information breach scheme 自 2027-01-01** 起，适用于任何时间收集的信息 | ✅ WA OIC（页面更新 2026-03-03）：https://www.wa.gov.au/organisation/office-of-the-information-commissioner/understanding-my-privacy-rights-when-do-they-commence |
| 适用对象 | WA 政府机构、法定机构等 + "some contracted service providers to government"；**不适用于私营 aged care provider**（走联邦 Privacy Act） | ✅ 同上 |
| 承包商 | contracted service providers 属于 "IPP Entities"，按合同须遵守 PRIS | ⚖️ Clayton Utz（2024-08）：https://www.claytonutz.com/insights/2024/august/wa-privacy-and-responsible-information-sharing-laws-the-new-information-privacy-principles |
| IPP 9 | "Disclosure outside **Australia**"（与 APP 8 类似但细节不同；去标识化信息出境也受限）——**不是出州限制**，澳洲境内托管可满足 | ⚖️ 同上；法条原文【未核实】（legislation.wa.gov.au 最新汇编链接 404） |
| IPP 10（ADM） | 须对涉及个人信息的自动化决策保持透明：影响评估、定期评估、通知个人、提供人工干预途径 | ⚖️ 同上；"significant effect" 等门槛的法条原文【未核实】 |

→ 对 CareKind：仅在向 WA 公立机构（如 WA Country Health Service 的 aged care/MPS）销售时直接相关。CareKind 的输出是**护士审核的草稿**而非"决定"，但归属引擎（attribution）与分类可能被 agency 视为 ADM 组成部分 → 需准备 ADM 说明材料（与联邦 APP 1.7–1.9，2026-12-10 生效，一并设计）。

### 2.2 录音/监听设备法 —— Surveillance Devices Act 1998 ✅

来源（STATE 列出的 `law_a810.html` 链接**指向错误法案**——见 §7）：https://www.legislation.wa.gov.au/legislation/prod/filestore.nsf/FileURL/mrdoc_45890.htm/$FILE/Surveillance%20Devices%20Act%201998%20-%20%5B02-g0-00%5D.html （含至 2023-04-05 的修订）

- **s3** "private conversation"：情形表明一方希望只被当事人听到；不包括应合理预期会被他人听到的对话。"principal party"：说话者或被说话的对象。
- **s5(1)** 不得安装/使用/维护 listening device：(a) 录制/监听**非本人参与**的私人对话；**(b) 录制本人参与的私人对话** → **当事人录音原则上也违法**。罚则：个人 $5,000 或 12 个月监禁或两者；法人 $50,000。
- **s5(3)**（仅对 s5(1)(b) 的例外）：(c) **每一位 principal party 明示或默示同意**；(d) 一位 principal party 同意且对保护该 principal party 的 **lawful interests 合理必要**。
- **s26（Part 5 public interest）**：(1) 当事人在一位 principal party 同意且有合理理由认为符合公共利益时可录；(3) carer/监护人等可代表儿童或 "protected person"（因精神障碍无法同意者）在符合其最大利益且公共利益时使用设备。
- **s9** 发布/传播通过设备获得的私人对话为罪，例外包括经每位 principal party 同意、履行职责、保护 lawful interests、法律程序等（s9(3) 限于合理必要范围）。
- **对录音模式的影响**：模式 A 独自口述一般不触发；房间内与居民交谈时录音 → 需**居民及在场每位说话者同意**（s5(3)(c)），"护理文档"难以套入 lawful interests 例外（该例外针对 principal party 自身法律利益，如取证）。认知障碍居民：s26(3) 是"代表 protected person"使用设备，**不是**代为同意他人录音的一般授权 → 模式 C 在 WA 风险最高之一。

### 2.3 药品/毒麻药品记录 —— Medicines and Poisons Act 2014 + Medicines and Poisons Regulations 2016 ✅

来源：https://www.legislation.wa.gov.au/legislation/prod/filestore.nsf/FileURL/mrdoc_49666.htm/$FILE/Medicines%20and%20Poisons%20Regulations%202016%20-%20%5B00-t0-00%5D.html （含至 SL 2025/212 的修订）

- **r14 residential care chart**：S4 可为纸质（墨水填写、处方者逐条签名日期）或经 **approved electronic prescribing system** 完成的电子 chart；**S8 只能通过 approved electronic prescribing system 完成**。
- **r143 给药/供应记录**：给予 S4/S8 的 authorised health professional 须确保在 clinical record 记录药名、数量、规格、剂型、日期等；**保存期 S4 ≥2 年、S8 ≥5 年**（自给药/供应之日）。
- **r144 S8 register**：authorised person 每处场所保存 register，事件发生时录入并签名；**保存 ≥5 年**。**r146–147**：register 须为 CEO 批准的形式；电子 register 须条目不可删除、系统标识+访问码、自动记录录入人、可打印。
- **r15(3)**：口头/电话医嘱，处方者须在 24 小时内在 clinical record 记录并签名。
- **对 CareKind**：同 QLD——不做 chart、不做 register、不建议剂量。若 provider 把 CareKind 审核后记录作为 r143 "clinical record" 的一部分，则**相关记录须可保存 5 年**（低于联邦 7 年，以 7 年为准）；CareKind 侧不得在保留期内删除已推送的正式记录或其审计轨迹。

### 2.4 监护/代理决策

- Guardianship and Administration Act 1990：Part 9B AHD、Part 9C/9D 治疗决策 "person responsible"（s110ZD）与无行为能力患者优先顺序（s110ZJ）。WA OPA 归纳的顺序：enduring guardian → guardian → 配偶/de facto → 成年子女（**所有成年子女同等优先**，OPA 2026 position statement）→ 父母 → primary unpaid caregiver → 兄弟姐妹 → 其他亲近人士；AHD 优先于该顺序。**付费支持工作者无权作治疗决定**。s110ZK 保护善意依赖上述决定的 health professional。（🔎 WA OPA：https://www.wa.gov.au/system/files/2026-07/opa-position-statement-1.pdf ；法条 ✅ https://www.legislation.wa.gov.au/legislation/prod/filestore.nsf/FileURL/mrdoc_45303.htm/$FILE/Guardianship%20and%20Administration%20Act%201990%20-%20%5B05-o0-00%5D.html ）
- → 文档模板记录 consent 来源时，WA 需能记录"依 s110ZD 顺序中的第几位"。

### 2.5 员工筛查、强制报告

- 无州级成人虐待强制报告；未发现 2025–2026 年 WA adult safeguarding 法案【未核实（仅一次检索无结果）】。
- 员工筛查依联邦 Rules（FED）；WA NDIS 筛查由 Department of Communities 执行【未核实】。

### 2.6 与联邦法交互

- 私营 provider：联邦 Privacy Act + Aged Care Act/Rules + 州药品法（S8 5 年）。公立：另加 PRIS Act（2026-07-01 IPPs、2027-01-01 breach）。
- Quality Standards 关于用药安全（medication management）的记录要求与 WA r143 并行；CareKind 草稿只作叙述记录。

### 2.7 WA：对 CareKind 的影响 / 必须做的事 / paperwork

- [ ] 产品：**模式 A 强制**；在 WA 部署时 UI 明确"录音前须确保没有他人对话被录入"；如需录居民话语，前置"每位在场说话者已同意"勾选并留痕。
- [ ] 合同（公立 WA 机构）：PRIS CSP 条款、2027-01-01 起的 breach 通报配合、ADM 透明度材料（IPP 10）、澳洲境内托管（IPP 9）。
- [ ] 保留策略：provider 可配置"药品相关记录 ≥5 年"（实际按联邦 7 年）。
- [ ] 文件：居民/家属录音同意书（WA 需**全体当事人**同意版本）；员工告知；药品记录免责说明。

---

## 3. South Australia（SA）

### 3.1 健康/信息隐私法

- **无隐私立法**。公共部门适用 Premier and Cabinet Circular **PC012 – Information Privacy Principles Instruction (IPPI)**，对 state agencies 有约束力，由各 agency principal officer 负责落实；IPPI 定义了 "contracted service provider" 与 "contract for service"，State Records 指引要求政府合同适当适用 IPPI，Crown Solicitor's Office 有范本条款。Privacy Committee 2022-23 年报指出**用 IPPI 约束承包商存在法律复杂性**。（🔎 https://www.archives.sa.gov.au/managing-information/privacy-in-south-australia/information-privacy-principles-instruction ；https://archives.sa.gov.au/managing-information/privacy-in-south-australia/contracting-and-the-ippi ；Privacy Committee 2024-25 年报：https://archives.sa.gov.au/privacy-committee/privacy-committee-annual-reports/privacy-committee-of-south-australia-2024-25-annual-report ）
- 未发现 2025–2026 年 SA 隐私法案【未核实（单次检索）】。
- **私营 provider 与 CareKind：联邦 Privacy Act 1988 兜底**；SA 无州级 breach 通报。
- SA Health 的 Health Care Act 2008 保密条款及 "Code of Fair Information Practice" 对承接 SA Health 公立服务的影响【未核实】。

### 3.2 录音/监听设备法 —— Surveillance Devices Act 2016 🔎

（legislation.sa.gov.au 对抓取返回 403；以下依据 SA Legal Services Commission 的 *Law Handbook*（政府法律援助机构）及高等法院判决信息）

- **s4** 禁止安装/使用/维护 listening device 偷听、录制、监听私人对话；以取得**所有 principal parties 明示或默示同意**为原则；例外包括：各方同意、为保护某人 lawful interests 所需、符合公共利益。罚则：个人最高 $15,000 或 3 年监禁；法人最高 $75,000。（🔎 https://lawhandbook.sa.gov.au/ch34s01s04.php ，最后修订 2018-04-17）
- **lawful interests 为客观判断**；为在民事诉讼中取得优势一般**不**构成 lawful interest（*Thomas & Anor v Nash* [2010] SASC 153）。（🔎 https://lawhandbook.sa.gov.au/ch34s01s04s04.php ）
- **s12** 明知而使用、传播、发布由监控设备获得的信息为罪，除非适用例外（如各方同意）；个人 $15,000 或 3 年、法人 $75,000。（🔎 https://lawhandbook.sa.gov.au/ch34s01s04s05.php ）
- **新判例**：*Potter (A Pseudonym) v The King* [2026] HCA 25（2026-08-05）涉及 s4(2)(a)(ii) lawful interests 例外的解释。判决具体要点本次未能读取（下载超时）【未核实】——建议律师审阅其对"当事人为保护自身利益录音"的影响。（https://www.hcourt.gov.au/sites/default/files/eresources/2026-08-05/HCA/Potter%20%28A%20Pseudonym%29%20v%20The%20King%20%28A24-2025%29%20%5B2026%5D%20HCA%2025.pdf ）
- s4(1)/(2) 条文原文【未核实（一手法条 403）】；STATE 所称 "s4" 结构与本次资料一致。
- **对录音模式的影响**：与 WA 相同——模式 A 可行；录到居民话语需**全体当事人同意**；模式 C 高风险。

### 3.3 药品/毒麻药品记录

- 框架：Controlled Substances Act 1984 + Controlled Substances (Poisons) Regulations 2011（drug of dependence register 等）。register 保存期、电子 register 条件、对 RACF 的具体要求【未核实】（法条站点 403；SA Health 页面未列保存期：https://www.sahealth.sa.gov.au/wps/wcm/connect/public+content/sa+health+internet/clinical+resources/clinical+programs+and+practice+guidelines/medicines+and+drugs/drugs+of+dependence ）。
- 对 CareKind 的设计结论与 QLD/WA 相同（不做 register、不建议）。

### 3.4 监护/代理决策

- Advance Care Directives Act 2013（substitute decision-maker）、Consent to Medical Treatment and Palliative Care Act 1995（"person responsible"）、Guardianship and Administration Act 1993 —— STATE §4 已列，本次未发现需纠正之处【未重新核对法条】。

### 3.5 员工筛查、强制报告

- **Ageing and Adult Safeguarding Act 1995**（2018 修订设立 Adult Safeguarding Unit）：**自愿报告 + 机构强制回应**，不对有行为能力成年人设强制报告（议会 Hansard 2018）。（🔎 https://hansardsearch.parliament.sa.gov.au/daily/uh/2018-09-06/36 ）
- 员工筛查：SA DHS Screening Unit（NDIS 筛查）【未核实】；aged care 依联邦 Rules。

### 3.6 SA：对 CareKind 的影响 / 必须做的事 / paperwork

- [ ] 产品：同 WA（全方同意州）。
- [ ] 合同（SA 政府/SA Health）：IPPI 合同条款（采用 Crown Solicitor 范本）、保密、State Records Act 1997 配合；因 IPPI 约束力有限，**以合同义务为主**。
- [ ] 合同（私营）：联邦 APPs DPA。
- [ ] 文件：全体当事人录音同意书；告知书。
- [ ] 待办：请律师就 *Potter v The King* [2026] HCA 25 出具意见。

---

## 4. Tasmania（TAS）

### 4.1 健康/信息隐私法 —— Personal Information Protection Act 2004（PIP Act）✅

来源：https://www.legislation.tas.gov.au/view/whole/html/inforce/current/act-2004-046 （授权版本 2024-09-05）

- **s3 "personal information custodian"** 包括：(a) public authority；**(b) 与 custodian 订立 "personal information contract"（关于个人信息收集、使用或存储的合同）的任何机构或个人**；(c) 规定机构。**s17(1)** custodian 须遵守 PIP principles。→ **CareKind 若与 TAS 公立机构签约处理个人信息，自身即成为 custodian，直接受该法约束**（不仅是合同义务）。
- **私营 provider 不受约束**（非 public authority），走联邦 Privacy Act。
- **无数据泄露通报义务**（仅 Sch 1 cl 4 的"合理保护"义务）。TLRI 曾建议引入 breach 通报（⚖️ https://thesenior.com.au/story/8673793/tasmania-calls-for-data-breach-notification-law-update ）；2025–2026 年是否有修订法案【未核实】。
- **PIPP 9（Sch 1 cl 9）跨境 = "outside Tasmania"**：仅在以下情形可向塔州以外披露：接收方受实质相似原则的法律/约束性计划/合同约束；本人同意；合同履行所需；custodian 已采取合理措施确保接收方不违反原则；法律授权。→ **CareKind 在悉尼（NSW）托管 TAS 公立客户数据也属于"出州"**；须用合同约束 + 合理措施满足 PIPP 9。

### 4.2 录音/监听设备法 —— Listening Devices Act 1991 ✅

来源：https://www.legislation.tas.gov.au/view/whole/html/inforce/current/act-1991-021 （授权版本 2019-02-14）

- **s3** "private conversation"：一人对一人或多人说话，情形可合理表明说话者希望只被他们自己（或经全体同意的人）听到。"principal party"：说话者或被说话的对象。
- **s5(1)** 不得使用、或**致使或允许使用（cause or permit to be used）** listening device：(a) 录制/监听非本人参与的私人对话；**(b) 录制本人参与的私人对话**。
- **s5(3)** s5(1)(b) 的例外：(a) **所有 principal parties 明示或默示同意**；或 (b) 一位 principal party 同意，且 (i) 对保护该 principal party 的 lawful interests 合理必要，**或 (ii) 录音不是为了向非当事人传播对话或其报告**。
- **s5(2)(d)** "unintentional hearing" 不适用禁令；**s9** 对违法或无意获得内容的传播限制；**s10** 当事人录音后的传播限制（例外：向其他当事人或经全体 principal parties 同意、法律程序、保护 lawful interests 合理必要、向有合理利益的人）。
- **罚则（s12）**：个人最高 40 penalty units 或 2 年监禁或两者；**法人最高 500 penalty units**。
- **对录音模式的影响**：
	- 模式 A 独自口述：非"对话"。
	- 房间内录到居民话语：s5(3)(b)(ii) 看似允许"一方同意 + 不为传播"，但护理记录**本来就是给其他员工阅读**，大概率不满足 → 实务上仍需**全体同意**。
	- **"cause or permit to be used"**：CareKind 作为设备/软件提供方，若产品被设计为环境录音，可能被认为"致使"使用 → 模式 C 对公司本身有刑事风险（法人 500 penalty units）。

### 4.3 药品/毒麻药品记录

- 框架：Poisons Act 1971 + Poisons Regulations 2018（SR 2018 No. 79）。据 AustLII 转载，reg 94(2) 要求销售/供应毒物者保存发票与处方记录 **≥2 年**（⚖️/🔎 https://classic.austlii.edu.au/au/legis/tas/consol_reg/pr2018230/s94.html ）；S8 register 保存期及 RACF 给药记录要求【未核实】。官方 PDF：https://www.legislation.tas.gov.au/view/pdf/authorised/2026-02-16%202026-02-16/sr-2018-079

### 4.4 监护/代理决策

- Advance care directive 由 Guardianship and Administration Amendment (Advance Care Directives) Act 2021 插入 G&A Act 1995 **Part 5A**，**2022-11-21 生效**（🔎 Justice Miscellaneous (Advance Care Directives) Act 2022 clause notes：https://www.parliament.tas.gov.au/__data/assets/pdf_file/0019/53353/41_of_2022-clause20notes.pdf ；法案：https://www.legislation.tas.gov.au/view/whole/html/asmade/act-2021-015 ）；ACD 可上传至 TASCAT 维护的登记册（⚖️）。STATE 的 2024-09-01 G&A 改革内容不变。

### 4.5 员工筛查、强制报告

- Registration to Work with Vulnerable People（RWVP）：NDIS Worker Check 需先取得带 NDIS endorsement 的 RWVP，有效 5 年；司法部页面称计划扩展 regulated activities 并纳入"nationally consistent aged care worker registration"，时间与内容【未核实】。（🔎 https://www.justice.tas.gov.au/rwvp ；https://www.justice.tas.gov.au/rwvp/apply-or-renew/ndis-worker-check ）
- 无州级成人虐待强制报告（STATE 已列）。

### 4.6 TAS：对 CareKind 的影响 / 必须做的事 / paperwork

- [ ] 产品：同 WA/SA（全方同意州），且注意"cause or permit"——**不提供**任何默认常开录音配置。
- [ ] 合同（TAS 公立/MPS）：CareKind 作为 custodian 直接遵守 PIP principles；**PIPP 9 出州条款**（说明 NSW 托管、合同约束、安全措施）；自愿 breach 通报条款。
- [ ] 文件：全体当事人录音同意书；告知书（注明数据在 NSW/澳洲境内托管）。

---

## 5. Northern Territory（NT）

### 5.1 健康/信息隐私法 —— Information Act 2002 ✅

来源：https://legislation.nt.gov.au/en/Legislation/INFORMATION-ACT-2002 （Word 版本 as in force at 2026-06-01）

- Part 5（信息隐私）适用于 **public sector organisations**；**s5(7)(c)–(d)** 把 public sector organisation 的范围延伸至 "**contract service provider** to the extent of the services it provides under the service contract" 及其员工/代理人；s4 "service contract" = 为公共机构收集或处理个人信息的合同。s149 规定承包商责任（原文未读取）。→ CareKind 与 NT 公立机构签约时**直接受 IPPs 约束**。
- **私营 provider 不受约束**，走联邦 Privacy Act。
- **无数据泄露通报**（全文检索未见相关部分）。
- **IPP 9 Transborder data flows = "outside the Territory"**：仅在法律授权、接收方受实质相似原则约束、本人同意、合同履行所需、为本人利益且无法取得同意、或已采取合理措施等情形下可转移。→ **悉尼托管 NT 公立数据也是"出领地"**。
- IPP 10 敏感信息（含健康信息）收集需同意或法律授权等。
- Part 9 记录与档案管理（s130–145，含 retention and disposal schedules s136A–136B）适用于公共机构【条文内容未读取】。

### 5.2 录音/监听设备法 —— Surveillance Devices Act 2007 ✅

来源：https://legislation.nt.gov.au/en/Legislation/SURVEILLANCE-DEVICES-ACT-2007 （Word 版本 as in force at 2026-06-01）

- **s4** "private conversation"；"party" = 说话者或被说话的对象。
- **s11(1)** 罪名仅针对录制/监听**本人不是当事人**、且明知未经每位当事人同意的私人对话 → **当事人可录**。罚则 **250 penalty units 或 2 年监禁**（STATE 未列罚则）。
- **s15(1)** 明知录音/报告来自监控设备而传播或发布为罪（同罚则）——**适用于任何人，包括当事人自己录的**；**s15(2) 例外**：经每位当事人明示或默示同意；为公共利益或**保护传播者 lawful interests 合理必要**；法律或**纪律程序（disciplinary proceeding）**中；等。
- **对录音模式的影响**：与 QLD 类似——当事人录音合法，但上传、转写、供他人阅读属"communicate"，NT s15(2) **没有 QLD s45(2)(c) 那样的"履行职责"或 (d)"有合理利益的人"例外**，例外面更窄 → 录到居民话语时**取得居民同意更为必要**。【该比较需律师确认】

### 5.3 药品/毒麻药品记录

- 框架：Medicines, Poisons and Therapeutic Goods Act 2012 + Regulations。S8 register、给药记录保存期及 RACF 要求【未核实】。

### 5.4 监护/代理决策

- Guardianship of Adults Act 2016；Advance Personal Planning Act 2013 —— STATE 已列，本次未重新核对【未核实】。

### 5.5 员工筛查、强制报告 —— **重要补充**

- **Domestic and Family Violence Act 2007 s124A** ✅（as in force at 2025-06-07；https://legislation.nt.gov.au/en/Legislation/DOMESTIC-AND-FAMILY-VIOLENCE-ACT-2007 ）：**任何成年人**如合理相信 (i) 某人已经或可能对与其处于 domestic relationship 的人造成伤害（harm = **serious physical harm**），或 (ii) 某人的生命或安全因家暴受到严重或迫在眉睫的威胁，须**尽快向警方报告**；最高 **200 penalty units**；合理理由抗辩（如合理相信他人已报告）；s125 善意报告者免责。
- **s9(g) + s12**：domestic relationship 包括 "carers relationship"，即"一方依赖另一方持续的 **paid or unpaid care**"。→ 字面上可能覆盖**付费照护者与被照护者**；对 RACF 员工-居民关系的适用性【需律师确认】。
- 对 CareKind：AI 不得判断"是否需要报告"（非诊断/风险评分边界）；但产品应忠实记录护士口述的伤害观察，并在 NT 部署的培训材料中提醒 provider 其 s124A 与联邦 SIRS 双重义务。
- 员工筛查：SAFE NT（NDIS 筛查）【未核实】；aged care 依联邦 Rules。

### 5.6 NT：对 CareKind 的影响 / 必须做的事 / paperwork

- [ ] 产品：模式 A；录到居民话语时取得同意并留痕（s15(2)(a)）。
- [ ] 合同（NT 公立/MPS）：CareKind 作为 contract service provider 直接遵守 IPPs；**IPP 9 出领地**条款；自愿 breach 通报条款；Part 9 records 配合。
- [ ] 文件：居民录音同意书（针对"传播"）；provider 培训材料中加入 NT DFV s124A 提示（仅提示，非法律意见）。

---

## 6. 与联邦 Aged Care Act 2024 / Strengthened Quality Standards 的交互（五辖区共通）

- **联邦为主框架**：Aged Care Act 2024 与 Aged Care Rules 2025 自 2025-11-01 生效，记录保存 7 年（Rules s154 系列，见 FED §1.1），Rules 多处注明 provider "may be required to comply with other Commonwealth, State or Territory laws in relation to the retention of records"——即州药品法等保存期与联邦并行，取最长。
- **州法补充而非取代**：本次五辖区均无约束私营方的州健康记录法；州层面对私营 provider 的直接影响主要是**录音法（刑法）**、**药品法**、**监护法（同意来源）**、NT DFV 报告义务。对公立 provider，再叠加州公共部门隐私法与档案法。
- **Strengthened Quality Standards**：信息管理与记录准确（FED §1.4，Outcome 2.7）、交接（Outcome 3.3）与用药安全要求在五辖区统一适用；州药品法规定"谁可给药、怎么登记"，Standards 要求"记录准确及时"——CareKind 草稿须忠实于口述，不得补全药品细节。
- **Restrictive practices 同意**：先按州监护法确定 RPSDM，州法无途径时才用 Rules 层级（STATE §4）。WA 的 s110ZD 顺序、SA 的 ACD Act、TAS Part 5A ACD、NT APP Act、QLD POA Act 各不相同 → 模板需"辖区 + 依据"字段。

---

## 7. 五辖区对比表

| 维度 | QLD | WA | SA | TAS | NT |
|---|---|---|---|---|---|
| 录音：当事人可否录私人对话 | ✅ 可（IoPA s43(2)(a)） | ❌ 原则上需每位 principal party 同意（SDA s5(1)(b)、s5(3)(c)） | ❌ 需所有 principal parties 同意（SDA 2016 s4）🔎 | ❌ 需全体同意；或一方同意 + lawful interests / 不为传播（LDA s5(3)） | ✅ 可（SDA s11 仅禁非当事人） |
| 录音：传播限制 | s45：需全体同意或职责/合理利益等例外 | s9 | s12 | s10 | s15：需每位当事人同意或 lawful interests 等（无"职责"例外） |
| 录音罚则（个人/法人） | 40 PU 或 2 年 | $5,000 或 12 月 / $50,000 | $15,000 或 3 年 / $75,000 🔎 | 40 PU 或 2 年 / 500 PU | 250 PU 或 2 年 |
| 州隐私法覆盖私营 provider | ❌（联邦兜底） | ❌（联邦兜底） | ❌ 无隐私法（联邦兜底） | ❌（联邦兜底） | ❌（联邦兜底） |
| 州隐私法直接约束承包商（CareKind） | 经合同 bind（QPPs、s33） | CSP 属 IPP Entity | 仅合同（IPPI，约束力有限） | 订立 personal information contract 即成 custodian | contract service provider 视同公共机构 |
| 州级 breach 通报 | agencies 2025-07-01（不直接适用承包商） | 2027-01-01 | 无 | 无 | 无 |
| 公共部门数据"出境"标准 | 出澳（s33）⚖️ | 出澳（IPP 9）⚖️ | — | **出塔州**（PIPP 9） | **出领地**（IPP 9） |
| 记录保存（私营健康记录） | 无州法 → 联邦 7 年 | 无州法 → 联邦 7 年 | 无州法 → 联邦 7 年 | 无州法 → 联邦 7 年 | 无州法 → 联邦 7 年 |
| 药品记录法定保存 | 2 年（MPMR s224） | S4 2 年；S8 给药记录与 register 5 年（r143/r144） | 【未核实】 | 发票/处方 ≥2 年（reg 94）⚖️；register【未核实】 | 【未核实】 |
| 州级强制报告（成人） | 无 | 无 | 无（自愿 + Adult Safeguarding Unit） | 无 | **DFV s124A：所有成年人，含 carers relationship（paid care）** |
| 关键 paperwork | 居民告知/同意（覆盖 s45 传播）；QH 合同含 QPP + breach 条款 | **全体当事人**录音同意书；PRIS CSP 条款 + ADM 说明 | 全体当事人同意书；IPPI 合同条款 | 全体当事人同意书；PIPP 9 出州条款 | 居民同意书（覆盖 s15 传播）；IPP 9 出领地条款；DFV 培训提示 |

---

## 8. 与 state-by-state-comparison.md 的差异 / 纠错建议

> 只提建议，未修改 STATE。是否采纳由 Terry 决定；修改 STATE 后需更新 `changelog/CHANGELOG.md`。

| # | STATE 位置 | 现状 | 建议 | 依据 |
|---|---|---|---|---|
| 1 | §1 QLD 行 "⚠️ MNDB 对 CSP 的直接适用性需核实" | 未决 | 改为：MNDB **不直接适用**于承包商；agency 须以合同写入 breach 通报/遏制/配合条款，且不得依赖承包商的联邦义务 | §1.1 OIC |
| 2 | §1 TAS 行 "跨境：有限" | 不明确 | 改为：PIPP 9 限制向 **塔州以外** 披露；承包商订立 personal information contract 即成为 custodian | §4.1 |
| 3 | §1 NT 行 "IPP 9" | 未说明标准 | 补充：IPP 9 为 **"outside the Territory"**；contract service provider 视同 public sector organisation（s5(7)） | §5.1 |
| 4 | §2 TAS 行 "例外：保护 lawful interests 等" | 不完整 | 补充 s5(3)(b)(ii)"一方同意且不为向非当事人传播"例外，及其对护理记录场景大概率不适用；补充 "cause or permit" 与法人 500 PU | §4.2 |
| 5 | §2 WA 行 | 只写 lawful interests | 补充 s26 public interest 及 s26(3) protected person 条款；罚则 | §2.2 |
| 6 | §2 NT 行 "限制传播" | 未说明例外范围 | 补充 s15(2) 例外（无"履行职责"例外）与罚则 250 PU | §5.2 |
| 7 | §2 下方 ⚠️ 说明 | 五辖区分类待复核 | QLD、WA、TAS、NT 已读到官方法条，可改为 ✅；SA 仍为 🔎（官方站点 403），并新增 *Potter v The King* [2026] HCA 25 待律师审阅 | §1.2 / §2.2 / §3.2 / §4.2 / §5.2 |
| 8 | §3 QLD 行 "support workers ≤ 50%" | **疑似错误** | 改为 "直接护理 skill mix ≥30% RN、≥50% nursing（RN+EN）"；法规名称写 Hospital and Health Boards Regulation **2023** | §1.4 |
| 9 | §5 NT 行 "⚠️ DFV s124A 需核实" | 未决 | 改为：已核实 s124A（200 PU，serious physical harm）；domestic relationship 含 paid/unpaid carers relationship（s9(g)、s12）；对 RACF 员工-居民的适用需律师确认 | §5.5 |
| 10 | §6 "QLD/WA/SA/TAS/NT 无私营方州级法定期限" | 不完整 | 补充：州**药品法**有法定期限——QLD 2 年（s224）、WA S8 5 年（r143/r144）；整体仍以联邦 7 年为准 | §1.3 / §2.3 |
| 11 | §6 "Qld Public Records Act 2023 ⚠️ 生效日待核" | 未决 | 改为：**2024-12-05 生效** | §1.1 |
| 12 | §4 TAS 行 | 未写 ACD 生效日 | 补充 Part 5A ACD **2022-11-21** 生效、TASCAT 登记册 | §4.4 |
| 13 | 来源 "WA Surveillance Devices Act 1998：…law_a810.html" | **链接错误**（该页为 Taxation (Staff Arrangements) Act 1969） | 换为 legislation.wa.gov.au 的 SDA 1998 汇编链接（见 §2.2） | §2.2 |
| 14 | §10 启示 4 "数据位置" | 只提 VIC/NSW 法定出境限制 | 补充：向 TAS/NT 公立客户销售时，**州外（含 NSW）托管即属出境**，须合同 + 合理措施 | §4.1 / §5.1 |
| 15 | §1 WA 行 | 未提 ADM | 补充 IPP 10 automated decision-making（2026-07-01 后收集的信息适用） | §2.1 |

---

## 9. 未核实项（需律师或后续检索）

1. SA Surveillance Devices Act 2016 s4、s12 的一手条文（legislation.sa.gov.au 403），以及 *Potter v The King* [2026] HCA 25 的判决要点。
2. WA PRIS Act IPP 9、IPP 10 的法条原文与 ADM 门槛（最新汇编链接 404，仅有律所二手资料）。
3. QLD Hospital and Health Boards Act 2011 s139 "designated person" 现行定义；Hospital and Health Boards Regulation 2023 中人员配比的条号与原文；OIC MNDB 页面 "In effect from 1 July 2026" 标注矛盾。
4. SA（Controlled Substances (Poisons) Regulations 2011）、TAS（Poisons Regulations 2018 S8 register）、NT（Medicines, Poisons and Therapeutic Goods Act 2012）的药品记录保存期及 RACF 要求。
5. 各州 NDIS worker screening 机构现名、TAS "nationally consistent aged care worker registration" 的时间表。
6. TAS 是否有 2025–2026 年 PIP Act breach 通报修订；SA 是否有隐私法案；WA 是否有 adult safeguarding 法案（均仅单次检索无结果）。
7. NT DFV s124A 对 RACF 付费照护关系的适用性。
8. QLD s45(2)(c)/(d)、NT s15(2)(b) 能否覆盖"上传至服务商转写并写入护理记录"——这是 QLD/NT 录音合规的关键法律问题。
9. 代理决策人（QLD statutory health attorney、WA person responsible 等）能否代居民同意录音/AI 转写。
10. 护理人员"独自口述"不构成 "private conversation" 的解释（模式 A 的法律基础）——需律师书面确认。
11. NT Guardianship of Adults Act 2016 / Advance Personal Planning Act 2013、SA ACD Act 2013 本次未重新核对条文。

---

## 来源（Sources）

- QLD Invasion of Privacy Act 1971：https://www.legislation.qld.gov.au/view/whole/html/inforce/current/act-1971-050
- QLD Information Privacy Act 2009：https://www.legislation.qld.gov.au/view/html/inforce/current/act-2009-014
- QLD OIC：https://www.oic.qld.gov.au/government/privacy/contractors-privacy ；https://www.oic.qld.gov.au/government/privacy/mandatory-data-breach-scheme ；https://www.oic.qld.gov.au/government/ipola ；https://www.oic.qld.gov.au/about/news/commencement-of-the-public-records-act-2023
- QLD Medicines and Poisons (Medicines) Regulation 2021：https://www.legislation.qld.gov.au/view/whole/html/inforce/current/sl-2021-0140
- QLD Hospital and Health Boards Act 2011：https://www.legislation.qld.gov.au/view/html/inforce/current/act-2011-032 ；explanatory note：https://legislation.qld.gov.au/view/pdf/published.exp/sl-2017-0107
- QLD aged care performance：https://www.performance.health.qld.gov.au/statewide-performance/prevention-early-intervention-and-primary-health-care/aged-care
- WA Surveillance Devices Act 1998：https://www.legislation.wa.gov.au/legislation/prod/filestore.nsf/FileURL/mrdoc_45890.htm/$FILE/Surveillance%20Devices%20Act%201998%20-%20%5B02-g0-00%5D.html
- WA OIC PRIS commencement：https://www.wa.gov.au/organisation/office-of-the-information-commissioner/understanding-my-privacy-rights-when-do-they-commence
- WA PRIS IPPs（⚖️ Clayton Utz）：https://www.claytonutz.com/insights/2024/august/wa-privacy-and-responsible-information-sharing-laws-the-new-information-privacy-principles
- WA Medicines and Poisons Regulations 2016：https://www.legislation.wa.gov.au/legislation/prod/filestore.nsf/FileURL/mrdoc_49666.htm/$FILE/Medicines%20and%20Poisons%20Regulations%202016%20-%20%5B00-t0-00%5D.html
- WA Guardianship and Administration Act 1990：https://www.legislation.wa.gov.au/legislation/prod/filestore.nsf/FileURL/mrdoc_45303.htm/$FILE/Guardianship%20and%20Administration%20Act%201990%20-%20%5B05-o0-00%5D.html ；WA OPA：https://www.wa.gov.au/system/files/2026-07/opa-position-statement-1.pdf
- SA Law Handbook（Legal Services Commission）：https://lawhandbook.sa.gov.au/ch34s01s04.php ；https://lawhandbook.sa.gov.au/ch34s01s04s04.php ；https://lawhandbook.sa.gov.au/ch34s01s04s05.php
- *Potter (A Pseudonym) v The King* [2026] HCA 25：https://www.hcourt.gov.au/sites/default/files/eresources/2026-08-05/HCA/Potter%20%28A%20Pseudonym%29%20v%20The%20King%20%28A24-2025%29%20%5B2026%5D%20HCA%2025.pdf
- SA IPPI：https://www.archives.sa.gov.au/managing-information/privacy-in-south-australia/information-privacy-principles-instruction ；https://archives.sa.gov.au/managing-information/privacy-in-south-australia/contracting-and-the-ippi
- SA Privacy Committee 2024-25：https://archives.sa.gov.au/privacy-committee/privacy-committee-annual-reports/privacy-committee-of-south-australia-2024-25-annual-report
- SA Hansard（Adult Safeguarding 2018）：https://hansardsearch.parliament.sa.gov.au/daily/uh/2018-09-06/36
- SA Health drugs of dependence：https://www.sahealth.sa.gov.au/wps/wcm/connect/public+content/sa+health+internet/clinical+resources/clinical+programs+and+practice+guidelines/medicines+and+drugs/drugs+of+dependence
- TAS Personal Information Protection Act 2004：https://www.legislation.tas.gov.au/view/whole/html/inforce/current/act-2004-046
- TAS Listening Devices Act 1991：https://www.legislation.tas.gov.au/view/whole/html/inforce/current/act-1991-021
- TAS Poisons Regulations 2018：https://www.legislation.tas.gov.au/view/pdf/authorised/2026-02-16%202026-02-16/sr-2018-079 ；AustLII reg 94：https://classic.austlii.edu.au/au/legis/tas/consol_reg/pr2018230/s94.html
- TAS ACD：https://www.legislation.tas.gov.au/view/whole/html/asmade/act-2021-015 ；https://www.parliament.tas.gov.au/__data/assets/pdf_file/0019/53353/41_of_2022-clause20notes.pdf
- TAS RWVP：https://www.justice.tas.gov.au/rwvp ；https://www.justice.tas.gov.au/rwvp/apply-or-renew/ndis-worker-check
- NT Surveillance Devices Act 2007：https://legislation.nt.gov.au/en/Legislation/SURVEILLANCE-DEVICES-ACT-2007
- NT Information Act 2002：https://legislation.nt.gov.au/en/Legislation/INFORMATION-ACT-2002
- NT Domestic and Family Violence Act 2007：https://legislation.nt.gov.au/en/Legislation/DOMESTIC-AND-FAMILY-VIOLENCE-ACT-2007
