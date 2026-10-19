# 州/领地深度核查：NSW、VIC、ACT —— Aged Care 文档相关州法

> ⚠️ **内部工作底稿，非法律意见。** 核查日期：**2026-10-19** ｜ Owner: Terry ｜ 复审：每季度，以及进入新州客户之前
>
> 性质：对 [state-by-state-comparison.md](state-by-state-comparison.md)（下称 STATE，2026-10-10）中 NSW / VIC / ACT 三地内容做**补充、核实、纠错**。已在 STATE 与 [federal-law-summary.md](federal-law-summary.md)（下称 FED）中写清楚的内容不重复，只引用。
>
> 标记：✅ = 已对照官方法律原文或官方部门页面核实（注明版本）；**【未核实】** = 未能取得官方一手文本；**【需律师确认】** = 原文已核实，但对 CareKind 的适用属于法律解释；（二手）= 仅有律所/媒体来源。
>
> 核查方法：法律原文取自 legislation.act.gov.au、legislation.vic.gov.au（authorised PDF）、legislation.nsw.gov.au。**NSW 网站当日对 current version 限流（HTTP 503/403）**，NSW 条文以 **as-made 原文**核对，并确认 HRIP Act 现行版本日期为 2026-09-30；as-made 与现行文本之间的修订未逐字比对（见第 8 节）。所有原文只在本机临时目录阅读，**未下载进仓库**。

---

## 0. 一页结论

1. **三地"环境录音（ambient）"实际上都要求所有当事人同意。** NSW s7、ACT s4 明文禁止当事人在未获**每位 principal party** 同意时录音；VIC s6 虽允许当事人自己录，但 **s11 禁止在未获每位当事人（明示或默示）同意时"communicate or publish"录音记录或其报告**——而把录音转成护理记录、上传到 CareKind 服务器、交给其他员工阅读，正是"communicate"。✅ 原文；适用于产品【需律师确认】。→ DR-004"全国按最严标准取得全部当事人同意"在三地都站得住。
2. **护士单人口述（dictation）不属于"private conversation"。** NSW 定义为"words spoken by one person **to another person**"，ACT 为"conversation **between persons**"，VIC 为"conversation"。护士独自对设备口述不在定义内 → MVP 的 dictation 模式风险最低。✅ 原文；背景中意外录到他人对话的处理【需律师确认】。
3. **VIC HPP 9 与 NSW HPP 14 管的是"出州"，不只是"出境"。** VIC：转移给"outside Victoria"的人；NSW：转移给"in a jurisdiction outside New South Wales"的人**或 Commonwealth agency**。→ VIC 客户的数据存到悉尼机房，本身就是 HPP 9 意义上的"transborder"。"数据留在澳洲"不够，**合同必须让 CareKind 受 HPP 约束**（HPP 9.1(a)/(f)、HPP 14(a)/(g)）。✅
4. **CareKind 作为"非 health service provider"有法定删除义务。** VIC HPP 4.5、ACT Principle 4.3 cl 2：非 health service provider 在信息不再需要时**必须采取合理步骤销毁或永久去标识**；NSW HPP 5(1)(a)：保存时间不得超过必要期限。而 7 年 / 25 岁的保存义务（NSW s25、VIC HPP 4.2、ACT Principle 4.1）主要压在**provider** 身上。✅ 原文。**例外是 ACT**：Principle 4.1 cl 2 规定**任何 record keeper**"must keep, and must not destroy"health record，与 4.3 存在张力 → 原始音频能否短期删除【需律师确认】。
5. **ACT 的 HRPA Act 明确把"aged care service"列为 health service**（VIC HRA 同样明列），并把 **record keeper** 定义为"possession or control"health record 的任何实体 → CareKind 托管数据即为 record keeper。若数据**存放在 ACT 境内**（堪培拉机房），s11(3) 直接赋予当事人对 CareKind 的访问权。✅
6. **NSW 药品法 2026-11-05 换新法。** *Medicines, Poisons and Therapeutic Goods Act 2022* + *Regulation 2026* 取代 Poisons and Therapeutic Goods Act/Regulation：residential care facility 的 S8 drug register 责任人、季度盘点、**强制 Electronic Drug Register Standards**。✅ NSW Health 页面。→ CareKind **不得**被定位或配置成 drug register。
7. **VIC 自 2026-07-01 起：residential aged care 中的 S4/S8/S9 及 drugs of dependence 只能由护士（RN/EN）或其他注册卫生从业者给药**（宽限期到 2026-09-29）。例外须由 RN 记录（事件日期、简述、非护士给药期间）。✅ Vic DH 页面（2026-10-14 更新）。
8. **ACT 口头 health direction 有效，且有通报义务。** *Medical Treatment (Health Directions) Act 2006* s9：口头 direction 须由 2 名 health professional 同时见证（其中 1 名为医生或 nurse practitioner）；s13–14：任何人得知 residential care home（按 Aged Care Act 2024 定义）中的居民作出或撤销 direction，须告知 person in charge，并在档案中放入副本或记录。✅ → AI 草稿**不得替代**这一流程，只能忠实记录并提示护士按机构流程处理。
9. **ACT Crimes Act s36A–36C（虐待、未保护、忽视 vulnerable person）已核实**："relevant institution"的例子就是 nursing homes；s36B 对 person in authority 最高 5 年监禁。✅ → 护理记录可能成为证据，AI 不得弱化、遗漏或"润色"虐待/伤害相关陈述。
10. **联邦 Aged Care Act 2024 明文不排除州法**：s33（supporters 部分）和 s185 均写明"does not exclude or limit the operation of a law of a State or Territory that is capable of operating concurrently"；s28 承认州法下的 guardian 与 enduring power of attorney 可代本人行事。✅ → 三地州法与联邦框架**叠加适用**，而不是被联邦法取代。

---

## 1. 跨三地的共同问题

### 1.1 "private conversation"的定义与 dictation 模式 ✅

| 辖区 | 定义要点（原文） | 当事人本人录音 | 传播限制 |
|---|---|---|---|
| NSW SDA 2007 s4 | "any words spoken by one person to another person or to other persons" in circumstances indicating any of them desires the words to be listened to only by themselves (or with consent of all) | s7(1)(b) 禁止，除非 s7(3)：(a) **所有** principal parties 明示或默示同意；或 (b) 一位 principal party 同意且录音 (i) 为保护其 lawful interests 合理必要，或 (ii) **不是为了向非当事人传播** | s11：禁止传播**违反本 Part** 所得的对话/报告 |
| VIC SDA 1999 s3 | "conversation carried on in circumstances that may reasonably be taken to indicate that the parties to it desire it to be heard only by themselves"；**不含**当事人应合理预期会被他人听到的对话 | s6 只禁止**非当事人**录音（未获每位当事人明示或默示同意） | **s11：禁止 knowingly communicate or publish 由 listening device 直接或间接产生的私人对话记录或报告**（不论录音本身是否合法）；例外：每位当事人同意、为公共利益或保护自身 lawful interests"no more than reasonably necessary"、法律程序等 |
| ACT LDA 1992 dict. | "conversation between persons" in circumstances indicating any principal party desires it to be listened to only by themselves (or with consent of each principal party) | s4(1)(b) 禁止，除非 s4(3)：(a) **每位** principal party 同意；或 (b) 一位同意且 (i) 合理认为为保护其 lawful interests 所必需，或 (ii) 不为向非当事人传播 | s5：当事人传播录音记录亦属犯罪，除非向其他当事人、经每位 principal party 同意、法律程序、保护 lawful interests 等 |

**对 CareKind 的推论**（【需律师确认】）：
- 护士独自口述 → 没有"另一个人"，不构成 private conversation → 三地均不触发。
- 环境录音模式 → 录音的目的就是生成供他人阅读的护理记录（即"向非当事人传播"），NSW s7(3)(b)(ii)、ACT s4(3)(b)(ii) 的"一方同意 + 不传播"例外**用不上**；"保护 lawful interests"例外针对的是防御性录音，不适合常规文档。→ 只剩"每位 principal party 同意"。
- VIC：护士作为当事人可以录，但把记录交给机构系统、CareKind 和 AI 处理链属于 s11 的"communicate"→ 仍需每位当事人（明示或默示）同意。此外，CareKind 不是对话当事人，若被认定为"install, use or maintain" listening device，可能落入 s6。
- NSW s7(1) 的行为包括"install, use **or cause to be used** or maintain"→ 软件供应商不能以"录音的是护士"为由完全免责。
- NSW s7(2)(c)、ACT s4(2)(b) 的"unintentional hearing"例外只说 hearing，不明确覆盖**录音**。dictation 中意外录到背景对话的处理，【需律师确认】。

**罚则（原文）**：NSW（as-made）公司 500 penalty units；个人 100 penalty units 或 5 年监禁或两者并处。VIC 个人 240 penalty units 或 2 年监禁；body corporate 1200 penalty units。ACT s4 最高 50 penalty units；s5 为 50 penalty units 或 6 个月监禁或两者并处（ACT penalty unit：个人 $160 / 公司 $810，据 HRPA R32 republication 说明）。

**居家照护（Support at Home）特别风险**：在居民家中录音时，家属、访客更可能在场并成为 principal party；居民的家对上门员工也可能构成"workplace"（NSW Workplace Surveillance Act、ACT Workplace Privacy Act）【需律师确认】。

### 1.2 州健康记录法：三地对照（本次核实的增量）

| 项目 | NSW HRIP Act 2002 | VIC Health Records Act 2001 | ACT HRPA Act 1997 |
|---|---|---|---|
| 对 CareKind 的适用 | s11(1)：适用于"every organisation that is a health service provider **or that collects, holds or uses health information**" ✅ | s11(1)：适用于"is a health service provider **or collects, holds or uses health information**"的私营主体 ✅；s5：holds 指在其占有或控制下，"whether in or outside Victoria" ✅ | "record keeper"= 对 health record 有"possession or control"的实体 ✅；health record 包括"containing personal health information"的任何记录 ✅ |
| aged care 是否属 health service | 定义列 "nursing services" 等（as-made），未单列 aged care | **明列** "(b) a disability service, palliative care service **or aged care service**" ✅ | **明列** "(b) a disability, palliative care **or aged care service** that involves the making or keeping of personal health information" ✅ |
| 法定保存期 | s25：仅约束 **"private sector person who is a health service provider"**——成人自最后服务起 7 年；未成年至 25 岁；删除/转移须留记录 ✅ | HPP 4.2：health service provider 不得删除，除非 7 年 / 25 岁（取较晚者）；HPP 4.3 删除须书面记录 ✅ | Principle 4.1 cl 2：**record keeper**"must keep, and must not destroy"；cl 3 例外：7 年 / 25 岁、法律允许、按 Electronic Transactions Act 2001 s11(2)(b) 生成电子副本、监控录像 ✅ |
| 非 provider（CareKind）的删除义务 | HPP 5(1)(a)：不得超过合法用途所需时间 ✅ | **HPP 4.5**：非 health service provider 在不再需要时**必须**销毁或永久去标识 ✅ | **Principle 4.3 cl 2**：非 health service provider 在不再需要时**必须**销毁或永久去标识 ✅（与 4.1 cl 2 的张力见 §4.1） |
| 外包/交给服务商 | HPP 5(1)(d)：为接受服务而交给他人时，须尽力防止未授权使用或披露 ✅ | s12：仅针对 **State contract**（公立客户）下的 outsourced service provider ✅ | Principle 4.1 cl 1(b)：记录交给另一实体时，须尽力防止未授权使用或披露 ✅ |
| 出州/出境 | **HPP 14**：转移给"in a jurisdiction outside New South Wales"**或 Commonwealth agency**的人，须满足 (a)–(h) 之一 ✅ | **HPP 9**：转移给"outside Victoria"的人，须满足 (a)–(g) 之一 ✅ | 无专门 transborder 原则（全文检索无 overseas/outside ACT 条款）✅；但 **s21(2)**：为规避本法而把 health record 移出 ACT 属犯罪 ✅ |
| 访问期限 | 45 天（as-made Part 4 Div 3）✅ | s34(2)：45 天 ✅ | s13B：30 天（或付费后 1 周，取较晚者）✅ |
| 修改/更正 | HPP 8 ✅ | HPP 6.5–6.10 ✅ | Principle 7（附更正，不删除原记录）✅ |
| 投诉机构 | Privacy Commissioner（IPC）/ NCAT【未逐条核实】 | Health Complaints Commissioner ✅ | ACT Human Rights Commission（s18 "the commission"）✅ |

### 1.3 与联邦 Aged Care Act 2024 的交互（三地通用）✅

- **s33**（Part 4 Supporters）与 **s185**（Chapter 3 Part 5，provider duties 与 compensation 之前）均规定：该 Part"does not exclude or limit the operation of a law of a State or Territory that is capable of operating concurrently"。→ 州监护法、州健康记录法、州监听法与联邦义务**并行适用**。
- **s28**：只有 (a) 依联邦/州/领地法拥有监护权者、(b) 法院/审裁机构任命的决策者、(c) enduring power of attorney 持有人、(d) Rules 规定类别，才能代本人做 Act 下的事。**s29**：给本人的信息须同时给其 supporter；若 supporter 属于 s28(2) 所列人员，则**不论本人是否同意**都要给。→ 同意记录需区分"registered supporter（只支持）"和"州法下的替代决策人"。
- Aged Care Rules 的记录保存条款注明 provider 可能还须遵守州法的保存要求（FED §1.1）→ 三地 7 年 / 25 岁规则叠加。
- 各州法律跟进 2024 Act 的情况不一：ACT MTHD Act、ACT WWVP Act 已引用 *Aged Care Act 2024* ✅；VIC Safe Patient Care Act（v011，2025-04-09）仍引用 *Aged Care Act 1997* ✅（2025-11-01 之后如何衔接【未核实】）。
- Strengthened Quality Standards：Outcome 2.7（information management）、3.3（communicating for safety and quality）、5.3（safe and quality use of medicines）规定"要做到什么"；**州药品法和健康记录法规定"怎么记、保存多久、谁能签"**。产品需同时满足（FED §1.4）。

---

## 2. NSW

### 2.1 健康信息隐私：HRIP Act 2002（现行版本 2026-09-30 ✅；条文按 as-made 核对）
- CareKind **直接**受 HRIP 约束（s11），不仅是 provider 的承包商；无 small business 豁免（适用于"every organisation"）。
- 7 年保存义务（s25）在 provider 身上；CareKind 自身适用 HPP 5(1)(a)"不超过必要期限" + 合同。
- HPP 14 管辖范围包括**出州**和"Commonwealth agency"→ 如果 NSW 客户的数据经墨尔本或其他州的机房 / 子处理方处理，同样触发 HPP 14。
- 公共部门强制数据泄露通报（PPIP Act）不适用于私营方（STATE §1 已述）。

### 2.2 录音：Surveillance Devices Act 2007 ✅（as-made 原文）
- 见 §1.1。NSW 是三地中**唯一**把"cause to be used"写进录音罪行为要件的辖区，对软件供应商最不利。
- 护士在居民房间与居民交谈并录音 = 录制当事人参与的私人对话 → 需**所有 principal parties** 同意（居民、在场家属、其他员工）。
- 居民缺乏同意能力时，谁能代为同意录音：SDA 本身没有规定；"person responsible"只对 medical/dental treatment 有法定授权（§2.4）→ 由 guardian / enduring guardian 代同意录音是否有效【需律师确认】。

### 2.3 药物记录：2026-11-05 起换新法 ✅（NSW Health）
- *Poisons and Therapeutic Goods Act 1966* + *Regulation 2008* → **自 2026-11-05 起**由 *Medicines, Poisons and Therapeutic Goods Act 2022* + *Medicines, Poisons and Therapeutic Goods Regulation 2026* 取代。
- Residential care facility（RCF）主要变化：
	- RCF 的 **authorised person** 负责在场所内保存合规的 drug register；日常 S8 记录仍由执行操作的执业者完成，并须**见证和会签**；
	- S8 盘点**每 3 个月**一次（公立机构 6 个月），不再限定在 3 月和 9 月；
	- S8 销毁须在 DON 或经理面前进行，并记入 register；
	- 电子 S8 register 必须符合强制性的 **Electronic Drug Register Standards**（NSW Health 2026-09-08 发布，配套指南"即将发布"）；
	- 设有 medicines governance committee 的机构可批准任意 S2/3/4/8 作为 urgent use medicines，但须有书面方案指导 RN 的使用、储存、给药和**记录**；
	- RCF 须同时遵守联邦 *Guiding Principles for medication management in residential aged care facilities*。
- 罚则：个人 20–400 penalty units，公司 100–2000 penalty units（NSW Health 汇总）。
- 电子用药图表（eNRMC）：据检索摘要，NSW Chief Pharmacist 2026-05 的豁免文书允许试点机构使用经批准的电子用药图表，有效至 2028-05-31【未核实：未打开官方 PDF】。
- **对产品**：CareKind 只记录给药相关的观察和叙述，不做 drug register，不做 medication chart，不给剂量建议。产品与营销材料中不得出现"可替代 S8 register"之类表述（否则会落入 Electronic Drug Register Standards）。

### 2.4 监护与替代决策 ✅（NCAT fact sheet）
- *Guardianship Act 1987* 下 "person responsible" 的层级：(1) 有医疗/牙科决定权的 guardian 或 enduring guardian → (2) spouse / de facto / close continuing relationship → (3) **unpaid** carer（提供或安排居家支持）→ (4) relative or friend。上一层可书面放弃，由下一层接替。
- person responsible **不能**同意 special treatment（只能由 NCAT 决定），也不能同意本人反对的治疗。
- ACD 仍依普通法；改革尚停留在咨询/议会调查阶段：NSW Ageing and Disability Commission 2026-03 提交意见称"no progress made on necessary legislative reform"✅。
- 对 restrictive practices：按 STATE §4，先看州法有无 RPSDM 途径，没有再用联邦 Rules 的层级（STATE 已述，不重复）。

### 2.5 强制报告、员工筛查与州级监管
- 无一般性成人强制报告（RACF 内适用联邦 SIRS）；Ageing and Disability Commissioner 负责社区中的老人（STATE §5 已述）。
- 员工筛查：联邦规定为 police certificate（3 年内）或 NDIS Worker Screening Clearance；全国 aged care worker screening check 仍在与各州协商（health.gov.au 2026-03 指南摘要，"not before mid-2026"）。是否已启动【未核实】。
- *Public Health Act 2010* s104（nursing home 须随时有 RN 在岗）的现行定义，以及与 2024 Act 如何衔接：**仍【未核实】**（网站限流；检索未发现 2025–2026 修订）。
- **新增：*Work Health and Safety Amendment (Digital Work Systems) Act 2026***（2026-02-12 通过，二手）：PCBU 须在合理可行范围内确保工人健康安全不因 "digital work system"（algorithm、AI、automation、online platform）而受威胁；另有工作分配相关的新 s21A。开始日期由公告确定，且不早于 SafeWork NSW 发布指南后 1 个月【未核实】。→ aged care provider 引入 CareKind 可能属于引入 digital work system，provider 会要求我们提供 WHS 风险资料。
- *Workplace Surveillance Act 2005*：14 天书面通知（STATE §2 已述）。

### 2.6 NSW：对 CareKind 必须做的事
1. 默认 dictation；环境录音模式在 NSW 须取得**所有 principal parties** 的同意，并逐次可审计（DR-004）。
2. 合同明确 CareKind 受 HRIP / HPP 约束（满足 HPP 14(a)/(g)）；列明所有子处理方及其所在州。
3. 保存策略：最终记录以 provider 系统为准；CareKind 侧按 HPP 5(1)(a) 在不再需要时删除，并记录删除日志（provider 需履行 s25(2) 删除记录义务时我们可提供）。
4. 2026-11-05 前复核产品文案和功能，确保不构成 drug register / medication chart；草稿不得生成剂量或用药建议。
5. 准备 WHS digital work system 资料包（风险说明、人工审核 HITL、员工培训要点）。

---

## 3. VIC

### 3.1 健康信息隐私：Health Records Act 2001（v050，2026-05-01 生效）✅
- CareKind 直接受约束（s11）；holds 的认定不论文件位于 Victoria 内外（s5）。
- **HPP 9 管"outside Victoria"**：VIC 客户数据传到悉尼 = transborder → 须依 HPP 9.1(a)（接收方受与 HPP 实质相似的法律或合同约束；NSW HRIP 可能满足，但不应依赖）或 (f)（采取合理步骤）→ **合同中直接约定 CareKind 遵守 HPPs**。
- **HPP 4.5**：CareKind 作为非 health service provider，不再需要时必须销毁或去标识 → 支持"原始音频转写后尽快删除"。
- s12 外包条款只适用于 **State contract**（向 PSRACS 等公立机构销售时）。
- 访问请求 45 天内答复（s34(2)）；投诉由 Health Complaints Commissioner 处理。

### 3.2 录音：Surveillance Devices Act 1999（v048，2025-12-10）✅
- 见 §1.1。**纠正产品层面的误读**：VIC 不是"当事人可以随便录"的州——s11 禁止在未获每位当事人同意的情况下传播记录或报告。对文档产品来说，"传播"是必然的。
- body corporate 罚则 1200 penalty units。
- **Vic DH《Ambient AI Scribes Sector Advisory》（2025-05，文件 URL 为 2026-06）✅**（对象是 Victorian public health services，但很可能成为采购参照）：
	- "Explicit consent must be obtained from the consumer or authorised medical treatment decision maker … prior to using an AI scribe, and that consent must be recorded"，并须提供 opt-out；
	- 明确 SDA 1999 适用（"As these tools are used to record conversations"）；
	- "Health services must only use AI scribes that store and process data in Australia"；
	- 不属于医疗记录的 AI 产物应"discarded as soon as practicable"，保留期应写进供应商合同；
	- 用患者数据训练模型须另行取得知情同意；
	- 须 TGA 监管的工具不在该指引范围内。

### 3.3 药物记录 ✅（Vic DH）
- *Drugs, Poisons and Controlled Substances Regulations 2017*：registered residential aged care provider 对 S4/S8 须"maintain, and be able to retrieve, accurate and complete records of transactions"，包括给药记录；S8 imprest stock 须有 drug register；以标注给药时间的防拆封 dose-administration container 配发的 S8 不需要余额 register（Vic DH 页面，2026-07-07 更新）。
- **新：护士给药要求**（DPCS Act Part II Division 10A + Regulations Chapter 3C）：
	- **2026-07-01 生效**：只有 RN、EN 和其他注册卫生从业者可以给不自行服药的居民给 prescribed/dispensed drugs of dependence、S4、S8、S9；宽限期到 **2026-09-29**；
	- 不适用于居家照护、未列入 schedule 的药物和 S2/S3；
	- 例外：出现意外事件导致护士无法到位，且管理用药的 RN 判断"cannot wait"并委托非护士给药；**RN 须记录事件日期、事件简述以及非护士给药的期间** ✅（页面 2026-10-14 更新）。
- DPCS Regulations 2017 将于 **2027-05-16** 失效，除非重新制定；Vic DH 2026-03 已发布 sunset review 讨论稿（二手：AMA Vic 转载）。
- **对产品**：可以把"例外给药记录"作为**纯记录模板**的候选需求（只记录 RN 说了什么，不判断是否构成例外，也不建议委托）→ 先写 spec 再说，本文件不做设计决定。草稿中的给药者身份字段对 VIC 客户合规有意义。

### 3.4 监护与替代决策 ✅（Office of the Public Advocate）
- *Medical Treatment Planning and Decisions Act 2016* 下 medical treatment decision maker 的层级：(1) 本人任命的 MTDM → (2) VCAT 任命、有医疗决定权的 guardian → (3) 第一个合理可及、愿意且能够决定的亲近人：spouse/domestic partner → primary carer（**"not a paid service provider"**）→ adult child → parent → adult sibling；同一层级多人时由最年长者担任。
- 有涵盖该治疗的 ACD（instructional directive）时，执业者须遵照执行。
- 执业者须"reasonable efforts"查找 ACD（ANMF Vic 解读，二手）。
- → aged care 员工**不可能**以"primary carer"身份成为 MTDM。

### 3.5 州级 aged care 监管、员工筛查、工作场所
- **Safe Patient Care Act 2015**（v011，2025-04-09）✅：ratio 适用于"**aged high care residential ward**"——定义为由 *Aged Care Act 1997* 下 approved provider 运营、且在 **2014-06-30** 至少有一个 high care place 的病区；由 hospital operator 配置：早班每 7 名居民 1 名护士 **+ 1 名 nurse in charge**；午班 1:8 + in charge；夜班 1:15。in charge 的要求由 *Safe Patient Care Amendment Act 2025*（No. 12/2025）加入（页边注）。→ 适用范围是**公立 health service 名下的 aged high care 病区**，不是全部 PSRACS（纠错见第 7 节）。
- 工作场所监控：Premier 2026-07-20 宣布将立法（通知、协商、合法目的限制、对影响工人权利的重大自动化决定须人工复核、工人可访问自己的监控数据等）✅；尚无法案进入议会的证据，二手来源称与 2026-11 州选举有关【未核实】。
- 员工筛查：*Worker Screening Act 2020*（NDIS 筛查）细节【未核实】；联邦要求同 §2.5。
- Supported Residential Services（州监管、非联邦 aged care）是否为潜在客户以及适用哪些法规【未核实，本次未深入】。

### 3.6 VIC：对 CareKind 必须做的事
1. 环境录音模式：取得每位当事人**明示**同意（以 Vic DH advisory 为基准），记录同意，提供 opt-out；居民无能力时由 MTDM 或 guardian 代同意，并记录其依据【需律师确认】。
2. 合同写明 CareKind 遵守 HPPs（覆盖 HPP 9 出州），列明数据所在州。
3. 默认不使用居民数据训练模型；如需训练，另行取得知情同意（advisory + FED §1.3）。
4. 写入保留期条款：AI 中间产物（音频、转写、草稿版本）在工作流完成后尽快删除（HPP 4.5）。
5. 向公立客户（PSRACS）销售时，另加 PDPA/VPDSS、State contract（s12）条款（STATE §8 已述）。

---

## 4. ACT

### 4.1 健康信息隐私：HRPA Act 1997（R32，2025-11-16）✅
- **适用**：aged care service 明列为 health service；CareKind 作为 record keeper 受 privacy principles 约束（s5–6）。
- **保存与销毁的张力**（核心问题，【需律师确认】）：
	- Principle 4.1 cl 2：record keeper 必须保存、不得销毁 health record，即使记录被认为不准确；
	- cl 3 的例外：(b) 成人自最后服务起 7 年 / 未成年至 25 岁；(c) 已按 *Electronic Transactions Act 2001* s11(2)(b) 生成电子副本，且可合理预期日后可读；
	- Principle 4.3 cl 2：**非 health service provider** 在不再需要时必须销毁或永久去标识；
	- → CareKind 删除原始音频，是否可依 4.3 cl 2，或依 4.1 cl 3(c)（转写/最终记录是否算音频的"电子副本"存疑），需律师意见。在意见出来前，ACT 客户的原始音频默认保留策略应保守，至少可配置并支持 legal hold。
- **Principle 4.2**：record keeper 须保存**销毁或转移记录的登记册**（居民、记录涵盖期间、销毁日期或接收方），登记条目至少保存 7 年 → 产品需提供删除/转移日志导出。
- **s11(3)**：health record 保存或位于 ACT 时，record keeper 须允许当事人依法访问；s11(7)：合同排除该条款的部分无效。→ 若 CareKind 选用位于堪培拉的机房区域（部分云厂商的"Australia Central"区域位于堪培拉——以供应商文档为准【未核实】），则所有居民（不限 ACT 居民）都可能直接向 CareKind 行使访问权。
- **s21**：为规避本法而销毁或移出 ACT health record 属犯罪（50 penalty units 或 6 个月监禁）。
- **s26**：当事人"legally incompetent"时，权利由 guardian 行使；guardian 明知同意违背本人丧失能力前所表达且未撤回的意愿时，该同意**无效**。
- 访问 30 天（s13B）；投诉向 ACT Human Rights Commission 提出（s18）。

### 4.2 录音：Listening Devices Act 1992（R10，2022-02-11）✅
- 见 §1.1。s4(4)：Territory 使用设备时不适用 lawful interests 例外（与私营客户无关）。
- 2022 年以来无修订 → STATE 中关于 ACT"需各方同意"的结论**已由原文确认**。

### 4.3 药物记录：Medicines, Poisons and Therapeutic Goods Regulation 2008（R57，2025-12-26）✅
- s351(1)(a)：按 standing order 给机构内患者用药，须记入患者 **medical records**（字典定义：institution 中患者的 medical records 包括其 clinical records 和 **medication chart**）。
- s351(1)(b)：controlled medicine（S8）须由规定的见证人见证，并同时记入 medical records 和 controlled medicines register；s351(2)：RACF 中以 dose administration aid 配发的不适用。
- s543：controlled medicines register 的必填字段（交易性质、日期、药品/剂型/强度/数量、供应方等、交易后余量）。
- **s361**：assistant（如护理员）可协助给药，但若居民属"person under a legal disability"（含因身体、精神、心理或智力状况导致决策能力受损），须**经其 parent 或 guardian 授权** → 与 §4.4 的同意记录直接相关。
- → 产品只做叙述性记录，不做 register；草稿不得生成用药建议。

### 4.4 监护与替代决策 ✅
- *Guardianship and Management of Property Act 1991*（R50，2025-12-16）s32B：health attorney 优先顺序为 domestic partner → carer → close relative or close friend；s32C(2)：居民住在 nursing home 等场所时，在该场所提供照护的人**不因此成为 carer**。
- *Medical Treatment (Health Directions) Act 2006*（R4，2026-09-05，经 *Nurse Practitioners Legislation Amendment Act 2026* 修订）：
	- s9：**非书面（口头）health direction** 须由 2 名 health professional 同时在场见证，其中至少 1 名为医生或 **nurse practitioner**；
	- s13：health professional "**or someone else**" 得知 health care facility（含 Aged Care Act 2024 定义的 residential care home）中的患者作出或撤销 direction，须告知 person in charge；
	- s14：person in charge 须合理确保副本或记录放入患者档案。
- → **产品影响**：录音或口述中出现居民拒绝治疗、临终意愿等内容时，AI 草稿必须原样、忠实记录，并提示护士按机构流程处理（s13 通报）。AI **不得**判断它是否构成有效 health direction（这是法律判断，也接近临床决策边界）。

### 4.5 强制报告 / 刑事责任 ✅
- *Crimes Act 1900*（R155，2026-02-23）：
	- **s36A** 虐待 vulnerable person（abuse 的定义包括"deprive or restrict the vulnerable person's freedom of action"且非安全照护所合理必需——与 restrictive practices 相关）；
	- **s36B** person in authority 未保护：relevant institution 定义的例子是"religious organisations, hospitals, **nursing homes**"以及"a group of nursing homes"；最高 5 年监禁；适用于公司（Legislation Act s161）；
	- **s36C** 忽视；
	- vulnerable person：有残障的成人，或 ≥ 60 岁且有影响思维的疾病、导致沟通/学习/行动能力显著下降的损伤、或社会孤立者。
- 生效日期 2021-04-21（二手）。
- → 护理记录可能被用作证明"知道风险"或"已采取措施"的证据。AI 草稿必须保留关于伤害、虐待、约束的原始陈述，不得概括、弱化或省略。

### 4.6 员工筛查、工作场所、其他
- *Working with Vulnerable People (Background Checking) Act 2011*（R28，2026-02-23）s12：**registered provider under the Aged Care Act 2024 的员工或志愿者**不需要 WWVP 注册 ✅。CareKind 员工不是 provider 的员工；远程软件支持是否属于 Schedule 1 的"regulated activity"【需律师确认，初判不属于】。
- *Workplace Privacy Act 2011*（R6）✅：适用于 data / optical / tracking surveillance device（**不含**音频）；s13 须至少提前 14 天书面通知；s14 须与工人协商。
- *Senior Practitioner Act 2018*（R7）✅：provider 定义为 education、disability、care and protection of children 以及 regulation 规定的服务——**不含 aged care**（除非 regulation 另行规定【未核实】）。→ ACT aged care 的 restrictive practices 仍走联邦框架 + 州监护法。

### 4.7 ACT：对 CareKind 必须做的事
1. 环境录音：取得**每位** principal party 同意（s4(3)(a)）。
2. 保存策略：在律师意见出来前，ACT 客户的原始音频不做"自动短期删除"，或仅在 provider 书面确认后删除；产品提供 Principle 4.2 删除/转移登记册导出。
3. 机房选址：评估是否放在 ACT（s11(3) 访问义务）；无论放在哪里，都不得为规避而转移记录（s21）。
4. 同意记录区分本人、guardian、health attorney；若 guardian 的同意违背本人先前意愿，按 s26(2) 无效 → 同意记录需留有"本人先前意愿"备注字段（产品需求候选）。
5. 草稿规则：health direction 和虐待相关内容须忠实记录并提示人工处理。

---

## 5. 所需 paperwork 汇总（草稿清单，均需律师审阅）

| 文件 | NSW | VIC | ACT | 说明 |
|---|---|---|---|---|
| 居民/代理人**录音同意书**（ambient 模式） | 必需：所有 principal parties | 必需：每位当事人明示同意 + opt-out（Vic DH advisory） | 必需：每位 principal party | 附代理人身份与法律依据（person responsible / MTDM / guardian / health attorney / EPOA） |
| 家属/访客现场告知与同意脚本 | 必需 | 必需 | 必需 | 居家照护尤其重要 |
| 员工使用告知 + 工作场所监控通知 | Workplace Surveillance Act：14 天 | 目前无专法；关注 2026 立法 | Workplace Privacy Act：14 天 + 协商 | 若使用日志被用于监控员工 |
| **DPA / 服务合同隐私条款** | CareKind 受 HRIP/HPP 约束（HPP 14(a)/(g)）；子处理方及其所在州 | CareKind 受 HPP 约束（HPP 9.1(a)/(f)）；保留期与删除（HPP 4.5）；禁止用于训练 | 遵守 privacy principles；Principle 4.1(1)(b)；s11 访问；删除登记册 | 与联邦 s168 / APP 条款合并 |
| 保留与删除时间表（retention schedule） | provider 7 年 / 25 岁；CareKind 按必要期限 | 同左；AI 产物尽快删除 | 原始音频删除需律师意见 | 写入合同附件 |
| 删除/转移登记册（产品导出） | s25(2)–(3)（provider） | HPP 4.3–4.4（provider） | Principle 4.2（record keeper，含 CareKind） | |
| WHS digital work system 资料包 | 新法生效后需要 | — | — | 二手来源，待生效日期确认 |
| 药品相关免责声明 | 不是 drug register / eNRMC | 不判断例外给药，只记录 | 不是 controlled medicines register | 写入产品说明与营销合规 |
| 隐私政策 / 收集通知中的州法条款 | HRIP | HRA | HRPA | 投诉渠道：IPC / HCC / ACT HRC |

---

## 6. 对 CareKind 产品影响总表

| 主题 | NSW | VIC | ACT | 产品默认值建议 |
|---|---|---|---|---|
| 单人口述 | 不触发 SDA | 不触发 | 不触发 | MVP 默认 |
| 环境录音 | 全体同意 | 实质上全体同意（s11） | 全体同意 | 机构开启 + 逐次同意 + 可停止（DR-004） |
| 出州数据流 | HPP 14 | HPP 9 | 无（但 s21） | 合同约束 + 子处理方清单 |
| CareKind 删除义务 | HPP 5(1)(a) | HPP 4.5 | 4.3 vs 4.1 张力 | 可配置；ACT 保守 |
| 药品 | 新法 2026-11-05 | 护士给药 2026-07-01 | 记入 medical records / register | 只记录，不建议，不做 register |
| 替代决策 | person responsible | MTDM | health attorney / guardian | 同意记录写明身份与依据 |
| 刑事/强制报告 | SIRS（联邦） | SIRS（联邦） | Crimes Act s36A–C + SIRS | 草稿忠实、不弱化 |

---

## 7. 与 state-by-state-comparison.md 的差异 / 纠错建议

> 只提建议，**未修改** STATE。是否采纳由 Terry 决定。

1. **§2 表格 VIC 行**："✅ 当事人可录"在法律上正确，但应补充：s11 禁止在未获每位当事人同意时传播记录或报告；s6 的"install, use or maintain"可能覆盖非当事人的软件供应商。建议在 §10 第 1 点把 VIC 从"当事人可录但限制传播"改为"**对文档产品而言实际上需要每位当事人同意**"。
2. **§2 表格 NSW / ACT 行的"主要例外"**：只写了 lawful interests，**漏了第二个例外**——"一方同意且录音不是为了向非当事人传播"（NSW s7(3)(b)(ii)、ACT s4(3)(b)(ii)）。建议补上，并注明该例外不适用于文档产品。
3. **§2 底部 ⚠️ 注释**（"二手资料互相矛盾，须律师逐州确认"）：NSW（as-made）、VIC（v048）、ACT（R10）三地已对照原文核实，建议把这三行改为 ✅，只保留"对产品的适用【需律师确认】"。
4. **§1 跨境列与 §10 第 4 点**：NSW HPP 14 和 VIC HPP 9 管的是**出州**（NSW 还包括 Commonwealth agency），不只是出境。§10 第 4 点暗示"托管在澳洲境内"即可满足，建议改为"澳洲境内托管 + 合同约束 CareKind 遵守对应州 HPP"。
5. **§1 ACT 跨境列"—"**：结论正确，建议补充 s21(2)（为规避而移出 ACT 属犯罪）和 s11(3)（记录位于 ACT 即产生访问义务）。
6. **§6 记录保存 NSW 行**：s25 只约束"private sector person **who is a health service provider**"，CareKind 不在其列；建议在 §10 第 5 点补充：CareKind 适用 NSW HPP 5(1)(a)、VIC **HPP 4.5**、ACT **Principle 4.3 cl 2**（非 provider 须删除或去标识），但 ACT Principle 4.1 cl 2 对所有 record keeper 设"不得销毁"义务，二者有张力。
7. **§6 ACT 行**"不得更改/销毁记录（可附更正）"：建议细化为 Principle 4.1 cl 2–3（含电子副本例外、7 年 / 25 岁例外）+ **Principle 4.2 销毁/转移登记册**（保存 7 年）。
8. **§3 VIC 行**：Safe Patient Care Act 的 ratio 适用于公立 hospital operator 名下的"**aged high care residential ward**"（以 Aged Care Act 1997 和 2014-06-30 的 high care place 定义），不等于全部 PSRACS。"Safe Patient Care Amendment Bill 2025 状态待核"可以更新为：已成为 *Amendment Act 2025*（No. 12/2025），早班、午班加入 nurse in charge。定义仍引用 1997 Act，2025-11-01 后如何衔接【未核实】。
9. **§4 表格**：建议补充——ACT 口头 health direction 的见证要求（s9）和 residential care home 的通报/存档义务（s13–14）；NSW "carer" 须为 unpaid；VIC primary carer 须"not a paid service provider"；ACT s32C(2) 机构员工不是 carer。→ aged care 员工在三地都不能当默认替代决策人。
10. **§5 ACT 行**："⚠️ 对有权责者有保护义务，需核实具体适用"可改为 ✅：s36A–36C 原文已核实，relevant institution 的例子明确包括 nursing homes，s36B 最高 5 年。
11. **§5 员工筛查**：建议补充 ACT WWVP Act s12——registered provider（Aged Care Act 2024）的员工和志愿者无需注册。
12. **缺少药品法维度**：STATE 未覆盖州药品法。建议新增一节或引用本文件：NSW 新法 2026-11-05 生效；VIC 护士给药要求 2026-07-01 生效；ACT MPTG Regulation s351/s361/s543。
13. **§2 工作场所监控**：VIC 部分可补充 Premier 2026-07-20 的立法宣布；NSW 可补充 *WHS Amendment (Digital Work Systems) Act 2026*（二手，开始日期未定）。
14. **§9 NSW** 中"Public Health Act 2010 s104 ⚠️ 现行定义待核"：本次仍未能核实，维持 ⚠️。
15. 建议在 [legal-reference-index.md](../../11-rules/legal-reference-index.md) "按州查找"中为 NSW / VIC / ACT 增加本文件入口，并在"录音"和"记录保存期限"话题中引用 §1.1、§1.2（需 Terry 批准后再改）。

---

## 8. 未核实项列表

| # | 事项 | 原因 / 下一步 |
|---|---|---|
| U-1 | NSW SDA 2007、HRIP Act 2002 的**现行**文本是否与 as-made 在 s7、s11、s25、HPP 5、HPP 14 上一致 | NSW 网站限流；下次在非高峰时段核对 current version（HRIP 现行版本 2026-09-30） |
| U-2 | NSW Public Health Act 2010 s104 现行定义，及与 Aged Care Act 2024 的衔接 | 同上 |
| U-3 | NSW HRIP 私营方投诉路径（Privacy Commissioner → NCAT）的具体条款 | 未逐条核对 |
| U-4 | NSW Electronic Drug Register Standards 的具体条款与开始日期；eNRMC 豁免文书（至 2028-05-31） | 只读到 NSW Health 网页摘要，未打开 PDF |
| U-5 | NSW *WHS Amendment (Digital Work Systems) Act 2026* 的开始日期与最终文本 | 只有二手来源 |
| U-6 | 全国 aged care worker screening check 是否已启动（2026-10） | health.gov.au 指南抓取超时；检索摘要称"not before mid-2026" |
| U-7 | VIC DPCS Regulations 2017 sunset（2027-05-16）及重新制定进展 | 二手（AMA Vic 转载 Vic DH 讨论稿） |
| U-8 | VIC Safe Patient Care Act "aged high care residential ward" 定义在 2025-11-01 后如何衔接 | v011 早于 2024 Act 生效；需查是否有后续修订 |
| U-9 | VIC 工作场所监控立法是否已有法案、时间表 | 仅有 2026-07-20 宣布；选举相关信息为二手 |
| U-10 | VIC Worker Screening Act 2020 对 aged care 的适用细节；Supported Residential Services 的法规框架 | 本次未深入 |
| U-11 | ACT Senior Practitioner Regulation 是否把 aged care 规定为"service" | 未查 regulation |
| U-12 | 堪培拉机房区域的具体云服务商与区域名称 | 以供应商文档为准 |
| U-13 | ACT Crimes Act s36A–36C 的生效日期（2021-04-21） | 二手；条文本身已核实 |
| U-14 | 三地均未找到州卫生部门针对 aged care / 私营机构的 AI scribe 专门指引（NSW 未检索到；VIC 指引只针对公立 health services） | 持续关注 |

**需律师确认的解释性问题（原文已核实）**：L-1 软件供应商是否构成 NSW s7 "cause to be used" / VIC s6 "install, use or maintain"；L-2 VIC s11 "communicate" 是否覆盖向 CareKind 服务器和 AI 子处理方传输；L-3 dictation 中意外录到背景对话的处理；L-4 居民无能力时由谁代为同意录音（SDA 本身没有规定）；L-5 ACT Principle 4.1 cl 2 与 4.3 cl 2 对 CareKind 原始音频的适用；L-6 CareKind 是否属 VIC/ACT 意义上的"health service provider"（我们只做文档，初判不是）；L-7 HRIP/HRA 对位于 NSW 的 CareKind 处理 VIC/ACT 居民数据的域外适用。

---

## 9. 来源（Sources，均于 2026-10-19 访问）

**NSW**
- Surveillance Devices Act 2007（as-made PDF）：https://legislation.nsw.gov.au/view/pdf/asmade/act-2007-64 ；现行版本入口：https://legislation.nsw.gov.au/view/html/inforce/current/act-2007-064
- Health Records and Information Privacy Act 2002（as-made PDF）：https://legislation.nsw.gov.au/view/pdf/asmade/act-2002-71 ；现行版本（2026-09-30）：https://legislation.nsw.gov.au/view/html/inforce/current/act-2002-071
- NSW Health – Legislation changes for healthcare settings（MPTG Act 2022 / Regulation 2026，2026-11-05）：https://www.health.nsw.gov.au/pharmaceutical/Pages/changes-for-healthcare-settings.aspx
- NSW Health – Electronic Drug Register Standards：https://www.health.nsw.gov.au/pharmaceutical/Pages/electronic-register-standards.aspx
- NSW Health – Residential care facilities：https://www.health.nsw.gov.au/pharmaceutical/Pages/residential-care-facilities.aspx
- NCAT – Person responsible fact sheet：https://ncat.nsw.gov.au/publications-and-resources/fact-sheets/person-responsible-fact-sheet.html
- NSW Ageing and Disability Commission，supported decision-making inquiry 提交意见（2026-03）：https://ageingdisabilitycommission.nsw.gov.au/documents/submissions/NSW_Ageing_and_Disability_Commission_submission_to_Inquiry_into_supported_decision-making_in_NSW_-_March_2026.pdf
- WHS Amendment (Digital Work Systems) Bill 2026（二手解读）：https://www.mallesons.com/au/en/insights/latest-thinking/new-ai-related-changes-to-nsw-work-health-and-safety-laws ；https://hamiltonlocke.com.au/nsw-parliament-passes-whs-digital-work-system-duty/ ；议会文本：https://www.parliament.nsw.gov.au/bill/files/18847/Second%20Print.pdf

**VIC**
- Surveillance Devices Act 1999 v048（authorised PDF）：https://content.legislation.vic.gov.au/sites/default/files/2025-12/99-21aa048-authorised.pdf
- Health Records Act 2001 v050（authorised PDF）：https://content.legislation.vic.gov.au/sites/default/files/2026-04/01-2aa050-authorised.pdf
- Safe Patient Care Act 2015 v011（authorised PDF）：https://content.legislation.vic.gov.au/sites/default/files/2025-04/15-51aa011-authorised.pdf
- Safe Patient Care Amendment Act 2025（as-made）：https://www.legislation.vic.gov.au/as-made/acts/safe-patient-care-nurse-patient-and-midwife-patient-ratios-amendment-act-2025
- Vic DH – Medication administration in residential aged care：https://health.vic.gov.au/drugs-and-poisons/medication-administration-in-residential-aged-care
- Vic DH – Residential aged care: medicine storage and record keeping：https://www.health.vic.gov.au/drugs-and-poisons/residential-aged-care-medicine-storage-and-record-keeping
- Vic DH – Ambient AI Scribes Sector Advisory：https://www.health.vic.gov.au/sites/default/files/2026-06/ambient-ai-scribes-advisory.docx
- Office of the Public Advocate – Medical treatment decision makers：https://www.publicadvocate.vic.gov.au/medical-treatment/medical-treatment-decision-makers
- Vic DH – Medical Treatment Planning and Decisions Act 2016：https://www.health.vic.gov.au/patient-care/medical-treatment-planning-and-decisions-act-2016
- Premier of Victoria，"Big Tech Must Stop Spying On Workers At Work"（2026-07-20）：https://www.premier.vic.gov.au/site-4/big-tech-must-stop-spying-workers-work
- DPCS Regulations sunset review 讨论稿（二手转载）：https://amavic.com.au/media/l31jy5ds/amavic_discussion_paper_for_consultation_dpcs_regulatory_review_march_2026.pdf

**ACT**
- Listening Devices Act 1992 R10：https://www.legislation.act.gov.au/a/1992-57/ （PDF：https://www.legislation.act.gov.au/DownloadFile/a/1992-57/current/PDF/1992-57.PDF）
- Health Records (Privacy and Access) Act 1997 R32：https://www.legislation.act.gov.au/a/1997-125/ （PDF：https://www.legislation.act.gov.au/DownloadFile/a/1997-125/current/PDF/1997-125.PDF）
- Medicines, Poisons and Therapeutic Goods Regulation 2008 R57：https://www.legislation.act.gov.au/DownloadFile/sl/2008-42/current/PDF/2008-42.PDF
- Guardianship and Management of Property Act 1991 R50：https://www.legislation.act.gov.au/DownloadFile/a/1991-62/current/PDF/1991-62.PDF
- Medical Treatment (Health Directions) Act 2006 R4：https://www.legislation.act.gov.au/DownloadFile/a/2006-51/current/PDF/2006-51.PDF
- Crimes Act 1900 R155（s36A–36C）：https://www.legislation.act.gov.au/DownloadFile/a/1900-40/current/PDF/1900-40.PDF
- Working with Vulnerable People (Background Checking) Act 2011 R28：https://www.legislation.act.gov.au/DownloadFile/a/2011-44/current/PDF/2011-44.PDF
- Workplace Privacy Act 2011 R6：https://www.legislation.act.gov.au/DownloadFile/a/2011-4/current/PDF/2011-4.PDF
- Senior Practitioner Act 2018 R7：https://www.legislation.act.gov.au/DownloadFile/a/2018-27/current/PDF/2018-27.PDF

**联邦（交互部分）**
- Aged Care Act 2024（compilation 2025-11-01，s28、s29、s33、s185）：https://www.legislation.gov.au/C2024A00104/2025-11-01/2025-11-01/text/original/epub/OEBPS/document_1/document_1.html ；最新版本：https://www.legislation.gov.au/C2024A00104/latest/text
- Aged care worker screening guidance（2026-03）：https://www.health.gov.au/sites/default/files/2026-03/aged-care-worker-screening-guidance-material_0.pdf
