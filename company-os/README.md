# CareKind AI — Company OS

> 让每一位养老护士把时间还给长者，而不是表格。
> *Give nurses their time back — for residents, not paperwork.*

这是 CareKind AI 的公司操作系统（Company OS）：公司如何思考、决策、运作、合规的**唯一事实来源（single source of truth）**。
任何"我们是怎么做 X 的？"的问题，答案都应该能在这里找到；找不到，就补上。

- **公司**：CareKind AI（拟注册为 CareKind AI Pty Ltd）
- **所在地**：澳大利亚
- **业务**：面向 aged care（养老机构 / 居家养老）护理人员的 AI 护理记录助手 —— 语音/简短输入 → 结构化护理记录（progress notes、ADL、incident、handover 等），护士审核后写入机构的护理管理系统
- **阶段**：Pre-seed / 项目启动期（OS 版本 v0.1，2026-10-10）

---

## 目录

| # | 模块 | 内容 | 状态 |
|---|------|------|------|
| 00 | [公司基础](00-company/) | 使命愿景价值观、公司档案、设立清单、术语表 | 🟡 草稿 |
| 01 | [战略](01-strategy/) | 定位与 ICP、OKR、路线图 | 🟡 草稿 |
| 02 | [运作节奏](02-operating-rhythm/) | 会议节奏、决策机制、决策日志 | 🟡 草稿 |
| 03 | [法律与合规](03-legal-compliance/) | **合规登记册**、隐私计划、数据泄露响应、录音同意、TGA 判定、Aged Care 对齐、[法规调研与模板](03-legal-compliance/research/) | 🔴 需律师审阅 |
| 04 | [财务](04-finance/) | 财务运营、税务、R&D 税收激励、ESIC | 🟡 草稿 |
| 05 | [HR 与团队](05-hr-teams/) | 团队名册（Terry、Ahmad、Matt、Dave）、组织与角色、招聘入职（Fair Work）、行为准则、员工政策、各团队文件夹 | 🟡 草稿 |
| 06 | [App 开发](06-app-development/) | 产品原则、临床安全框架、AI 治理、信息安全、工程规范、specs、R&D 记录（代码将来放独立 GitHub 仓库） | 🟡 草稿 |
| 07 | [市场与运营](07-marketing-operations/) | 品牌、市场合规、销售、试点、客户成功、渠道、[竞争对手调研](07-marketing-operations/competitor-research/README.md) | 🟡 草稿 |
| 08 | [用户反馈](08-feedback/README.md) | 用户反馈原始记录（raw）：原话照录，人工录入，**不经 AI 编写** | ✅ 结构就绪 |
| 09 | [工作流](09-workflows/README.md) | 周度运营回顾、月度合规检查、新功能闸门、成员入职、事件响应 —— Claude / Codex 可执行 | ✅ |
| 10 | [技能库](10-skills/README.md) | 9 个 skills（Claude `.claude/skills` 与 Codex `.agents/skills` 通用），改完运行 `sync_skills.py` | ✅ |
| 11 | [规范 Rules](11-rules/README.md) | 公司规范、运营规范、代码规范（SOLID / DRY / KISS，Tab 缩进宽度 4，单文件 ≤ 1000 行自动重构）、产品设计与 PRD 法律参考规范 + 法律参考索引；`check_rules.py` 自动检查 | ✅ |
| — | [模板](templates/) | 决策记录、周报、会议纪要、事故复盘 | ✅ |

## 使用规则

1. **先写下来再做**：重要决策写进 [决策日志](02-operating-rhythm/decision-log.md)；政策变更改这里的文档。
2. **每份文档有 Owner 和复审日期**（见文档头部）。过期未复审 = 不可信。
3. **合规优先**：任何涉及居民（resident / care recipient）数据、录音、AI 输出的改动，先查 [合规登记册](03-legal-compliance/compliance-register.md)。
4. **不是法律意见**：`03-legal-compliance/` 下的内容是内部工作底稿，基于 2026-10 的公开信息整理，**上线前必须由澳洲执业律师（健康/隐私方向）审阅**。
5. 改动通过 git 提交（建议），提交信息写清"改了什么、为什么"。

## 最高优先级的 10 件事（启动期）

见 [00-company/setup-checklist.md](00-company/setup-checklist.md) 与 [03-legal-compliance/compliance-register.md](03-legal-compliance/compliance-register.md)。摘要：

1. 注册 Pty Ltd（Director ID → ASIC → ABN/TFN）、股东协议、IP 转让给公司
2. 商标检索并申请 "CareKind"（IP Australia）
3. 确定产品边界：**只做记录，不做诊断/治疗建议**（保持在 TGA 医疗器械定义之外）
4. 数据全部驻留澳洲；LLM 供应商签署"不用于训练 + 澳洲区域处理"条款
5. 隐私政策 + APP 合规 + 数据泄露响应计划（NDB 计划）
6. 录音同意流程：按**最严格的州（全体当事人同意）**统一设计
7. 客户合同包：MSA、DPA（数据处理协议）、试点协议
8. 信息安全基线：ACSC Essential Eight，目标 ISO 27001
9. 临床顾问（注册护士 RN）入职，建立临床安全框架
10. R&D Tax Incentive 记录从第一天开始保留
