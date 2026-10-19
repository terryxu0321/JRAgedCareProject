# 竞争对手如何解决"aged care 护理文档负担 + 合规"（How Competitors Solve It）

> 研究日期：2026-10-19｜研究员：AI 竞品研究（内部工作稿，**非法律意见**）｜在 2026-10-10 研究（[README](README.md)、[competitor-matrix](competitor-matrix.md)、[au-care-management-systems](au-care-management-systems.md)、[ai-scribes-and-ai-startups](ai-scribes-and-ai-startups.md)、[sources](sources.md)）基础上做**解决方案剖析**，并补充 2026-10-10 之后核查到的新动态。
>
> 规则：只写可核实事实，正文方括号编号 [Nx] 对应文末"来源"表（含 URL 与核查日期）；沿用旧研究的事实标 [旧 Ax/Bx/Cx/Dx]，编号见 [sources.md](sources.md)（核查日期 2026-10-10）。厂商数字均为 vendor claim。**【未核实】**= 仅搜索摘要、付费墙或页面未能打开。"未公开"= 公开渠道未找到。竞品原话若含 detects/predicts 等词，仅作引用，不代表我们可用此措辞。

## 0. 自 2026-10-10 以来的新发现（最重要的 8 条）

1. **TGA 数字 scribe 审查结果（2026-10-16）：12 款中 8 款"可能属于医疗器械"**，被审产品包括 Heidi、Lyrebird、Microsoft Dragon Medical One 等，TGA 未点名是哪 8 款；问题集中在"分析临床信息、给出发现/结论/建议"的生成式功能；**"声明或免责条款不足以决定是否为医疗器械"** [N1]。TGA 官方页面本次抓取超时 [N2]【官方原文未直接打开】。→ 行业"贴一句 not a medical device"的做法已被明确否定。
2. **voize（柏林）是最接近 CareKind 核心机制的海外玩家**：护理人员对手机说话，官网称 voize "reliably recognizes residents and assigns documentation to the right person"，并结构化到生命体征、液体摄入、护理报告等表单；离线可用、人始终在环、与 MEDIFOX DAN、Connext Vivendi、Dedalus ORBIS U 集成；自称 2,000+ 机构 [N3]；2025-11 获 US$50M Series A（Balderton 领投），计划进入美国 [N4]。**未找到澳洲业务。** → CareKind"按居民自动归属"不是全球首创，需以澳洲合规 + 多语言 + 澳洲 CMS 回写取胜。
3. **PointClickCare 的 Ambient Scribe Services 由 Nabla 提供**（2026-03 合同附件）：**录音同意完全由客户负责**（"PointClickCare shall have no responsibility to obtain such consents"），音频/转写可被用于"tune, enhance and improve"语音识别（去标识化后可在合同终止后继续使用），且"will not maintain any audit logs" [N5]。→ 典型的"把合规风险推给机构"模式，也是 CareKind 可反向差异化之处。
4. **Telstra Health 已有自研 AI scribe——但只用于 GP**：Smart Scribe（2025-02-26）内嵌于 MedicalDirector Clinical，每次使用提示确认患者同意、录音转写后删除、存于澳洲数据中心 [N6]。2026-05 Telstra Health 将 Kyra Flow 医院产品出售给 Alcidion，并称在建设覆盖"primary, community and aged care"的 **"care intelligence ecosystem"** 与"AI-powered workflows" [N7]。→ 能力与意图都已具备，移植到 Clinical Manager（aged care）只是时间问题。**截至 2026-10-19 仍未找到 Clinical Manager 内置 AI notes** [N8]。
5. **澳洲新的直接小型对手 Notive（阿德莱德）**：护理员"speak your shift"→ 按 mood/nutrition/skin/mobility 分节的交班记录；音频转写后立即删除；数据存悉尼；签署后锁定只能追加 addendum；7 天试用、价格按机构规模商议；正在 SA/VIC 招募"founding facilities"；无集成、无认证、无具名客户 [N9]。
6. **大型 provider 自建继续增加**：Regis（72 家院舍）用 Microsoft Copilot Studio + Foundry 与 Cognizant 自建 **RegiCare Assist**，汇总 progress notes 与 24 小时报告、按临床类别归类，约 150 名员工使用，计划与其护理系统集成；Regis CNO 表示尚无法判断对临床治理的效果 [N10]。Uniting 的 AI 平台"now used by other providers"（2026-07-24，付费墙）[N11]【未核实细节】。
7. **Heidi 已公开安全认证**：support/区域页面称持有 ISO 27001、ISO 42001、SOC 2 Type 2（部分区域另列 Cyber Essentials Plus 或 ISO 9001，各页不一致）[N12][N13]；ANZ 数据"locally hosted within Australia"、音频生成 note 后删除 [N14]。Lookout Assist 发布文把 Heidi 列为可与 Assist 协同的临床文档工具 [N15]（**未见正式集成公告**）。
8. **Aged Care Act 2024 已于 2025-11-01 生效**：卫生部的数字准备清单要求 provider 与软件厂商沟通 API 报告/申报方案，并确认"my systems have been updated to align to the new Act" [N16][N17]。本次**未找到任何 CMS 厂商专门针对新法发布 AI 文档功能**的公告——各厂商的新法工作集中在 Support at Home 申报 API（如 AlayaCare、Lookout）[旧 A25][N18]。

## 1. 问题拆解：护理文档负担 + 合规由哪些子问题构成

| 痛点 | 法定/合规来源（内部理解，见 PRD F0） | 现有解决方式（行业） |
|---|---|---|
| Progress notes（每班、每位居民） | Strengthened Quality Standards Outcome 2.7（准确及时）[PRD A1] | 点选图标（PCS）、模板表单（多数 CMS）、语音听写 + AI 改写（ShiftCare、Notive、AccuNote）、ambient（Heidi、PCC Vox、voize） |
| Incident / SIRS | 事件记录法定字段、SIRS 24 小时/30 天 [PRD A1] | CMS 内事件表单；Heidi 起草 incident report [旧 B1]；ShiftCare Care Signals 在 note 中标记潜在事件（美国版）[N19]；Notive"incident flags" [N9] |
| Handover | Outcome 2.7 / 交接连续性 | Notive 交班 note [N9]；Lookout handover 摘要 [N15]；Regis 汇总 24 小时报告 [N10] |
| Care plan / 复审 | 新法下的护理计划要求 | Lookout 从外部临床文档生成 care plan [N15]；AlayaFlow"Recommended Care Plans" [旧 A21]；Birdie SmartPlans [旧 C7] |
| AN-ACC 资金证据 | AN-ACC 评估 | Telstra Clinical Manager 可把临床文档标记为 AN-ACC 证据、提醒重评 [N20]；Mirus 曾试点 AI 辅助 AN-ACC 流程（2024）[N21]——**未找到用生成式 AI 写 AN-ACC 证据的上线产品**（且对外宣称"提升资助"违反我们的 O-4.3） |
| 质量指标 QI | National Aged Care Mandatory QI Program | 多为 CMS 报表与 benchmarking（Mirus、MOA/Evaran）[旧 A31][旧 A16]；**未找到 AI 文档产品直接产出 QI** |

## 2. 解决方案剖析

> 每个竞品按六点：①痛点 ②交互方式 ③合规做法（同意/驻留/HITL/TGA/认证）④CMS 集成 ⑤定价（仅公开）⑥优点·短板·对 CareKind 启示。

### A. 澳洲护理管理系统（CMS）

#### A1. Telstra Health（Clinical Manager / CareKeeper；前身 iCare）

| # | 内容 |
|---|---|
| ① | Residential 全流程记录、eMAR、AN-ACC 证据标记与重评提醒 [N20]；与 RMIT 合作的 NLP 风险分析研究以 progress notes 为数据源 [旧 A5] |
| ② | 移动端点选/键入（CareKeeper）；**aged care 产品未见语音/AI 草稿** [N8]。GP 侧 Smart Scribe 为 ambient 问诊录音 [N6] |
| ③ | Smart Scribe：每次使用提示确认患者同意、录音转写后删除、澳洲数据中心、GP 审核编辑后保存 [N6]。Aged care 产品的驻留/认证声明：未找到 |
| ④ | 本身即 system of record；Clinical Manager 对接 My Health Record（第三方汇总）【未核实】 |
| ⑤ | 未公开；Smart Scribe 提供分层方案与 30 天试用 [N6] |
| ⑥ | **优点**：装机量（自称 60,000+ beds [旧 A3]）、已有本土 scribe 技术与同意/驻留设计。**短板**：aged care 端尚无 AI 记录。**启示**：最大"内置"威胁；CareKind 的集成与合作窗口取决于 Telstra 是否把 Smart Scribe 移植到 aged care——应尽早争取成为其生态伙伴，而不是与之正面比"会转写" |

#### A2. Leecare（Platinum6）

| # | 内容 |
|---|---|
| ① | Residential 为主的全流程系统 [旧 A7] |
| ② | 浏览器端表单；曾与 Voice-Care 做语音合作（英国试点，日期不明）[旧 A9]；本次检索**未找到 2026 年 AI 新功能** [N22] |
| ③ | 驻留/认证：未明示 |
| ④ | 有嵌入第三方（CAREFUL）先例 [旧 A8] |
| ⑤ | 未公开 |
| ⑥ | **启示**：开放合作的先例使其仍是首选集成伙伴；无 AI 新动态 = 窗口仍在 |

#### A3. AutumnCare（OneTouch Health）

| # | 内容 |
|---|---|
| ① | 结构化临床记录、护理计划、评估、给药（Anglicare SQ 案例）[N23] |
| ② | 移动端床旁评估表单 [N23]；**未找到 AI/语音功能** [N23] |
| ③④⑤ | 未明示 / 未公开 |
| ⑥ | **启示**：PE 背景的英爱母公司可能从英国引入 AI（英国同行 Access、Nourish 已有语音记录）[旧 C8–C10]；短期是集成目标 |

#### A4. Person Centred Software（PCS）

| # | 内容 |
|---|---|
| ① | 日常护理记录（ADL 事件化）[旧 A14] |
| ② | **icon-driven 点选**：点图标预填 note 再扩写；第三方称全球每日 900 万+ care notes [N24]【未核实】。2026 年未找到 AI 语音 notes 发布 [N24] |
| ③ | 未明示 |
| ④ | 自有平台；2026-06 收购 Camascope（给药）[旧 A15] |
| ⑤ | 未公开 |
| ⑥ | **启示**：点选范式把"结构化"做到极致但不擅长叙述性/事件型记录；CareKind 语音 + 归属可作为其补充层，而非替代 |

#### A5. Evaran（eCase / MOA / CareLineLive / Checked In Care）

| # | 内容 |
|---|---|
| ①② | eCase 覆盖 residential/home/disability；**未找到 AI 记录功能** [旧 A16][N25] |
| ③④⑤ | 未明示 / 自有平台 / 未公开 |
| ⑥ | **启示**：PE 整合平台更可能"买"AI 而不是自研——CareKind 的集成资产与合规设计也可能是被收购价值 |

#### A6. AlayaCare（Support at Home）

| # | 内容 |
|---|---|
| ① | Home care 表单、care plan 推荐、排班、visit 验证 [旧 A20–A22] |
| ② | AI Form Assistant：语音听写→结构化表单，审核后批准 [旧 A20]；Layla 对话助手；AlayaFlow agents [旧 A21] |
| ③ | 声称遵守 Privacy Act、SOC 2 Type II、HITRUST、每个 AI 动作需人工批准；**未写明托管地点** [旧 A19]。录音同意：听写模式（护理员对设备说话）未见专门同意流程 |
| ④ | 自身即 CMS；2025-10 宣布收购 Nightingale Software [N18] |
| ⑤ | 未公开 |
| ⑥ | **启示**："听写→表单 + 人工批准"已是 home care 标配；我们 H1 不进 home care 的决定仍成立 |

#### A7. Lookout（The Lookout Way）

| # | 内容 |
|---|---|
| ① | Care plan（基于外部临床文档）、临床摘要、handover 摘要、可用性采集 [N15] |
| ② | 嵌入工作流的任务型 agents；多语言（可用性采集支持最多 10 种语言）[N15] |
| ③ | "A human is always present to direct and intervene"；锁定提示词、受限工具、输出审核、全流程决策日志 [N15]；驻留与同意：未提及 |
| ④ | 自身即 CMS；文中把 Heidi 列为协同的临床文档工具 [N15] |
| ⑤ | 未公开 |
| ⑥ | **启示**：Lookout 的"六点控制（governed AI）"叙事是 aged care 买家熟悉的合规语言，CareKind 的 HITL/审计说法应同样具体；"CMS + 外部 scribe 协同"模式已在 home care 出现 |

#### A8. ShiftCare

| # | 内容 |
|---|---|
| ① | Progress notes、shift 摘要；美国版 **Care Signals** 实时审阅 note，标记事件/安全隐患与文档缺口，带严重度与置信度，管理员确认或清除 [N19] |
| ② | 护理员 app 内语音听写 + AI rephrase，用户审核后接受 [旧 A29] |
| ③ | Care Signals 页面使用"detects three severity levels"等措辞、对跌倒/用药错误/自伤标"High" [N19]——**在澳洲语境下接近 TGA 关注的"分析临床信息"边界**（推断，未经律师确认）；澳洲是否提供 Care Signals：未说明 |
| ④ | 自身即 CMS |
| ⑤ | AU：A$8–25/用户/月，AI notes 含在 Basic [旧 A28] |
| ⑥ | **启示**：价格锚点极低；其"严重度标签"正是我们 PRD A7 / DESIGN.md 明确不做的（不对临床风险着色/评分） |

#### A9. 其他 CMS（核实结果）

- **VCare**：仅找到 2022 年与 PainChek 合著的行业报告，未找到其 AI 文档功能 [N26]。
- **ManageCare**：**未找到**可核实的澳洲产品，不纳入。
- **Acredia**：澳洲 aged care 模块化软件；搜索摘要称 For Purpose Aged Care Australia 2026-01 战略投资以"完全重建"平台、在临床/运营/合规模块整合 AI [N27]【未核实，原页 403】。
- **Statura Care、Ideagen**：合规/治理与政策管理，非床旁记录 [旧 A36][N28]。

### B. AI scribe（通用临床）——是否进入 aged care

#### B1. Heidi Health

| # | 内容 |
|---|---|
| ① | Aged care 页：care note、incident report、family letter、care plan；模板含 falls risk assessment、wound documentation；基于机构政策的 cited answers [N29] |
| ② | Ambient（"listens to your visit"）+ 桌面听写 + 挂绳式 Remote 设备（断网继续记录）；母语口述→英文草稿 [N29] |
| ③ | 驻留：ANZ 数据本地托管、音频生成 note 后删除 [N14]；认证：ISO 27001、ISO 42001、SOC 2 Type 2 [N12][N13]；HITL：草稿"ready for your review" [N29]；**aged care 页未说明同意处理、未作 TGA 声明** [N29]；在 TGA 审查的 12 款之列（未知是否属 8 款）[N1] |
| ④ | Aged care 页未列 aged care 系统集成 [N29]；Lookout 文中提到协同 [N15]；正在招聘 EMR/EHR 集成工程师 [N30] |
| ⑤ | 有免费层；付费价格官网未公开 [旧 B3] |
| ⑥ | **优点**：资金、认证、ambient 设备、多语言。**短板**：以"一次问诊/一次探访"为单位，需先确定对象；面向临床人员；同意交给用户；新增"Evidence"临床问答使其更接近 TGA 关注区。**启示**：不在"转写质量"上竞争；在班次归属、PCW 工作流、澳洲 aged care CMS 回写、同意基础设施上竞争 |

#### B2. Lyrebird Health

| # | 内容 |
|---|---|
| ① | GP/专科/医院 notes、信件；aged care 无专门产品 [旧 B12] |
| ② | Ambient |
| ③ | **同意做成产品功能**：录音前提示获取同意并打时间戳，同意写入 note 并随写回 Best Practice 记录；可中途停止、对敏感问诊关闭 [N31]；同意指南强调 NSW/SA 全体主要当事人同意、认知障碍时的替代决策人并记录其姓名与关系 [N32]；Azure 悉尼处理、音频转写后丢弃、note 默认 7 天删除 [N31]；ISO 27001 等 [旧 B12] |
| ④ | Best Practice（双向）、Epic、Cerner 等 [旧 B12] |
| ⑤ | Free / Pro $160/月 [旧 B12] |
| ⑥ | **启示**：同意时间戳 + 写入记录 + 替代决策人记录，是 CareKind D8 同意管理可直接对标的行业最佳实践；但 Lyrebird 未进入 aged care |

#### B3. Telstra Health Smart Scribe（GP）——见 A1

#### B4. Microsoft Dragon Copilot（含护理版）/ Nuance DAX

- 护理 ambient：床旁对话→flowsheet，护士可暂停预览、编辑后传入 EHR（Epic）；美国 2025-12 GA [N33]。区域上线清单含美、加、英、荷、法、德、奥、爱，**未见澳洲护理版** [N34]【二手许可博客】。Dragon Medical One 在 TGA 审查名单中 [N1]。
- **启示**：医院护理赛道，不进入 aged care；但其"暂停预览—编辑—传 flowsheet"交互可参考。

#### B5. Abridge / Ambience / Suki / Tandem

- Abridge、Ambience：医院 inpatient 护理产品 [旧 C2][旧 C12]；本次**未找到 SNF/长期照护/aged care 部署** [N35]。
- Suki：称平台支持 skilled nursing 与 home health；与 WellSky 合作把 ambient scribe 集成到其专科 EHR（含 LTACH、康复）[N35][N36]；澳洲业务未找到。
- Tandem：欧洲/NHS，未找到澳洲业务 [旧 C15]。
- **启示**：美国大 scribe 进入长期照护的路径是"嵌入 EHR 厂商"（Suki×WellSky、Nabla×PointClickCare），而不是直销养老院。

#### B6. Nabla（经 PointClickCare 进入 SNF）——见 C2

### C. Aged care / 护理专属 AI（澳洲 + 海外）

#### C1. voize（德国，护理语音记录）

| # | 内容 |
|---|---|
| ① | 护理报告、生命体征、液体摄入等结构化表单；伤口图像、给药等 [N3][N4] |
| ② | 对手机口述，**AI 识别居民并把记录分配到对应居民与表单**；离线运行、恢复连接后同步 [N3]（官网未写明按键或 ambient） |
| ③ | HITL："there's always a human in the loop"、"does not add or assume any information" [N3]；美国部署端侧语音识别、签 BAA [N3]；德国报道称数据本地存储 [N37]【二手】；ISO 27001/GDPR/医疗器械声明：官网正文未见 [N3] |
| ④ | MEDIFOX DAN、Connext Vivendi、Dedalus ORBIS U 等，双向集成 [N3] |
| ⑤ | 未公开 |
| ⑥ | **优点**：几乎就是"护士只管说、系统负责归属 + 写回"的成熟版本，规模大（自称 2,000+ 机构）。**短板**：无澳洲业务、澳洲 CMS 无集成。**启示**：证明该机制可规模化；也说明它可能进入澳洲——CareKind 需在 12–24 个月内建立澳洲 CMS 集成与本地合规壁垒；值得研究其"表单字段级结构化"与离线设计 |

#### C2. PointClickCare Vox Advantage + Ambient Scribe Services（Nabla）

| # | 内容 |
|---|---|
| ① | SNF/senior living 护理对话→EHR 临床 note [旧 C5] |
| ② | 员工手机 app 录制护理互动（ambient）[N38] |
| ③ | 官方称"builds consent into every session"、每条 note 签署后入档 [N38]；但 Nabla 版合同：**同意由客户独自负责**、数据可用于调优语音识别、PCC 不保留审计日志、"Not a Medical Device"条款与"not a health care provider"免责 [N5]；评论文章质疑同意细节过少、在居民房间用员工手机录音 [N38] |
| ④ | 原生内置于 PCC EHR |
| ⑤ | 未公开 |
| ⑥ | **启示**：EHR 原生 ambient 是海外终局形态；其合同把同意与错误纠正全部推给机构——**CareKind 可把"同意状态在系统里强制执行 + 不用客户数据训练 + 完整审计日志"作为机构 IT/法务审查的卖点** |

#### C3. Notive（澳洲，阿德莱德）

见第 0 节第 5 条 [N9]。①交班/progress notes、incident 与 RN follow-up 标记、PDF 合规导出 ②语音听写 ③音频即删、数据悉尼、签署锁定 + addendum、"Privacy Act 1988 aligned"、无认证/TGA/同意说明 ④无集成（浏览器）⑤7 天试用，按规模议价 ⑥**启示**：与 CareKind H1 高度重叠但无归属、无多语言、无 CMS 回写；"签署后只能追加更正"已是本土小玩家的基本盘，不再是差异点。

#### C4. AccuNote（澳洲）

①progress notes（模板/自由文本/听写），对照 Quality Standards 检查；SIRS/handover/care plan 不是功能模块 ②听写 + 模板 ③数据存澳洲；"should review the transcription… before saving"；无认证、同意、TGA 说明；明确"不认证合规、不保证评估结果" ④称与 Telstra CM、PCS、AlayaCare"alongside"，未说明技术方式 ⑤14 天试用 ⑥声称省 80% 时间/每班 2–3 小时（vendor claim）[N39]。**启示**：用"Quality Standards 合规评分"做卖点，但无具名客户。

#### C5. Provider 自建：Uniting "Buddy"、Regis "RegiCare Assist"

- Buddy：多语言语音→case notes + 翻译，1,200+ 员工 [旧 B16]；2026-07 报道称平台"now used by other providers" [N11]【付费墙，细节未核实】。
- RegiCare Assist：Copilot Studio + Foundry，汇总 notes/24 小时报告，点选式审定提示词，约 150 人使用，计划与 CMS 集成；未披露数据驻留 [N10]。
- **启示**：大型 provider 选择在 Microsoft 生态内自建"阅读/汇总"层；CareKind 的买家更可能是**无力自建的中小机构**（与 PRD A5 一致），并应支持 Azure 澳洲区域以降低大型机构 IT 顾虑（推断）。

#### C6. Minikai、MediQo Health、AI Healthcare（Yes AI）

沿用旧研究 [旧 B20–B24]；本次未找到新的公开动态。

#### C7. 英国护理软件内置语音：Access NotesCentre / Smart Notes、Birdie、Nourish

- Access NotesCentre：AI 听写，**私有 LLM 仅在英国数据中心运行**、不送公共 AI、不用于训练、ISO 27001、与 Access Mosaic 集成（状态表述不一）[N40]。
- Birdie SmartPlans、Nourish speech-to-text：见 [旧 C7–C9]。
- **启示**："私有模型 + 本国数据中心 + 不训练"是英国护理软件的标准合规话术——澳洲买家会用同样的问题审 CareKind。

#### C8. Ambient 监测类（非文档，但会与"环境录音"混淆）

- **Ally Cares（英国）**：夜间声学监测，按声音建立活动画像并提示呼救/异常活动，与 KareInn 护理记录联动，案例称覆盖 6,000+ 居室 [N41]【vendor 材料】。
- **Sensi.ai（美国 home care）**：无摄像头的家庭音频 pod，持续 ambient 音频分析 [N42]【二手汇总】。
- 南澳 2021–2022 两家院舍 AI 音视频监测试点的公开事件记录称产生大量误报 [N43]【事件数据库二手，供应商未确认】。
- **启示**：这类产品属于"监测/预警"，正是 CareKind 不做的（TGA + 监控法风险）。对外沟通须清楚区分"护理员主动口述记录"与"环境监听"，避免被归为同类。

#### C9. 未能核实存在的名称

- "Kinora"、"Care Pro AI"：**未找到**可核实的 aged care 产品 [N44]，不纳入。

## 3. 行业通行做法（Patterns）

1. **听写优于 ambient（在 aged care）**：澳洲 aged care 已上线产品（ShiftCare、Notive、AccuNote、AlayaCare）几乎都是护理员对设备口述；ambient 主要出现在临床问诊型产品（Heidi、Lyrebird、PCC Vox、Dragon）。
2. **"音频即删 + 澳洲托管 + 不训练"已是入场券**：Heidi、Lyrebird、Telstra Smart Scribe、Notive、AccuNote 都作此类声明 [N6][N9][N14][N31][N39]——不再构成差异。
3. **HITL 普遍是"一句话"**：多数只写"ready for review"；做得深的会锁定签署记录（Notive）、全流程决策日志（Lookout）、同意时间戳写入记录（Lyrebird）。
4. **同意大多推给用户/机构**：PCC 合同最极端 [N5]；Heidi aged care 页不提同意 [N29]；只有 Lyrebird、Telstra Smart Scribe 把"每次提示确认同意"做进产品 [N6][N31]。**没有任何 aged care 产品展示"居民级同意状态 + 替代决策人 + 未同意者不处理"的系统化做法。**
5. **TGA 定位靠免责声明**：PCC/Nabla 合同"Not a Medical Device"条款 [N5]；多数澳洲产品不提 TGA。TGA 2026-10 已明确声明不足以定性 [N1]。
6. **海外终局 = EHR 原生或嵌入 EHR**：PCC×Nabla、Suki×WellSky、voize 双向集成、Access×Mosaic；独立 scribe 在长期照护中靠"嵌入"而非直销。
7. **从"写"走向"审"**：ShiftCare Care Signals、AccuNote 合规评分、Regis 汇总报告——下一波竞争是"记录质量/完整性检查"。
8. **大型 provider 自建 + 中小机构买现成**：Uniting、Regis 自建；Notive/AccuNote 瞄准中小机构。

## 4. 市场空白 / CareKind 差异化机会

| 空白 | 证据 | CareKind 对应（PRD） |
|---|---|---|
| **班次级、按居民自动归属——在澳洲无人提供** | voize 在德国已做 [N3]；澳洲 Heidi/Notive/AccuNote 均为"先定对象或单条 note" [N9][N29][N39] | A2、C3 归属引擎；"不确定就待归属"比 voize 公开描述更保守 |
| **系统化的居民级同意管理** | 多数产品把同意推给用户/机构 [N5][N29] | D8 同意管理；未同意居民不经 AI 处理 |
| **写回澳洲 residential CMS** | Telstra/Leecare/AutumnCare/PCS 均无 AI 记录 [N8][N22][N23][N24]；Heidi 未列 aged care 集成 [N29]；Notive 无集成 [N9] | D7 导出与回写、H2 集成 |
| **PCW / CALD 多语言 + RN 复核工作流** | Heidi 母语→英文但面向临床人员 [N29]；Buddy 仅限 Uniting 及合作方 [N11]；Notive 未提多语言 [N9] | D4 PCW 起草→RN 复核；A3 亮点 3 |
| **"可证明 documentation-only"的 TGA 设计** | TGA：8/12 scribe 可能属器械，声明无效 [N1] | F1：用功能边界（不生成诊断/建议/风险评分）+ 评测证据，而非免责声明 |
| **法定字段结构（事件 13 项、SIRS 时限提醒）** | 多数 incident 功能为通用格式或"flag" [N9][N19][N29] | E4 记录生成、C5 事件快速通道 |
| **完整审计留痕 + 不用客户数据训练** | PCC 合同不保留审计日志、数据用于调优 [N5] | C7、A7 |

## 5. 我们应避免的做法

1. **用免责声明代替功能边界**——TGA 已表态无效 [N1]。
2. **严重度/风险标签与"detects"式宣传**（如 Care Signals 的 High/Moderate/Low 与置信度 [N19]）——违反 PRD A7、O-4.2 与 DESIGN.md。
3. **把录音同意全部推给机构**（PCC 合同模式 [N5]）——在 NSW 等全体同意州份对机构与我们都是刑事风险。
4. **用客户音频/转写训练或调优模型**（PCC/Nabla 条款 [N5]）——违反 PRD A7"不训练"。
5. **在居民房间用员工手机做 ambient 录音**（PCC Vox 被质疑之处 [N38]）——与 DR-004 按键口述默认相悖。
6. **环境音频监测/预警**（Ally、Sensi 类 [N41][N42]）——属监测，不是记录。
7. **未披露托管地点或子处理方**（AlayaCare 未写托管地 [旧 A19]；Heidi 隐私政策提到境外收件人 [N14]）——我们须在 DPA 中列清（O-1.3）。
8. **无证据的节省时间数字**（AccuNote"80%"、Lookout"11,000 小时"均为 vendor claim [N39][N15]）——ACL 风险，我们只用试点证据。
9. **宣称合规评分/保证审核通过**——AccuNote 自己也声明不保证 [N39]；CareKind 只说"审核就绪的结构"，不承诺结果。

## 6. 对比表（竞品 × 交互 × 同意 × 驻留 × HITL × CMS 集成 × aged care 专注度）

> ✅ 有公开证据｜🟡 部分/二手｜❌ 未找到｜— 不适用。aged care 专注度：高=专门为 aged care 设计；中=有 aged care 方案但非核心；低=未进入。

| 竞品 | 交互方式 | 录音同意处理 | 数据驻留 | HITL | CMS 集成 | Aged care 专注度 | 来源 |
|---|---|---|---|---|---|---|---|
| Telstra Health Clinical Manager | 点选/键入（aged care）；GP 版 ambient | GP 版每次提示确认 ✅；aged care — | GP 版 AU ✅；aged care ❌ | GP 版审核后保存 ✅ | 自身即 CMS | 高（无 AI） | N6 N8 N20 |
| Leecare P6 | 表单；语音合作 🟡 | ❌ | ❌ | — | 自身即 CMS；嵌入第三方先例 | 高（无 AI） | 旧 A7–A9, N22 |
| AutumnCare | 移动表单 | — | ❌ | — | 自身即 CMS | 高（无 AI） | N23 |
| PCS | icon 点选 | — | ❌ | — | 自身即 CMS | 高（无 AI） | N24 |
| AlayaCare | 听写→表单 | ❌ | ❌ 未写明（SOC 2） | ✅ 人工批准 | 自身即 CMS | 高（home care） | 旧 A19–A21 |
| Lookout Assist | 任务 agents，多语言 | ❌ | ❌ | ✅ 六点控制 + 日志 | 自身即 CMS；提及 Heidi 协同 | 高（home care） | N15 |
| ShiftCare | 听写 + rephrase | ❌ | 🟡 | ✅ 审核/triage | 自身即 CMS | 中（NDIS/home） | 旧 A28–29, N19 |
| Heidi Health | Ambient + 听写 + 挂绳设备 | ❌ aged care 页未说明 | ✅ AU | ✅ review | ❌ aged care 未列 | 中 | N12–14, N29 |
| Lyrebird | Ambient | ✅ 提示 + 时间戳 + 写入记录 | ✅ Azure 悉尼 | ✅ | GP/医院 EHR | 低 | N31 N32 |
| Dragon Copilot 护理版 | Ambient→flowsheet | ❌ | ❌ AU 未上线 | ✅ 预览编辑 | Epic | 低 | N33 N34 |
| voize（DE） | 口述→自动归属居民 + 表单，离线 | ❌ 官网未说明 | 🟡 端侧/本地 | ✅ | ✅ MEDIFOX、Vivendi、ORBIS | 高（无 AU） | N3 N4 N37 |
| PCC Vox / Ambient Scribe（Nabla） | 手机 ambient | 🟡 "built into session"；合同由客户负责 | ❌ 美国 | ✅ 签署入档 | EHR 原生 | 高（无 AU） | N5 N38 |
| Notive | 听写→交班 note | ❌ | ✅ 悉尼 | ✅ 签署锁定 + addendum | ❌ | 高 | N9 |
| AccuNote | 听写/模板 | ❌ | ✅ AU | ✅ 保存前审阅 | 🟡 "alongside"，方式未说明 | 高 | N39 |
| Uniting Buddy（自建） | 多语言语音 + 翻译 | ❌ 未披露 | ❌ 未披露 | 🟡 | 内部 | 高（自用 + 合作方） | 旧 B16, N11 |
| Regis RegiCare Assist（自建） | 点选式汇总已有 notes | — | ❌ 未披露 | 🟡 管理者审阅 | 计划集成 | 高（自用） | N10 |
| Access NotesCentre（UK） | 听写 | ❌ | ✅ 英国私有 LLM | 🟡 审计轨迹 | Access Mosaic | 中（社会照护） | N40 |
| **CareKind（计划，非现状）** | 按键口述，班次级自动归属 | 居民级同意状态，未同意不处理 | AU | 签字 + PCW→RN 复核 + 逐句溯源 | 导出 → 回写澳洲 CMS（H2） | 高 | PRD |

## 7. 建议更新（competitor-matrix.md 等，待人工确认后修改）

1. **新增行**：voize（DE，护理语音 + 居民自动归属，2,000+ 机构自称，US$50M Series A 2025-11，无 AU 业务）[N3][N4]；Notive（AU，SA，听写交班 note，悉尼托管）[N9]；Regis RegiCare Assist（provider 自建）[N10]；Telstra Health Smart Scribe（GP，AU 数据，2025-02）[N6]；Acredia（AI 重建，【未核实】）[N27]；Ally Cares / Sensi.ai 归入"监测类，非竞品"[N41][N42]。
2. **修改 Telstra Health 行**："其他 AI"补充"已有 GP 版 Smart Scribe；2026-05 出售 Kyra Flow 并宣布 care intelligence ecosystem"[N6][N7]；"数据驻留"可注明 Smart Scribe 为 AU 数据中心（aged care 产品仍未明示）。
3. **修改 Heidi 行**：增加"ISO 27001 / ISO 42001 / SOC 2 Type 2"[N12][N13]；"TGA 立场"改为"在 TGA 2026-10 审查的 12 款中（结果未点名）"[N1]；"集成"补充"Lookout 文中提到协同，未见正式集成"[N15]。
4. **修改 Lyrebird 行**：增加"同意提示 + 时间戳写入记录；note 默认 7 天删除"[N31]。
5. **修改 PointClickCare 行**：注明 Ambient Scribe Services 由 Nabla 提供、同意由客户负责、数据可用于调优 [N5]；Vox Advantage 2026-10 商用**本次未确认已发生** [N38]。
6. **修改 ShiftCare 行**：增加"美国版 Care Signals（严重度标签 + 置信度）"[N19]。
7. **README 一页摘要第 6 条（监管）**建议补："TGA 2026-10-16 审查：8/12 scribe 可能属器械，免责声明不足" [N1]——同时建议 Terry 判断是否需要触发 `regulatory-watch` 把该结果加入 `03-legal-compliance/`（产品决策须引用本地法律文件，本文件不替代）。
8. **sources.md**：建议追加本文 N1–N44。
9. **删除/标注**：任务列表中的 "ManageCare"、"Kinora"、"Care Pro AI" 未找到，建议不入矩阵。

## 8. 局限

- TGA 审查结果来自 Medical Republic 报道，TGA 官方页面本次超时未打开 [N1][N2]；8 款具体名单未公开。
- voize、PCC、Heidi 的同意与驻留细节以官网/合同为准，可能随版本变化；未联系厂商。
- 付费墙（Weekly Source）与 403 页面（Acredia）内容未核实。
- 未找到任何竞品的 IRAP 评估声明。
- 本文的"推断"均已标明，不构成法律意见；涉及 TGA、监控法、同意的判断需律师与 Clinical Lead 确认。

## 来源（核查日期均为 2026-10-19，除另注明）

| # | 主题 | URL |
|---|---|---|
| N1 | Medical Republic：Eight of 12 AI scribes may be medical devices（2026-10-16） | https://www.medicalrepublic.com.au/?p=130085 |
| N2 | TGA：Outcome of digital scribe review（抓取超时，未直接打开） | https://www.tga.gov.au/node/599817 |
| N3 | voize 官网（EN/DE FAQ） | https://www.voize.ai/ |
| N4 | tech.eu：voize US$50M Series A（2025-11-17） | https://tech.eu/2025/11/17/voize-lands-50m-to-bring-ai-where-its-needed-most-the-nursing-frontline/ |
| N5 | PointClickCare Addendum to MSA – Ambient Scribe Services（2026-03，PDF） | https://pointclickcare.com/wp-content/uploads/2026/03/PointClickCare-Addendum-to-MSA-Ambient-Scribe-Services.pdf |
| N6 | Telstra Health：Smart Scribe 发布（2025-02-26） | https://www.telstrahealth.com/telstra-health-launches-ai-powered-smart-scribe/ |
| N7 | Alcidion ASX 公告：收购 Kyra flow products（2026-05-18，含 Telstra Health 声明） | https://announcements.asx.com.au/asxpdf/20260518/pdf/06zp94b3v05k8y.pdf |
| N8 | Telstra Health aged care 产品目录（沿用 [旧 A1]，本次检索未见 AI notes） | https://www.telstrahealth.com/products-category/aged-care/ |
| N9 | Notive 官网 | https://notive.com.au/ |
| N10 | Microsoft Source Asia：Regis RegiCare Assist（2026-05-19） | https://news.microsoft.com/source/asia/features/at-aged-care-provider-regis-ai-takes-on-paperwork-so-staff-can-focus-on-residents/ |
| N11 | The Weekly Source：Inside Uniting's AI platform now used by other providers（2026-07-24，付费墙） | https://www.theweeklysource.com.au/inside-unitings-ai-platform-now-used-by-other-providers/ |
| N12 | Heidi Support：Is Heidi compliant with healthcare privacy regulations | https://support.heidihealth.com/en/articles/8885110-is-heidi-compliant-with-healthcare-privacy-regulations |
| N13 | Heidi 博客：SOC 2 Type 2 certification | https://www.heidihealth.com/en-ca/blog/soc-2-type-2-certification |
| N14 | Heidi ANZ Compliance（沿用 [旧 B4]，本次复核） | https://www.heidihealth.com/en-au/compliance/app |
| N15 | Lookout：Lookout Assist 发布（2026-06-01） | https://thelookoutway.com/blog/2026-06-01-powering-the-next-horizon-in-home-care |
| N16 | 卫生部：New Aged Care Act – digital readiness checklist（2025-10） | https://www.health.gov.au/sites/default/files/2025-10/new-aged-care-act-a-digital-readiness-checklist-for-providers.pdf |
| N17 | King & Wood Mallesons：A new Aged Care Act – what is changing | https://www.mallesons.com/content/mallesons/au/en/insights/latest-thinking/a-new-aged-care-act-what-is-changing-and-what-you-need-to-know |
| N18 | The Weekly Source：AlayaCare acquires Nightingale Software | https://www.theweeklysource.com.au/alayacare-acquires-nightingale-software-to-deepen-its-aged-care-footprint-in-anz/ |
| N19 | ShiftCare（US）Care Signals | https://shiftcare.com/us/care-signals |
| N20 | Telstra Health：AN-ACC and aged care – is your clinical software AN-ACC ready | https://telstrahealth.com/an-acc-and-aged-care-is-your-clinical-software-an-acc-ready |
| N21 | Mirus Australia：AN-ACC 分类页（AI 试点，2024） | https://www.mirusaustralia.com/category/an-acc/page/3 |
| N22 | 检索记录：Leecare 2026 AI（无结果）；Leecare 官网 | https://leecare.com.au/ |
| N23 | Caring Times：OneTouch acquires Australian care platform；AutumnCare 移动端 | https://caring-times.co.uk/?p=38681 |
| N24 | PCS：icon-driven progress notes（复核）；CB Insights PCS 概况 | https://personcentredsoftware.com/en-au/resources/why-icon-driven-progress-notes-are-more-person-centred |
| N25 | Accel-KKR：Evaran 成立（沿用 [旧 A16]）；本次检索无 eCase AI 结果 | https://www.accel-kkr.com/evaran-launches-to-unify-aged-care-technology-as-providers-adapt-to-new-regulatory-environment/ |
| N26 | PainChek × VCare 行业报告（2022） | https://www.painchek.com/industry-report-digital-transformation-in-aged-care-2022-and-beyond/ |
| N27 | Techleap：For Purpose backs Acredia in AI-powered aged care software rebuild（403，仅搜索摘要） | https://finder.techleap.nl/news/feed/for-purpose-backs-acredia-in-ai-powered-aged-care-software-rebuild-1 |
| N28 | Ideagen aged care management | https://au.ideagen.com/lp-aged-care-management |
| N29 | Heidi：Aged care 解决方案页（复核） | https://www.heidihealth.com/solutions/aged-care |
| N30 | Heidi 招聘：Senior Software Engineer – EMR/EHR Integrations | https://jobs.blackbird.vc/companies/heidi-health/jobs/67219349-senior-software-engineer-backend-emr-ehr-integrations |
| N31 | Lyrebird Help：How do I obtain patient consent；Best Practice 集成 FAQ | https://help.lyrebirdhealth.com/en/articles/9229843-how-do-i-obtain-patient-consent |
| N32 | Lyrebird 博客：Patient consent for AI scribes in Australia（2026-01-01，复审 2026-08-25） | https://www.lyrebirdhealth.com/au/blogs/patient-consent-for-ai-scribes-in-australia |
| N33 | Microsoft：Dragon Copilot 扩展至护士（2025-10-16） | https://news.microsoft.com/source/2025/10/16/microsoft-extends-ai-advancements-in-dragon-copilot-to-nurses-and-partners-to-enhance-patient-care/ |
| N34 | Licensing School：Dragon Copilot 许可与区域（二手） | https://www.licensingschool.co.uk/licensing-blog/tag/dragon-copilot/ |
| N35 | Healthcare IT News：Suki expands availability（含 SNF、home health） | https://www.healthcareitnews.com/news/suki-expands-availability-its-ambient-ai-clinical-documentation-platform |
| N36 | Fierce Healthcare：Suki × WellSky（2025-10-31） | https://www.fiercehealthcare.com/ai-and-machine-learning/suki-inks-partnership-wellsky-integrate-ambient-ai-specialty-care-ehr |
| N37 | Sonntagsblatt：voize 在养老院的使用（德语，二手） | https://www.sonntagsblatt.de/artikel/gesellschaft/digitale-pflege-mit-herz-wie-sprachsoftware-den-alltag-im-heim-erleichtert |
| N38 | SpeechTechMag：PointClickCare Launches Vox Advantage；评论 ustechautomations | https://www.speechtechmag.com/Articles/Archives/Industry-View/PointClickCare-Launches-Vox-Advantage-176128.aspx |
| N39 | AccuNote 官网（复核）；AccuNote 比较文（2026-02-05） | https://accunote.com.au/ ；https://accunote.com.au/blog/best-progress-note-software-aged-care-australia |
| N40 | Access Group：Access NotesCentre | https://www.theaccessgroup.com/en-gb/products/access-notes-centre |
| N41 | techUK：Ally Cares intelligent care after dark case study | https://www.techuk.org/insights/guest-insights/ally-cares-intelligent-care-after-dark-case-study |
| N42 | Home Health Care News：Sensi.ai Series B；yespress 汇总 | https://homehealthcarenews.com/2024/06/home-care-technology-platform-sensi-ai-raises-31-million-in-series-b/ |
| N43 | AI Incident Database：AI-enabled video and audio surveillance system（SA 试点） | https://incidentdatabase.ai/es/entities/ai-enabled-video-and-audio-surveillance-system-for-fallscream-detection/ |
| N44 | 检索记录："Kinora" OR "Care Pro AI" aged care（无匹配结果，2026-10-19） | — |
