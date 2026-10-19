# CareKind Design System（设计系统）

| 项 | 内容 |
|---|---|
| 文档 ID | SPEC-003 |
| 类型 | 产品基础设施：护士 App（`mobile-app`）与管理后台（`admin-web`）共用的视觉、交互、文案与无障碍规范 + 组件库 |
| 版本 | v0.1 草稿 · 2026-10-11 |
| Owner | Terry（Product Owner + Tech Lead） |
| Assignee | Dave |
| 状态 | 🟡 **待 Terry 审阅**（🛑 人工确认）；安全关键组件（§5.3）待 Clinical Lead（待招）审阅 |
| 难度 | **L3**（[PRD 分配规范](../../11-rules/prd-assignment-rules.md) §2）：§5.3 组件承载 HITL 审核与 H-03/H-08 等 hazard 的缓解措施；涉及 2 个模块 |
| 目标 | Foundations v1：2026-11-06（与 M0 原型同步）；组件代码 v1：技术栈 DR 后 4 周 |
| 合规检查 | [有条件通过](../../03-legal-compliance/checks/2026-10-11_design-system.md) |
| 关联 | [docs/PRD.md](../../../docs/PRD.md) C1 架构、C3 归属、D2 审核流程、E7 非功能需求；[品牌与信息](../../07-marketing-operations/brand-and-messaging.md)；[临床安全框架](../clinical-safety-framework.md)；[工程规范](../engineering-standards.md)；`src/mobile-app/AGENTS.md`、`src/admin-web/AGENTS.md` |

> ⚠️ 本文中的法律判断为内部工作底稿，不构成法律意见。本 spec 不改变产品边界（TGA、录音模式、HITL、数据驻留），无需 Type 1 DR。

---

## 1. 问题

- 目前没有统一的视觉与交互规范：`brand-and-messaging.md` 中"视觉"仍是"待设计"（色彩"温暖但专业（待定）"）
- PRD E7 要求"大按钮、单手操作、高对比度；WCAG 2.2 AA"，但没有落到可执行的 token 和组件
- 审核界面的安全设计（第二标识、低置信度高亮、逐段确认、草稿与已确认的区分）分散在 PRD 与 hazard log 中，没有统一组件，各页面容易做得不一致 → 直接放大 H-03、H-08 风险
- 护士原话：用户访谈尚未开始（`08-feedback/raw/` 为空），**不引用、不编造**；§8 的可用性测试是第一手证据来源

## 2. 目标与度量

| 目标 | 度量 | 目标值 |
|---|---|---|
| 无障碍达标 | 自动检查（axe 等）严重问题数；token 颜色对的对比度 | 0 个严重问题；正文 ≥ 4.5:1，大字与 UI 元素 ≥ 3:1 |
| 审核安全 | 可用性测试中"确认了错误居民"或"未察觉 AI 草稿状态"的次数 | 0 |
| 一致性 | 新页面使用组件库组件的比例（评审时检查） | ≥ 90%，例外须写原因 |
| 效率 | 护士完成"口述 → 审核 → 确认一条记录"的操作步数与时间（合成数据原型） | 基线在 M0 测得后设定，不预设数字 |

## 3. 使用者与场景

- **护士 / 护理员**（主要）：夜班光线暗、戴手套、单手持设备、频繁被打断、英语可能是第二语言
- **DON / 管理员**：在办公室用 `admin-web` 管理名册、同意状态、审计
- **团队**：设计与开发共用同一套 token 与组件；AI 助手（Claude Code、Codex）生成界面代码时必须使用组件库

## 4. 范围 / 不做什么

**做**：设计原则 → design tokens → 基础组件 → CareKind 安全关键组件 → 文案与语气规范 → 无障碍规范 → token 构建与 CI 检查 → 文档站

**不做**：
- 营销网站与宣传物料的完整视觉（只共用 token；对外发布走[市场合规](../../07-marketing-operations/marketing-compliance.md)）
- 任何表示**临床严重程度、风险等级、预警**的视觉组件（如居民"红/黄/绿风险"标签、跌倒风险徽章）—— TGA 边界，见 §6
- 在技术栈 DR 之前写平台组件代码（token 先以平台无关的 JSON 定义）

## 5. 内容

### 5.1 设计原则

1. **护士做主**：AI 内容永远以"草稿"呈现，确认动作明确、不可误触
2. **一眼认清是谁**：凡出现居民的地方，同时显示姓名与第二标识（照片或房号）
3. **在困难条件下可用**：夜班、手套、单手、被打断后能回到原处
4. **安静而清楚**：温暖但专业；颜色只表达**系统状态**，不表达临床判断
5. **失败要说清楚**：离线、上传失败、低置信度都要明确可见，绝不静默

### 5.2 Foundations（design tokens，平台无关 JSON）

| 类别 | 要求 |
|---|---|
| 颜色 | 品牌色 + 中性色 + 系统状态色（草稿、已确认、错误、离线、低置信度）；每个前景/背景组合登记对比度；浅色与深色（夜班）两套主题 |
| 字体 | 支持系统动态字号放大到 200% 不截断；正文默认不小于 17pt（iOS）/ 16sp（Android）/ 16px（Web）|
| 触控 | 主要操作目标 ≥ 48×48 dp（高于 WCAG 2.2 AA 2.5.8 的 24×24 CSS px 下限，考虑手套与单手）；相邻目标留间距 |
| 间距 / 圆角 / 阴影 / 动效 | 4 pt 网格；动效可被"减少动态效果"系统设置关闭 |

### 5.3 CareKind 安全关键组件（safety-related）

| 组件 | 作用 | 对应 hazard |
|---|---|---|
| 居民身份条 Resident Identity Chip | 姓名 + 第二标识（照片 / 房号）；同名居民时额外提示 | H-03、H-09 |
| AI 草稿卡 Draft Card | "AI 草稿 / 已修改 / 已确认"三态，形状 + 文字 + 图标区分，不只靠颜色 | H-01、H-08 |
| 低置信度标记 Low-confidence Mark | 高亮需核对的词（药名、剂量、数字、姓名），可逐个确认 | H-02 |
| 逐段确认控件 Section Confirm | 关键项须逐段确认后才能整体确认；不提供"全部一键确认" | H-08 |
| 原文 / 译文对照 Source Compare | 多语言输入时并排显示原文与译文 | H-07 |
| 状态横幅 System Banner | 离线、上传失败、已本地保存 —— 明确、持续可见 | H-06 |
| 隐私遮罩 Privacy Shield | App 切换到后台时遮住记录内容；锁屏通知不显示健康信息 | 隐私（§6） |

### 5.4 基础组件

按钮、输入框、列表、卡片、对话框、底部操作栏、Toast、标签页、导航、空状态、加载状态。每个组件都要有：用途、状态（默认 / 按下 / 禁用 / 焦点 / 错误）、无障碍说明（读屏标签、焦点顺序）、正反例。

### 5.5 文案与语气（UI 文案）

沿用[品牌语气规则](../../07-marketing-operations/brand-and-messaging.md)：说 "draft" 不说 "automatic notes"；用 "residents / the people you care for"；不出现 detects / predicts / diagnoses / early warning 等暗示医疗器械用途的词。错误信息写"发生了什么 + 你的内容是否安全 + 下一步"。文案用简单英语（目标读者可能英语为第二语言）。

### 5.6 交付物与位置

- 规范与 token：**[design-system/DESIGN.md](../design-system/DESIGN.md)**（唯一来源，YAML token + 用法）。风格由 Terry 于 2026-10-11 选定（极简、单一蓝色强调色、浅 / 近黑表面），并按 §5.2 的无障碍要求调整
- 平台产物与构建脚本：由 DESIGN.md 生成，随代码仓库（技术栈 DR 后确定，T-0007）
- 设计稿工具：待定（如需新 SaaS，按[运营规范](../../11-rules/operations-rules.md)审批支出；**只放合成数据**）

## 6. 法律依据 Legal References

> 查阅日期：2026-10-11 ｜ 依据 [法律参考索引](../../11-rules/legal-reference-index.md)

| 话题 | 本地文件（章节） | 对设计的影响 |
|---|---|---|
| AI 功能边界（TGA） | [tga-samd-assessment.md](../../03-legal-compliance/tga-samd-assessment.md)（功能闸门表："跌倒风险评分" = 器械）；[federal-law-summary.md](../../03-legal-compliance/research/federal-law-summary.md) §3 | 不设计风险等级、临床预警、严重程度色标组件；状态色只表示系统状态；禁用词进入文案规范（§5.5） |
| 护士对 AI 记录的责任 | [federal-law-summary.md](../../03-legal-compliance/research/federal-law-summary.md) §0 第 10 点、§4（Ahpra/NMBA） | AI 内容必须显式标为草稿，由护士逐段确认后才成为记录（§5.3 草稿卡、逐段确认） |
| 记录质量（Quality Standards 2.7、3.3） | [aged-care-alignment.md](../../03-legal-compliance/aged-care-alignment.md)；[federal-law-summary.md](../../03-legal-compliance/research/federal-law-summary.md) §1.4 | 记录须"accurate and current"、可被理解 → 低置信度标记、原文对照、清晰的确认状态 |
| 居民权利与尊严 | [aged-care-alignment.md](../../03-legal-compliance/aged-care-alignment.md)；[federal-law-summary.md](../../03-legal-compliance/research/federal-law-summary.md) §1.2 | 文案用尊重的称呼；示例与插图不使用真实居民照片 |
| 隐私、健康信息 | [privacy-program.md](../../03-legal-compliance/privacy-program.md) §2、§3 | 隐私遮罩、锁屏通知不含健康信息；组件文档、截图、设计稿只用合成数据 |
| 营销与对外宣称 | [marketing-compliance.md](../../07-marketing-operations/marketing-compliance.md) | 若 token 用于对外物料，发布前走市场合规清单 |
| 无障碍（残障歧视法） | ⚠️ **本地文件未覆盖** | WCAG 2.2 AA 目前来自 PRD E7 的产品决定。按 L-4，须先用 skill `regulatory-watch` 把 Disability Discrimination Act 1992 与数字无障碍要求补进 `03-legal-compliance/`，再引用（任务 T-0009） |

**需律师确认**：客户（养老机构）采购时是否要求 WCAG 合规声明，以及 CareKind 作为软件供应商在 DDA 下的义务范围（待 T-0009 补充本地文件后确认）。
**合规检查**：[checks/2026-10-11_design-system.md](../../03-legal-compliance/checks/2026-10-11_design-system.md)

## 7. 检查

- [x] 法律依据已填写，`python company-os/11-rules/check_rules.py` 通过
- [x] TGA 判定：是否生成诊断 / 治疗 / 用药建议？**否**；明确禁止风险等级类视觉组件
- [ ] 临床 hazard 已加入 hazard log —— **建议**（待 Clinical Lead 审阅后由人加入）：
	- **H-17** AI 草稿与已确认记录视觉区分不清，未审核内容被当作正式记录 → 缓解：三态草稿卡、形状 + 文字 + 图标区分、可用性测试
	- **H-18** 组件被误用来表示临床严重程度（如红色"高风险"标签），造成误导并触碰 TGA 边界 → 缓解：组件库不提供此类组件；评审清单检查
- [x] 隐私：无新数据类型；设计材料只用合成数据；无需新 PIA
- [ ] 新子处理方：设计工具待定 —— 不放个人信息，但新 SaaS 仍按运营规范审批
- [x] 可访问性与多语言：本 spec 的核心内容

## 8. 评测计划

| 评测 | 方法 | 通过标准 |
|---|---|---|
| 对比度 | 脚本检查所有登记的 token 颜色对 | 全部达标（§2） |
| 自动无障碍检查 | 组件文档站与示例页跑 axe 等工具，进 CI | 0 个严重问题 |
| 读屏与动态字号 | VoiceOver、TalkBack、200% 字号手动走查清单 | 清单全部通过 |
| 可用性测试 | 用合成数据原型，招募护士顾问（≥ 5 人），模拟夜班光线、手套、单手、被打断 | 0 次确认错误居民；0 次未察觉草稿状态；记录任务完成率与问题 |
| 临床审阅 | Clinical Lead 审阅 §5.3 组件与 H-17、H-18 | 签字（未到岗时记录"待 Clinical Lead"，不阻止 Foundations，但阻止组件用于生产） |

## 9. 任务分配

**Assignee（PRD 负责人）**：**Dave**（Senior）—— Terry 于 2026-10-11 确认。本 spec 为 L3，按[分配规范](../../11-rules/prd-assignment-rules.md) §1 须 Senior 或 Lead 担任；分配前 Dave 负责 0 份 PRD。按规范 §3a"整份 PRD 归一人"，本 spec 的**全部任务**由 Dave 负责并执行；评审人为 Terry（评审人 ≠ 执行者，ADLC AS-2）。

任务文件在 [`adlc/tasks/`](../adlc/tasks/README.md)（格式按 [ADLC spec](2026-10-adlc-delivery-lifecycle.md) §6.1）。由 Terry 于 2026-10-11 确认，状态 `ready`。

| 任务 | 内容 | 执行 | 评审 | 阶段 / 截止（建议） |
|---|---|---|---|---|
| T-0001 | 视觉方向与设计原则：两套视觉方向供 Terry 选 | Dave | Terry | 1 · 10-17 |
| T-0009 | 用 `regulatory-watch` 补充无障碍法律到本地文件 | Claude Code（AI，代 Dave 执行） | Terry | 1 · 10-17 |
| T-0002 | Design tokens：颜色（含对比度登记、深色主题）、字体、触控、间距、动效 | Dave | Terry | 1 · 10-24 |
| T-0003 | 无障碍规范与走查清单（WCAG 2.2 AA、读屏、动态字号、手套 / 单手） | Dave | Terry | 1 · 10-24 |
| T-0006 | UI 文案与语气规范 | Dave | Terry | 1 · 10-24 |
| T-0007 | Token 构建管线与 CI（对比度检查、无障碍检查、版本发布） | Dave | Terry | 2 · 10-31 |
| T-0004 | 基础组件设计规格 | Dave | Terry | 2 · 11-06 |
| T-0005 | 安全关键组件设计规格（§5.3）🔒 safety | Dave | Terry（+ Clinical Lead） | 2 · 11-06 |
| T-0008 | 可用性测试（合成数据原型，≥ 5 位护士顾问） | Dave | Terry | 3 · 11-20 |

依赖：T-0007 的平台产物与组件代码须等技术栈 DR（[工程规范](../engineering-standards.md)"技术栈（建议，待 DR 确认）"）。截止日按一人执行排列；Dave 同时 `in-progress` 的任务不超过 3 个（ADLC §6.2 WIP 上限），实际进度以站会为准。

## 10. 待决问题

| # | 问题 | 负责人 |
|---|---|---|
| 1 | 🛑 审阅本 spec 正文（Assignee 与 §9 任务分配已于 2026-10-11 确认） | Terry |
| 2 | 设计工具选型（是否引入新 SaaS） | Terry |
| 3 | ~~移动端技术栈 DR（React Native / Flutter）~~ —— 已定（Terry 2026-10-19）：第一阶段为 React + TypeScript Web App，不做原生 App；组件代码按 React + TS 实现 | Terry |
| 4 | H-17、H-18 是否加入 hazard log | Clinical Lead（待招） |
| 5 | Matt 的级别（影响能否承担更多任务） | Terry |
