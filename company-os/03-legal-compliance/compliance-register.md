# 合规登记册 Compliance Register

> Owner: Privacy Officer / CEO ｜ 复审: **每月** ｜ 最近核实: 2026-10-10
> ⚠️ 内部工作底稿，不构成法律意见。上线/签约前须由澳洲执业律师审阅。

状态：⬜ 未开始 ｜ 🟡 进行中 ｜ ✅ 达成 ｜ 👀 监测中（未来生效/尚未适用）

> 📚 详细法规调研、各州对比与下载的官方模板：[research/](research/README.md)（2026-10-10）。要点：
> - Aged Care Rules 2025：提供者的大部分法定记录须保留 **7 年**；NSW/VIC/ACT 健康记录法另有"最后服务后 7 年或至 25 岁"规则
> - Quality Standards Outcome 2.7 要求记录"准确且及时（accurate and current）"；Outcome 3.3 涉及交接与升级
> - SIRS：Priority 1 须 24 小时内、Priority 2 须 30 天内上报；委员会要求时 84 天内提交最终报告（旧指南写的是 60 天）
> - NSW/VIC/ACT 健康记录法直接约束私营机构，并限制健康数据出州/出境 → 全部数据与 AI 处理留在澳洲
> - 录音：NSW、WA、SA、TAS、ACT 一般需全体当事人同意，违反属刑事犯罪 → 默认护士按键口述（push-to-talk），不做常开环境录音

## 1. 健康数据与隐私

| 法规 / 框架 | 对我们意味着什么 | 我们的控制措施 | Owner | 状态 |
|---|---|---|---|---|
| **Privacy Act 1988 (Cth) + 13 条 APPs** | 我们处理健康信息（sensitive information）。持有健康信息的提供方**不适用**小企业豁免（A$3M 营业额门槛）—— 按完全受约束处理 | [隐私计划](privacy-program.md)、隐私政策、APP 映射 | Privacy Officer | ⬜ |
| **APP 8 跨境披露** | 若数据/LLM 处理在海外，我们对海外接收方的违规负责 | 数据与 AI 推理全部澳洲区域；[子处理方清单](../06-app-development/security/vendors-and-subprocessors.md) | CTO | ⬜ |
| **Notifiable Data Breaches (NDB)** | 疑似泄露 30 天内完成评估；构成"合格泄露"须尽快通知 OAIC 和受影响个人 | [数据泄露响应计划](data-breach-response-plan.md) | Privacy Officer | ⬜ |
| **Privacy and Other Legislation Amendment Act 2024（Tranche 1）** | 已生效：严重侵犯隐私的法定侵权诉讼（statutory tort）、OAIC 更强的执法与罚款层级 | 隐私设计、培训 | Privacy Officer | 🟡 |
| **自动化决策透明义务（Tranche 1）—— 2026-12-10 生效** | 隐私政策须披露：使用个人信息、且可能显著影响个人权益的自动化决策 | 我们不做自动化决策（HITL）；仍在隐私政策中透明说明 AI 的用途与边界 | Privacy Officer | 🟡 |
| **Tranche 2 改革（Privacy Amendment (Personal Data Protection) Bill 2026 征求意见稿，2026-08-31 发布）** | 可能引入"公平合理"处理测试、删除权等约 40 项变化；尚未立法 | 按"公平合理"标准提前设计；关注立法进展 | Privacy Officer | 👀 |
| **州/领地健康记录法**：Health Records Act 2001 (Vic)、Health Records and Information Privacy Act 2002 (NSW)、Health Records (Privacy and Access) Act 1997 (ACT) | 在这些州为客户处理健康信息，可能同时受州法约束（如访问、保留期限） | 按客户所在州对照；DPA 中约定 | Privacy Officer | ⬜ |
| **My Health Record / Healthcare Identifiers Act 2010** | 仅当集成 My Health Record 或使用 IHI 时适用 | 当前不集成；集成前重新评估 | CTO | ➖ |

## 2. 养老行业监管

| 法规 / 框架 | 对我们意味着什么 | 我们的控制措施 | Owner | 状态 |
|---|---|---|---|---|
| **Aged Care Act 2024 (Cth) + Aged Care Rules 2025**（2025-11-01 生效） | 我们不是注册提供者，但客户是；产品必须帮助而不是妨碍他们履行义务（记录、权利、事件管理） | [Aged Care 对齐](aged-care-alignment.md) | Clinical Lead | 🟡 |
| **Statement of Rights** | 长者的隐私、尊严、知情、选择权 → 影响录音同意与数据使用 | 同意流程、透明告知材料 | Clinical Lead | ⬜ |
| **Strengthened Aged Care Quality Standards** | 客户被按此审核；记录质量是证据 | 模板与完整性提示对齐标准 | Clinical Lead | ⬜ |
| **SIRS** | 客户有严格的上报时限；我们的工具不得延误或替代其判断 | Incident 草稿功能仅辅助，提示人工判断 | Clinical Lead | 👀 |
| **Code of Conduct for Aged Care / 工作人员筛查** | 我们进入机构的员工可能被客户要求 police check 等 | 现场人员 police check、按机构要求的疫苗/培训 | HR | ⬜ |

## 3. 医疗器械 / 临床

| 法规 / 框架 | 对我们意味着什么 | 我们的控制措施 | Owner | 状态 |
|---|---|---|---|---|
| **Therapeutic Goods Act 1989 / TGA SaMD 规则** | TGA 立场：只转录/整理临床对话的 digital scribe 不是医疗器械；生成未经临床人员陈述的诊断或治疗建议的则是。TGA 2026 年已对部分 AI scribe 采取合规行动，审查结果待发布 | [TGA 自评](tga-samd-assessment.md)；功能闸门 | CEO + Clinical Lead | 🟡 |
| **AHPRA / NMBA 专业义务** | 护士对记录负责；AHPRA 关于在医疗中使用 AI 的指引要求从业者理解工具、获得知情同意、审核输出 | 产品强制审核；为客户提供护士使用指引 | Clinical Lead | ⬜ |
| **ACSQHC（澳洲医疗安全与质量委员会）AI scribe 指引** | 面向临床人员的使用建议，客户可能据此评估我们 | 对照其清单准备答复材料 | Clinical Lead | ⬜ |

## 4. 录音 / 监听

| 法规 | 对我们意味着什么 | 控制措施 | Owner | 状态 |
|---|---|---|---|---|
| **各州/领地 Surveillance Devices / Listening Devices / Invasion of Privacy Acts** | 规则各州不同，多数州要求私人对话的全体当事人同意 | [录音同意指南](recording-consent.md)：统一采用全体同意标准 | CEO | ⬜ |

## 5. AI 治理

| 框架 | 意义 | 控制措施 | Owner | 状态 |
|---|---|---|---|---|
| **Guidance for AI Adoption（NAIC/DISR，2025-10）—— 6 项基本实践** | 自愿性，但是客户和政府采购评估的事实标准 | [AI 治理](../06-app-development/ai-governance.md) | CTO | 🟡 |
| 澳洲尚无专门 AI 立法 | 关注政策变化 | 每季度检查 | CEO | 👀 |

## 6. 网络安全

| 法规 / 框架 | 意义 | 控制措施 | Owner | 状态 |
|---|---|---|---|---|
| **Cyber Security Act 2024** | 勒索软件赎金支付须在 72 小时内报告（适用营业额 > A$3M 的企业）；目前可能未达门槛 | 事件响应计划中预留流程 | CTO | 👀 |
| **ACSC Essential Eight** | 客户安全问卷常见要求 | [信息安全政策](../06-app-development/security/information-security-policy.md) | CTO | ⬜ |
| **ISO/IEC 27001 / SOC 2** | 大客户采购通常要求 | 路线图阶段 2–3 | CTO | 👀 |

## 7. 公司、劳动、消费者

| 法规 | 意义 | 控制措施 | Owner | 状态 |
|---|---|---|---|---|
| **Corporations Act 2001** | 董事义务、记录保存、ASIC 年审 | [设立清单](../00-company/setup-checklist.md) | CEO | ⬜ |
| **Fair Work Act 2009 + NES + Modern Awards** | 雇佣合同、最低条件、FWIS、right to disconnect | [HR](../05-hr-teams/) | HR | ⬜ |
| **Superannuation Guarantee + Payday Super（2026-07-01 起）** | SG 12%，须在发薪后 7 个工作日内到账 | 工资系统配置 | Finance | ⬜ |
| **WHS Act（按州）** | 包括心理社会风险；员工现场访问养老院的安全 | WHS 政策 | HR | ⬜ |
| **Australian Consumer Law** | 不得误导性宣传（"节省 X 小时"需有证据）；标准格式合同不公平条款（2023-11 起可罚款） | [市场合规](../07-marketing-operations/marketing-compliance.md)、合同审阅 | CEO | ⬜ |
| **Spam Act 2003** | 营销邮件须同意、标识、可退订 | 邮件营销工具设置 | Marketing | ⬜ |
| **税务**：GST、PAYG、STP、R&D Tax Incentive | 见 [财务](../04-finance/finance-ops.md) | | Finance | ⬜ |

---

## 法规变化监测源（每月扫一遍）

- OAIC 新闻与指引 — oaic.gov.au
- TGA 数字健康/AI 页面 — tga.gov.au（**重点：digital scribe 审查结果与新开发者指引**）
- Aged Care Quality and Safety Commission — agedcarequality.gov.au
- Department of Health, Disability and Ageing — health.gov.au
- AHPRA / NMBA — ahpra.gov.au
- National AI Centre — industry.gov.au
- ACSC — cyber.gov.au
- Fair Work Ombudsman — fairwork.gov.au
