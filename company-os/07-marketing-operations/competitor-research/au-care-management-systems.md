# 澳洲 aged care 护理管理系统（Incumbents）详细档案

> 研究日期：2026-10-10。来源编号见 `sources.md`（如 [A1]）。“[未核实]”= 仅有搜索摘要/二手来源；“未公开/未找到”= 公开渠道未找到。厂商数据均为 vendor claim。
>
> 对 CareKind AI 的意义：这些系统是 **progress notes 的最终落地处（system of record）**。我们必须与之集成（写回 notes），同时要警惕它们自研/内置 AI notes 功能而把我们挤出。

## 总体判断

- **Residential（RACF）主力系统**：Telstra Health（Clinical Manager / CareKeeper，前身 iCare）、Leecare（Platinum6）、AutumnCare（OneTouch 旗下）、Person Centred Software（PCS）、Health Metrics eCase（现属 Evaran）。DLA Piper 将 AutumnCare 称为澳洲 residential 软件 “top four” 之一 [A11]，但**公开渠道未找到可靠的市场份额数据**。
- **Support at Home / 社区护理主力系统**：AlayaCare、Lookout（The Lookout Way）、ShiftCare、Visualcare、Lumary（Salesforce 底座）、CareLineLive（Evaran）、eCase 也覆盖 home care。
- **AI 进展分化明显**：home care 系统（AlayaCare、Lookout、ShiftCare）已上线 AI 语音/摘要；residential 系统（Telstra Health、Leecare、AutumnCare、PCS）截至 2026-10 **未找到已上线的生成式 AI progress notes 功能**。这是 CareKind 在 residential 的窗口期。

---

## 1. Telstra Health（Clinical Manager / CareKeeper / Medication Management）

| 项目 | 内容 |
|---|---|
| HQ | 澳洲（Telstra 子公司） |
| 细分 | Residential aged care（主），另有医院、药房等 |
| 产品 | Clinical Manager、CareKeeper（床旁移动记录）、Medication Management、MedPoint、Resident Manager、Message Manager [A1] |
| 规模 | 自称 clinical software 支持 60,000+ aged care beds、药物软件 55,000+；业务起源为 **iCare**（即任务中提到的 “iCare Health” 实为 Telstra Health 前身）[A3]；另有报道称 Clinical Manager 部署于 360+ 设施 [A5][未核实] |
| AI 功能 | 与 RMIT、Digital Health CRC 合作的 **NLP/ML 风险预测**（跌倒、抑郁、死亡率），数据来自评估、观察表与 **progress notes** [A5]。**未找到生成式 AI 记录/语音 scribe 功能**。产品页未提 AI [A1] |
| 输入方式 | 移动端点选/键入（CareKeeper）；未见语音 |
| 近期客户 | Whiddon（23–24 家院舍，2025–2026）[A4]；Apollo Care（6 家院舍、近 500 床）[A6] |
| 定价 | 未公开 |
| 数据驻留 | 未找到明确声明（Telstra 为本土公司，推测本地托管 [未核实]） |
| 对 CareKind | **首要集成目标**（装机量大、无 GenAI notes）。同时也是最大潜在威胁：Telstra 有 Azure OpenAI 内部经验（Telstra 零售侧 “One Sentence Summary”）[未核实，见搜索摘要]，随时可能推出内置功能。 |

## 2. Leecare Solutions（Platinum6 / P6）

| 项目 | 内容 |
|---|---|
| HQ | 澳洲墨尔本，创始人兼 CEO Dr Caroline Lee [A7] |
| 细分 | Residential（主）、retirement villages、home care、定制 acute care [A7]；另有 NZ、新加坡、英国业务（第三方称 650+ 客户 [未核实]） |
| 产品 | Platinum6（浏览器端），模块 P6Community、P6Exec、P6Finance、P6Med、P6Mobile、P6MyCarePlan、P6Pharm Messenger；每月 15 日发版 [A7] |
| AI 功能 | 官网**未提 AI** [A7]。曾与 **Voice-Care** 合作给 P6 加语音能力（英国试点，日期未标注）[A9]。2025-10 与 **CAREFUL**（GP/药房/护理团队沟通协同平台）合作，非 AI [A8] |
| 集成 | 官网有 Interoperability 页但无细节 [A7]；愿意整合第三方（CAREFUL 被嵌入 P6）[A8] |
| 定价 / 融资 | 未公开 |
| 对 CareKind | **合作开放度高**（已有嵌入第三方的先例），是 partnership 优先对象之一。 |

## 3. AutumnCare（OneTouch Health 旗下）

| 项目 | 内容 |
|---|---|
| HQ | 澳洲；2023-08 被 August Equity 支持的 OneTouch Health（爱尔兰/英国）收购 [A10][A11] |
| 细分 | Residential（主），也有 home care、retirement living；2005 年上线，“top four” residential 软件商 [A11] |
| 产品 | 电子护理记录、药物管理、家属门户、护理员移动 app [A10] |
| AI 功能 | **未找到** AI/语音功能。OneTouch 2026-06 博客讨论 “AI in Social Care” [未核实，仅标题] |
| 客户 | Anglicare Southern Queensland（2021 起，含 residential 与 support at home）[仅搜索摘要] |
| 定价 | 未公开 |
| 对 CareKind | 集成目标；被 PE 支持的国际集团收购后可能从英国母公司引入 AI 功能（需持续监测）。 |

## 4. Person Centred Software（PCS，Australia）

| 项目 | 内容 |
|---|---|
| HQ | 英国；澳洲 2016 年开展、2018 年首家客户 [A13] |
| 细分 | Residential aged care、retirement living [A13] |
| 产品 | Clinical Care System、Resident Experience Platform 等；2022 年并入 ATLAS eMAR；2026-06 收购 Camascope（药物管理）[A13][A15] |
| 记录方式 | **icon-driven progress notes**（点图标预填 note，可扩写）[A14]；第三方称全球每日 900 万+ care notes [未核实] |
| AI 功能 | 澳洲/英国均**未找到**已发布的 AI 语音 notes |
| 对 CareKind | 其“快速点选”范式与我们的语音范式互补：PCS 的结构化 ADL 事件 + CareKind 的叙述性/事件型 note 可共存。集成目标。 |

## 5. Health Metrics – eCase（现属 Evaran）

| 项目 | 内容 |
|---|---|
| HQ | 维州 Heatherton；2026-05 与 MOA Benchmarking、CareLineLive（英国 home care）合组 **Evaran**（Accel-KKR 控股），2026-06 并入 Checked In Care [A16][A17] |
| 规模 | Evaran 自称 1,100+ providers、170,000 care recipients、2,100 地点、7 国 [A16]；eCase 自称 80,000+ recipients、770+ 地点 [仅搜索摘要] |
| 细分 | Residential、home care、retirement living、disability |
| AI 功能 | **未找到** eCase 生成式 AI 功能。早年与 Monash 做 ML 风险预测研究 [仅搜索摘要]。eCase 联创 Steven Strange 2026-08 加入 AI 公司 MediQo Health [B23] |
| 客户 | Summerset（NZ）澳洲业务 [A18]；Eldercare（SA）[仅搜索摘要] |
| 对 CareKind | PE 整合中的平台，可能通过并购补齐 AI（**威胁 + 潜在收购方**）。 |

## 6. AlayaCare（加拿大，ANZ 重点市场）

| 项目 | 内容 |
|---|---|
| HQ | 加拿大蒙特利尔；ANZ 有本地团队 |
| 细分 | Home & community care（Support at Home）；首批获 Support at Home API 认证，2025-11 与 Resthaven 提交首笔 claim [A25] |
| AI 功能（已上线） | **AI Form Assistant（语音听写→结构化表单，可审核后批准）**[A20]；**AI Smart Summaries**（note 摘要）；**Layla** 对话助手 [A24]；**Client Intelligence Suite**（NLP/LLM 分析 notes 预测风险，2025-02，premium 功能）[A23]；**AlayaFlow** agentic 平台（2026-02-25 悉尼发布，首批 agent：空班排班、visit 验证、推荐 care plan；声称文档时间降低最多 20%）[A21][A22] |
| 语言 | 未列出 [A19] |
| 数据 / 治理 | 声称遵守 Privacy Act 1988、SOC 2 Type II、HITRUST；每个 AI 动作需人工批准；**未写明数据托管地点** [A19] |
| 定价 | 未公开 |
| 对 CareKind | **在 Support at Home 是最强直接威胁**：已内置语音→表单。CareKind 若做 home care 赛道，差异化需在多语言 CALD 护理员、离线、PCW 体验上。 |

## 7. Lookout（The Lookout Way）

| 项目 | 内容 |
|---|---|
| HQ | 澳洲 |
| 细分 | Home care（100+ home care providers）[仅搜索摘要] |
| AI 功能 | **Lookout Assist**（2026-06-01）：任务型 AI agents——基于外部临床文档生成 care plan、clinical summaries、connected care handover 摘要、**多语言支持**；human-in-the-loop、决策日志 [A26][A27]；声称护理计划每月可省 ~11,000 小时 [vendor claim] |
| 定价 | 未公开 |
| 对 CareKind | home care 直接竞争；其“治理型 AI（governed AI）”叙事与我们相近。 |

## 8. ShiftCare

| 项目 | 内容 |
|---|---|
| HQ | 澳洲（亦有 UK/CA 站点） |
| 细分 | NDIS、home care（中小 provider） |
| AI 功能 | **AI progress notes**：护理员 app 内语音听写 → AI “rephrase” 为专业表述；shift 摘要、潜在 incident 提示；Completeness Coach；可连接 Claude/ChatGPT [A28][A29] |
| 定价（AUD，ex GST，每用户/月） | Basic $8（年付）/$9（月付）；Professional $13/$15；Premium $20/$25；最少 5 人；Enterprise（250+）未公开。AI progress notes 与语音转写包含于 Basic [A28] |
| 对 CareKind | **价格锚点**：基础 AI 语音 notes 已被“打包进 A$8–9/用户/月”的 SaaS，单卖 AI notes 在小型 home care 市场很难高价。 |

## 9. Visualcare

- 澳洲 home care / NDIS 管理平台。AI note-taking 在公开路线图上为 **“planned”**（自由文本 shift notes → 结构化）[A30]。未发布。定价未公开。

## 10. Lumary

- 阿德莱德公司，基于 **Salesforce** 的 disability / aged care 工作流平台 [A33]。**未找到** Lumary 自有 AI notes 功能；Salesforce Agentforce 有 home health 用例但未见与 Lumary 绑定 [未核实]。

## 11. Mirus Australia（MirusPlus）

- 咨询 + 软件（MirusPlus 平台；2025 收购 ManAd）；推出 **Careverse** 行业聚合临床数据集，并称在开发 AI [A31][A32]。偏 benchmarking/分析，**非床旁记录**。可作为数据/分析伙伴。

## 12. 其他相关

- **InteliCare（ASX: ICR）**：传感器 + AI 监测平台，与 Bolton Clarke、mecwacare 试点 [A35]——非文档类，可能成为数据输入伙伴。
- **Statura Care**：2026-04 进入市场的“compliance-first”平台（治理、incident 管理）[A36]。
- **Epicor**：**未找到**其在澳洲 aged care 护理记录领域的证据，建议不列为竞争对手。
- **CareLink+**：**未找到**可核实的澳洲产品信息（可能与其他名称混淆），不纳入。
- **iCare Health**：即 Telstra Health 前身 iCare [A3]，非独立公司。
- Services Australia 的 aged care online claiming 软件列表可用于核对厂商清单，但本次抓取超时 [A34][未核实]。
