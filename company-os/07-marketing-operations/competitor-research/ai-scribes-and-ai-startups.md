# AI scribe 与 AI 初创公司详细档案（澳洲 + 国际）

> 研究日期：2026-10-10。来源编号见 `sources.md`。“[未核实]”= 仅二手/搜索摘要；厂商数据为 vendor claim。

## 一、澳洲 AI scribe（通用临床，正在下沉到 aged care）

### 1. Heidi Health —— 头号威胁

| 项目 | 内容 |
|---|---|
| HQ | 墨尔本，2019 年成立 |
| 目标细分 | GP、专科、急诊、医院；**已有专门的 Aged care 解决方案页** [B1]，并发布护士 shift notes 指南 [B2] |
| Aged care 功能 | ambient scribe 生成 care notes、incident reports、care plans、family letters、falls risk 评估、wound 文档模板；基于机构自身政策的 cited answers；桌面听写；**Remote 挂绳式录音夹（断网仍可记录）**；均“ready for your review” [B1] |
| 输入方式 | Ambient（环境录音）+ dictation |
| 语言 | 可用母语转写/听写，**输出英文 note**（aged care 页）[B1]；其他页面称支持 115+ 语言 [仅搜索摘要] |
| 定价 | 官网 AU 页仅列 Free / Clinician / Practice / Enterprise，**无公开价格** [B3]；第三方称 2026 Clinician 约 US$110–150/用户/月 [B10][B11][未核实] |
| 数据驻留 | 自称 ANZ 数据“locally hosted within Australia”；隐私政策注明部分第三方服务可能在境外（不含可识别健康信息）；不保存音频 [B4] |
| TGA 立场 | 未找到 Heidi 针对 aged care 的 TGA 声明；其“Evidence”临床问答类功能若涉及治疗建议，需关注 TGA digital scribe 界线 [D1] |
| 集成 | aged care 页**未列出任何 aged care 系统集成** [B1]；Enterprise 计划有 EHR 集成 add-on [B3] |
| 融资/规模 | 2025-10 Series B US$65M（估值 US$465M）[B8]；2026-09 共 US$340M（US$100M Series C @US$900M + US$240M 成长投资）[B5][B6]；Forbes AU 报道估值 ~US$1.2B、2026-04 ARR US$50M [B7]（估值数字各源不一致）|
| Aged care 客户 | **Metlifecare（NZ）**：12 名 RN 4 个月试点后，扩展至另外 3 家 care homes（2026-05-12），RN 须审核编辑后再录入系统，并用于交班与会议 [B9]。澳洲 aged care 客户**未找到** |
| 对 CareKind | 资金、品牌、产品力远超我们；已明确进入 aged care。但其定位是“临床医生（RN/GP）”工具，未见 PCW/护理员、ADL 结构化、写回 Leecare/Telstra 等的证据——这是缝隙。 |

### 2. Lyrebird Health

| 项目 | 内容 |
|---|---|
| HQ | 墨尔本，2023 年上线 |
| 细分 | GP、专科、医院、企业网络；aged care **仅出现在客户 logo 中**，无专门产品 [B12] |
| 功能 | 后台 ambient 记录→SOAP notes、转诊信、care plans、出院小结等 |
| 集成 | Best Practice（独家双向）、Oracle Cerner、Epic、Meditech、Genie、Gentu 等 [B12] |
| 数据驻留 | **在澳洲境内处理和存储，不出境**；音频转写后销毁；不用于训练；APP、ISO 27001、Cyber Essentials Plus 等 [B12] |
| 定价 | Free（每月 50 次转写）；Pro **$160/月或 $1,920/年**（官网标 “$”，AU 页）[B12] |
| 融资 | 2025-06 约 $12M Series A（Five V Capital 领投）[B13] |
| 客户 | Gold Coast Health（澳洲最大医院 ambient AI 部署）、Alder Hey（英国）[B12][B14] |
| TGA | 发布过 TGA 与 AI scribe 的解读博客 [B15] |
| 对 CareKind | 目前非 aged care 直接竞品；其“全澳境内托管 + 定价 $160/临床医生/月”是**数据与价格锚点**。 |

### 3. 其他澳洲通用 scribe

- **i-scribe**（Magentus）：面向专科，集成 Genie/Gentu [B25]。定价未公开。非 aged care。
- **PatientNotes**：GP/allied health，列出 RACF 查房记录用例 [B26]。定价/客户未核实。
- **Microsoft Dragon Copilot**：护理 ambient 版 2025-10 发布，集成 Epic Rover，US 先行（12 月 GA）[C1]；**澳洲护理版上线未找到**。
- **Tandem Health**（瑞典）：欧洲/英国 NHS，**未找到澳洲业务** [C15]。
- **Amplify+**：**未找到**可核实信息。

## 二、澳洲 aged care / 社区护理专属 AI 初创与内部工具

### 4. Uniting NSW.ACT “Buddy”（Provider 自建，非商业产品）—— 最接近 CareKind 的参照物

- **内容**：多语言语音→progress notes + 自动翻译（保留口语表达）+ 实时政策问答；语言含 **Hindi、Nepali、Indonesian、Mandarin、Cantonese** [B16]。
- **规模/效果**：1,200+ home & community care workers 使用；case note 时间 15 分钟→<2 分钟；支持工作者每天省约 30 分钟；计划扩展至 residential aged care [B16]。
- **合作方**：Engage Squared（咨询）、Microsoft Tech for Social Impact；另有 5 家大型 aged care 机构共同参与（未具名）[B16]。获 2026 Australian NFP Technology Awards “Best use of AI for community impact”。
- **商业化**：文中未说明是否对外提供 [B16]。
- **意义**：**验证了“CALD 护理员多语言语音记录”需求真实且大型 provider 愿意投入**；同时说明大型 NFP 可能“自建”，CareKind 需证明比自建更便宜、更合规、可集成。参与的 5 家机构是潜在客户或潜在竞争联盟。

### 5. AccuNote

- 澳洲 aged care / NDIS / home care 文档工具：语音转文字、模板、对照 **strengthened Aged Care Quality Standards（2025-11-01 生效）** 的 note 检查器 [B17][B18]。
- 自称数据存放于澳洲服务器；声称与 Telstra Health Clinical Manager、Person Centred Software、AlayaCare “协同使用”（具体集成方式未说明）[B17]。
- 语言、定价、创始人、客户：**未公开**（仅 14 天免费试用）[B17]。声称每班省 2–3 小时 [vendor claim]。
- **意义**：定位与 CareKind 高度重合（Quality Standards 合规 + 语音 notes），但公开信息极少、无具名客户，体量可能很小。需持续监测。

### 6. AI Healthcare（aihealthcare.au，“Powered by Yes AI”）

- 覆盖牙科、aged care、GP、allied health 的通用 AI 服务商；aged care 方案含语音→合规格式 notes、语音 incident 报告、家属热线、多语言（面向家属）、与 iCare/MedSignal 等 eMAR 集成 [B20]。定价、托管、客户：**未公开**。

### 7. MediQo Health

- 澳洲 AI 平台：AI 接待、实时临床文档、听写、care planning 等；称已用于 GP、allied health 与 aged care [B24]。2026-08 任命 eCase 联创 Steven Strange 为 Director of Aged Care，进军 residential 与 home care [B23]。融资/客户/托管：**未公开**。
- **意义**：带着行业人脉进入 residential aged care 的新直接竞争者。

### 8. Minikai

- 墨尔本，2024 年成立；为 disability（NDIS）与 aged care 做 AI agents：对话→结构化报告、incident reporting、合规缺口扫描、“always-on audit” [B22]。
- 2025-02 种子轮 $2.5M（Tidal Ventures 领投、Antler 参投）；客户合计服务 15 万+ 人；具名客户 SDA Services [B21][B22]。
- **意义**：偏 NDIS 与合规/行政；若进入 aged care incident/progress notes 则与 CareKind 正面竞争。

### 9. 其他（非文档类但抢“AI 预算”）

- **Silverchain × Talius（CuriousThing）**：AI 语音外呼助手（确认/改期探访），2025-06 WA 试点 [B27][B28]。
- **Andromeda（Abi 机器人）**：陪伴机器人，90 种语言 [B29]。
- **InteliCare**：传感器 AI 监测 [A35]。

## 三、国际参考玩家

| 公司 | HQ | 细分 | AI 文档能力 | 进入澳洲？ | 来源 |
|---|---|---|---|---|---|
| **PointClickCare – Vox Advantage** | 加拿大/美国 | 美国 SNF / senior living EHR 龙头 | 移动端录制护理对话→EHR 内临床 note，按会话内置同意，护理团队签署后入档；2026-08 限量发布，**2026-10 商用**；另有 Chart Advisor | 未找到澳洲业务 | [C5][C6] |
| **Microsoft Dragon Copilot（护理）** | 美国 | 医院护士 | 床旁对话→flowsheet，护士审核后入 Epic | 澳洲护理版未找到 | [C1] |
| **Abridge for Nurses** | 美国 | 医院（Epic inpatient） | 与 Mayo/Epic 共建 ambient 护理文档 | 未找到 | [C2][C3] |
| **Suki** | 美国 | 医院/医生，2025-10 成立 Nursing Consortium | 护理 ambient 文档共建中；400+ 机构 | 未找到 | [C4] |
| **Ambience Healthcare** | 美国 | 医院（含 inpatient 护理套件） | Nursing Summary、Ambient Flowsheet；2025 Series C US$243M | 未找到 | [C12] |
| **Nabla** | 法国 | 医生（35 种语言） | Copilot 结构化 notes；无专门护理产品 | 未找到 | [C14] |
| **Hippocratic AI** | 美国 | 患者外呼 AI agents（出院随访等） | 非文档 scribe | 仅美国 [未核实] | [C13] |
| **Birdie – SmartPlans** | 英国 | Home care | 录制评估对话→引用转写片段的 care plan 草稿（2026-06-09） | 未找到 | [C7] |
| **Nourish Care** | 英国 | 社会照护（residential + home） | 手机 speech-to-text 记录；2026-08 获 Hg 成长投资，计划加速 AI | 未找到 | [C8][C9] |
| **Access Group – Smart Notes** | 英国 | 护理管理软件 | AI 语音记录观察，员工审核后定稿（2026-07） | 页面未提澳洲（Access 在澳洲有其他业务 [未核实]） | [C10] |
| **Log my Care** | 英国 | 社会照护 | icon 快速记录 + PainChek 集成；无 AI 语音 notes | 未找到 | [C11] |
| **Person Centred Software（UK）** | 英国 | Residential | icon-driven notes；未找到 AI 语音 | 已在澳洲（见 incumbents） | [A13][A14] |
| **日本 介護記録 AI 音声入力** | 日本 | 介護施設/訪問介護 | 分三类：介護ソフト内蔵型、通用转写、手机自带；通用工具约 ¥1,000/月起，介護ソフト ¥5,000–50,000/月（2026-08）；例：Confido “Voice DLog” | 未进入澳洲 | [C16][C17] |

**国际趋势要点**：
1. 2025–2026 年，“护理/社会照护版 ambient 文档”成为主流 EHR 的标配（PointClickCare、Access、Birdie、Microsoft、Abridge）。**澳洲 residential 系统是少数尚未跟进的市场**——窗口期可能只有 12–24 个月。
2. 国际产品几乎都“内置于 EHR”。独立 scribe 在 aged care 的长期出路是**成为 EHR 的 AI 层/合作伙伴**或被收购。
3. 英国 PE 整合（OneTouch 收购 AutumnCare、Evaran、Hg 投 Nourish）意味着澳洲 incumbents 可能从英国母公司“移植” AI 功能。
4. 日本的价格分层（通用工具 vs 内置型）可作为参考：独立工具价格天花板低，内置型可卖平台价。

## 四、监管要点（与所有竞品相关）

- **TGA**：仅转写/翻译、不做分析解读的 digital scribe **不是医疗器械**；若生成临床医生未陈述的诊断/鉴别诊断/治疗建议，则属医疗器械，需 ARTG 登记，TGA 已表示会执法 [D1][D2]。2025-11 TGA 开启 digital scribe 利益相关方信息收集 [D3]；2026-07 TGA 演示继续聚焦 AI/软件合规 [D4]。
- **ACSQHC** 2025-08 发布临床医生 AI（含 ambient scribe）实用指南 [D5]；AIDH 发布 AI scribe 实施指南 [D6]。
- **Aged Care Quality and Safety Commission** 在强化版 Quality Standards 下看“文档是否证明满足各 outcome”，泛化的 AI 文本可能失败；公共 GenAI、境外存储、知情同意是风险点 [D7]。
- 联邦卫生部内部材料指出部分 scribe 声称不受器械规管、部分供应商的云平台数据出境 [D9][仅搜索摘要]。
