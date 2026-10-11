# 战略 Strategy

> Owner: CEO ｜ 状态: 草稿 v0.1 ｜ 复审: 每季度规划会

## 1. 市场判断

- 澳洲 aged care 正处于监管重塑期：Aged Care Act 2024 与 Strengthened Quality Standards（2025-11-01 生效）把"记录"变成了证明合规的核心证据
- 机构面临：24/7 RN 与 care minutes 要求、人手短缺、CALD 员工比例高、审核压力、SIRS 上报时效
- 记录是护士最不喜欢、但最不能出错的工作 —— 这是我们的切入点

## 2. 目标客户（ICP）

**首要 ICP（Beachhead）**：
- 澳洲**中小型机构养老提供者**（residential aged care），1–10 个机构（facility）
- 已使用电子护理管理系统（clinical/care management system），但护士仍在手工录入大量文本
- 决策人：Director of Nursing（DON）/ Clinical Care Manager；经济决策人：CEO/COO；把关人：IT 与隐私负责人

**第二阶段**：大型连锁提供者、Support at Home 居家养老提供者

**用户**：RN、EN、PCW/AIN（重点关注 CALD 背景的护理员）

## 3. 产品定位

> **CareKind AI：护士说，AI 写，护士审核签字。**

| 维度 | 我们的选择 |
|---|---|
| 核心任务 | progress notes、ADL、incident 记录草稿、handover 摘要、wound/behaviour 观察记录 |
| 输入 | 语音（班后口述或护理过程中简述）、简短关键词、多语言输入 → 英文专业记录 |
| 输出 | 结构化、符合机构模板的记录草稿 → **护士审核确认** → 推送/复制到机构护理系统 |
| 差异化 | ① 专为 aged care 设计（不是 GP scribe 改造）② 多语言输入 ③ 对齐 Quality Standards 的记录完整性提示 ④ 澳洲数据驻留与透明 AI 治理 |
| 明确边界 | 不做诊断、不做治疗/用药建议、不做风险评分决策（见 [TGA 自评](../03-legal-compliance/tga-samd-assessment.md)） |

## 4. 商业模式（假设，待验证）

- SaaS 订阅，按**床位（per bed）/ 月**或按**活跃用户 / 月**计价
- 付费试点（paid pilot）6–8 周 → 年度合同
- 集成服务费（与主流护理管理系统对接）

## 5. 竞争格局

> 详细调研（2026-10-10）：[competitor-research](../07-marketing-operations/competitor-research/README.md)

| 类型 | 示例 | 我们的应对 |
|---|---|---|
| AI scribe 进入 aged care | **Heidi Health**（已推出 aged care 产品：多语言口述→英文记录、离线挂绳录音设备；2026-09 融资 US$340M）—— **头号威胁**；Lyrebird（数据澳洲驻留，约 $160/clinician/月） | 差异化：面向 PCW 与 CALD 护理员而非仅 RN、Quality Standards 映射、**回写现有护理系统**（Heidi 未公开 AU 护理系统集成） |
| 澳洲机构养老护理系统 | Telstra Health、Leecare、AutumnCare、Person Centred Software、eCase（Evaran）—— 调研时**均未发现生成式 AI 记录功能** | 成为集成/合作伙伴；优先接触 **Leecare**（已集成第三方工具 CAREFUL）与 **Telstra Health**。海外同类（PointClickCare、Access、Birdie）已内置 AI → 窗口期估计 12–24 个月 |
| 居家养老（Support at Home）平台 | AlayaCare、Lookout、ShiftCare（AI 已含在 A$8–9/用户/月套餐） | 该细分已拥挤，**首阶段聚焦机构养老** |
| 大型提供者自建 | Uniting NSW.ACT 的 "Buddy"（多语言语音记录，1,200+ 员工，记录耗时 15 分钟→<2 分钟） | 证明需求真实；对中小提供者，自建不可行 → 我们的 ICP |
| 小型直接竞争者 | AccuNote、MediQo Health、Minikai、AI Healthcare | 持续跟踪 |
| 现状（手写/手工录入） | — | 用试点数据证明节省时间与质量提升 |

**定价启示**：按床位或按机构计价，避开按护士计价与通用工具（ShiftCare 等）的低价对比。

## 6. 关键风险

| 风险 | 缓解 |
|---|---|
| AI 生成错误内容（幻觉）进入护理记录 | 强制人工审核、来源可追溯、临床安全框架、质量监控 |
| 被认定为医疗器械 | 严格产品边界 + 功能变更前 TGA 判定流程 |
| 隐私/数据泄露 | 澳洲驻留、加密、最小化、NDB 计划、网络保险 |
| 录音同意争议 | 全体当事人同意的统一标准、居民/代理人同意流程 |
| 销售周期长 | 付费试点 + 行业协会/展会渠道 + DON 口碑 |
| 集成难度 | 先做"复制粘贴/导出"MVP，再逐个系统集成 |
