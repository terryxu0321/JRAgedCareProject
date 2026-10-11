---
name: CareKind Design System
version: 0.2.0
updated: 2026-10-11
source_of_truth: true
style_reference: "Terry 选定（2026-10-11）：以摄影为主、界面隐身的极简风格（参考 Apple 网站视觉语言）；按 CareKind 护理场景调整，见 §10"
colors:
  # Brand & accent — the only interactive colour
  primary: "#0066cc"            # Action Blue: links, pill CTAs (5.57:1 on canvas)
  primary-focus: "#0071e3"      # keyboard focus ring (4.70:1 on canvas)
  primary-on-dark: "#2997ff"    # links on dark surfaces (4.94:1 on surface-tile-1)
  on-primary: "#ffffff"
  # Surfaces
  canvas: "#ffffff"
  canvas-parchment: "#f5f5f7"
  surface-pearl: "#fafafc"
  surface-tile-1: "#272729"
  surface-tile-2: "#2a2a2c"
  surface-tile-3: "#252527"
  surface-black: "#000000"
  surface-chip-translucent: "rgba(210, 210, 215, 0.64)"
  scrim: "rgba(0, 0, 0, 0.48)"
  # Text
  ink: "#1d1d1f"
  on-dark: "#ffffff"
  body-muted-on-dark: "#cccccc"
  ink-muted-80: "#333333"
  ink-muted: "#6e6e73"          # CareKind: replaces #7a7a7a (failed AA: 4.29:1)
  ink-muted-on-dark: "#a1a1a6"
  # Lines
  divider-soft: "rgba(0, 0, 0, 0.04)"
  hairline: "#e0e0e0"           # decorative only (1.32:1) — never the only boundary of a control
  border-input: "#86868b"       # CareKind: input / control boundaries (3.62:1)
  # Status — CareKind addition. System states only, NEVER clinical severity (H-18, TGA)
  status-draft: "#5e3fbe"
  status-draft-bg: "#f3effc"
  status-confirmed: "#1b7f3b"
  status-confirmed-bg: "#e8f5ec"
  status-error: "#c5221f"
  status-error-bg: "#fdecea"
  status-attention: "#8a5300"   # low-confidence words to check
  status-attention-bg: "#fff4d6"
  status-offline: "#6e6e73"
  status-offline-bg: "#f5f5f7"
  # Status on dark (night theme)
  status-draft-on-dark: "#b8a4ff"
  status-confirmed-on-dark: "#5fd38a"
  status-error-on-dark: "#ff7b72"
  status-attention-on-dark: "#ffc861"
typography:
  font-display: "system-ui, -apple-system, BlinkMacSystemFont, 'SF Pro Display', Inter, 'Segoe UI', Roboto, sans-serif"
  font-text: "system-ui, -apple-system, BlinkMacSystemFont, 'SF Pro Text', Inter, 'Segoe UI', Roboto, sans-serif"
  hero-display: { size: 56px, weight: 600, line-height: 1.07, letter-spacing: -0.28px, scope: web }
  display-lg: { size: 40px, weight: 600, line-height: 1.10, letter-spacing: 0, scope: web }
  display-md: { size: 34px, weight: 600, line-height: 1.18, letter-spacing: -0.374px }
  title: { size: 28px, weight: 600, line-height: 1.14, letter-spacing: 0.196px }
  lead: { size: 28px, weight: 400, line-height: 1.14, letter-spacing: 0.196px, scope: web }
  tagline: { size: 21px, weight: 600, line-height: 1.19, letter-spacing: 0.231px }
  body-strong: { size: 17px, weight: 600, line-height: 1.24, letter-spacing: -0.374px }
  body: { size: 17px, weight: 400, line-height: 1.47, letter-spacing: -0.374px }
  dense-link: { size: 17px, weight: 400, line-height: 2.41, letter-spacing: 0, scope: web }
  caption: { size: 14px, weight: 400, line-height: 1.43, letter-spacing: -0.224px }
  caption-strong: { size: 14px, weight: 600, line-height: 1.29, letter-spacing: -0.224px }
  button: { size: 17px, weight: 600, line-height: 1.18, letter-spacing: -0.374px }
  button-utility: { size: 14px, weight: 400, line-height: 1.29, letter-spacing: -0.224px }
  fine-print: { size: 12px, weight: 400, line-height: 1.33, letter-spacing: -0.12px, scope: web }
spacing:
  xxs: 4px
  xs: 8px
  sm: 12px
  md: 16px
  lg: 24px
  xl: 32px
  xxl: 48px
  section: 80px
size:
  touch-target-min: 48px        # CareKind: gloves + one hand (Apple reference: 44px)
  control-height: 48px
  top-bar-height: 52px
  action-bar-height: 72px
rounded:
  none: 0px
  sm: 8px
  md: 11px
  lg: 18px
  pill: 9999px
  full: 50%
elevation:
  flat: none
  hairline: "0 0 0 1px rgba(0, 0, 0, 0.08)"
  frosted: "backdrop-filter: saturate(180%) blur(20px); background: rgba(245, 245, 247, 0.8)"
  media: "rgba(0, 0, 0, 0.22) 3px 5px 30px 0"   # the only drop shadow — marketing imagery only
motion:
  press: "transform: scale(0.95)"
  duration-fast: 120ms
  duration-base: 200ms
  reduce-motion: "disable scale and transitions when the OS reduce-motion setting is on"
components:
  button-primary: { bg: "{colors.primary}", fg: "{colors.on-primary}", type: "{typography.button}", radius: "{rounded.pill}", padding: "12px 24px", min-height: "{size.control-height}" }
  button-secondary-pill: { bg: transparent, fg: "{colors.primary}", border: "1px solid {colors.primary}", radius: "{rounded.pill}", padding: "12px 24px", min-height: "{size.control-height}" }
  button-dark-utility: { bg: "{colors.ink}", fg: "{colors.on-dark}", type: "{typography.button-utility}", radius: "{rounded.sm}", padding: "8px 16px", min-height: 40px, scope: admin-web }
  button-pearl-capsule: { bg: "{colors.surface-pearl}", fg: "{colors.ink-muted-80}", border: "1px solid {colors.border-input}", type: "{typography.caption}", radius: "{rounded.md}", padding: "12px 16px", min-height: "{size.control-height}" }
  button-icon-circular: { bg: "{colors.surface-chip-translucent}", fg: "{colors.ink}", radius: "{rounded.full}", size: "{size.touch-target-min}" }
  button-focus: { outline: "2px solid {colors.primary-focus}", outline-offset: 2px }
  text-link: { fg: "{colors.primary}" }
  text-link-on-dark: { fg: "{colors.primary-on-dark}" }
  card: { bg: "{colors.canvas}", border: "1px solid {colors.hairline}", radius: "{rounded.lg}", padding: "{spacing.lg}" }
  input: { bg: "{colors.canvas}", fg: "{colors.ink}", border: "1px solid {colors.border-input}", type: "{typography.body}", radius: "{rounded.sm}", min-height: "{size.control-height}", padding: "12px 16px" }
  input-error: { border: "2px solid {colors.status-error}", message: "{typography.caption} {colors.status-error}, icon + text" }
  search-input: { bg: "{colors.canvas}", border: "1px solid {colors.border-input}", radius: "{rounded.pill}", min-height: "{size.control-height}", padding: "12px 20px" }
  selection-chip: { bg: "{colors.canvas}", fg: "{colors.ink}", border: "1px solid {colors.border-input}", radius: "{rounded.pill}", padding: "12px 16px", min-height: "{size.control-height}" }
  selection-chip-selected: { border: "2px solid {colors.primary-focus}", icon: checkmark }
  top-bar-frosted: { surface: "{elevation.frosted}", height: "{size.top-bar-height}", title: "{typography.tagline}", fallback: "{colors.canvas-parchment} opaque when reduce-transparency is on" }
  action-bar: { surface: "{elevation.frosted}", height: "{size.action-bar-height}", padding: "12px 16px", primary: "{component.button-primary}" }
  resident-identity-chip: { bg: "{colors.canvas-parchment}", fg: "{colors.ink}", name: "{typography.body-strong}", second-identifier: "{typography.body}", photo: "40px {rounded.full}", radius: "{rounded.lg}" }
  draft-card: { bg: "{colors.status-draft-bg}", border: "2px dashed {colors.status-draft}", label: "AI draft", radius: "{rounded.lg}", padding: "{spacing.md}" }
  draft-card-edited: { bg: "{colors.status-draft-bg}", border: "2px solid {colors.status-draft}", label: "Edited draft" }
  draft-card-confirmed: { bg: "{colors.status-confirmed-bg}", border: "1px solid {colors.status-confirmed}", label: "Confirmed", icon: checkmark }
  low-confidence-mark: { bg: "{colors.status-attention-bg}", fg: "{colors.ink}", underline: "2px dotted {colors.status-attention}", label: "Check" }
  section-confirm: { control: "{component.selection-chip}", rule: "each key section confirmed separately; no confirm-all" }
  system-banner-offline: { bg: "{colors.status-offline-bg}", fg: "{colors.ink}", icon: offline, persistent: true }
  system-banner-error: { bg: "{colors.status-error-bg}", fg: "{colors.ink}", accent: "{colors.status-error}", icon: alert, persistent: true }
  privacy-shield: { bg: "{colors.canvas-parchment}", content: "app name only — no resident or health information" }
  # Common components (v0.2.0)
  select: { bg: "{colors.canvas}", fg: "{colors.ink}", border: "1px solid {colors.border-input}", type: "{typography.body}", radius: "{rounded.sm}", min-height: "{size.control-height}", padding: "12px 44px 12px 16px", chevron: "{colors.ink-muted}", options: "{component.menu}" }
  menu: { bg: "{colors.canvas}", border: "1px solid {colors.border-input}", radius: "{rounded.lg}", padding: "{spacing.xxs}", item-min-height: "{size.control-height}", item-type: "{typography.body}", item-selected: "checkmark + {colors.primary} text", separator: "1px {colors.hairline}" }
  checkbox: { box: "24px, 2px solid {colors.border-input}, radius {rounded.sm}", checked: "fill {colors.primary}, check {colors.on-primary}", target: "{size.touch-target-min}", label: "{typography.body}" }
  radio: { circle: "24px, 2px solid {colors.border-input}, {rounded.full}", selected: "2px solid {colors.primary} ring + 12px {colors.primary} dot", target: "{size.touch-target-min}", label: "{typography.body}" }
  switch: { track: "51x31 {rounded.pill}", off: "fill {colors.border-input}", on: "fill {colors.primary}", thumb: "27px {colors.canvas} {rounded.full}", target: "{size.touch-target-min}", label: "{typography.body}, label left, switch right" }
  textarea: { bg: "{colors.canvas}", fg: "{colors.ink}", border: "1px solid {colors.border-input}", type: "{typography.body}", radius: "{rounded.sm}", min-height: 120px, padding: "12px 16px", counter: "{typography.caption} {colors.ink-muted}" }
  date-time-input: { base: "{component.input}", date-format: "DD/MM/YYYY", time-format: "24-hour HH:MM", picker: "platform native" }
  file-upload: { zone: "{colors.canvas-parchment}, 1px solid {colors.border-input}, {rounded.lg}, padding {spacing.lg}", file-row: "{component.list-item} + {component.progress}", error: "{colors.status-error} icon + text", scope: admin-web }
  toast: { bg: "{colors.ink}", fg: "{colors.on-dark}", type: "{typography.caption}", radius: "{rounded.lg}", padding: "12px 16px", icon-success: "{colors.status-confirmed-on-dark}", action: "{colors.primary-on-dark}", duration: 4s, position: "bottom, above {component.action-bar}" }
  dialog: { scrim: "{colors.scrim}", bg: "{colors.canvas}", radius: "{rounded.lg}", padding: "{spacing.lg}", title: "{typography.tagline}", body: "{typography.body}", max-width: 400px, actions: "{component.button-primary} + {component.button-secondary-pill}, stacked on phones" }
  bottom-sheet: { scrim: "{colors.scrim}", bg: "{colors.canvas}", radius: "{rounded.lg} top corners", grabber: "36x5 {colors.border-input} {rounded.pill}", padding: "{spacing.md}" }
  progress: { track: "{colors.canvas-parchment}, 4px, {rounded.pill}", fill: "{colors.primary}", spinner: "{colors.primary}, 24px", label: "{typography.caption} {colors.ink-muted}" }
  empty-state: { title: "{typography.tagline}", body: "{typography.body} {colors.ink-muted}", action: "{component.button-secondary-pill}", align: center, padding: "{spacing.xl}" }
  status-tag: { type: "{typography.caption-strong}", fg: "{colors.ink}", radius: "{rounded.pill}", padding: "4px 12px", variants: "draft / confirmed / error / attention / offline: status-*-bg fill + status-* icon", interactive: false }
  tabs: { track: "{colors.canvas-parchment}", radius: "{rounded.pill}", padding: 2px, segment-min-height: 44px, selected: "{colors.canvas} + {elevation.hairline}, {typography.caption-strong}", unselected: "{typography.caption} {colors.ink}" }
  tab-bar: { surface: "{elevation.frosted}", height: 56px, items: "3-5, icon + {typography.caption} label", selected: "{colors.primary}", unselected: "{colors.ink-muted}", scope: mobile-app }
  side-nav: { bg: "{colors.canvas-parchment}", width: 240px, item-min-height: 40px, item-type: "{typography.body}", selected: "{colors.canvas} fill, {colors.primary} text, weight 600", radius: "{rounded.sm}", scope: admin-web }
  list-item: { min-height: 56px, padding: "12px {spacing.md}", title: "{typography.body}", secondary: "{typography.caption} {colors.ink-muted}", trailing: "chevron {colors.ink-muted}", separator: "1px {colors.hairline}, inset {spacing.md}" }
  data-table: { header: "{typography.caption-strong} {colors.ink-muted}", row-min-height: 48px, cell: "{typography.body}", numbers: tabular-nums, separator: "1px {colors.hairline}", pagination: "{component.button-secondary-pill}", scope: admin-web }
  accordion: { header-min-height: "{size.control-height}", header: "{typography.body-strong}", chevron: "{colors.ink-muted}", body: "{typography.body}", separator: "1px {colors.hairline}" }
  marketing-tile-light: { bg: "{colors.canvas}", padding: "{spacing.section} 0", radius: "{rounded.none}", scope: web }
  marketing-tile-dark: { bg: "{colors.surface-tile-1}", fg: "{colors.on-dark}", padding: "{spacing.section} 0", radius: "{rounded.none}", scope: web }
---

# CareKind Design System — DESIGN.md

> **唯一来源（SoT）**：CareKind 所有界面（护士 App `mobile-app`、管理后台 `admin-web`、营销网站）的视觉、组件与 token 以本文件为准。上方 YAML 是 token 的唯一定义；正文解释如何使用。代码、设计稿、AI 生成的界面都必须引用 `{token}`，不得内联十六进制颜色或字号。
>
> Owner: Terry（风格决定）｜ 维护：SPEC-003 Assignee（Dave）｜ 需求：[SPEC-003](../specs/2026-10-design-system.md) ｜ 规则：[AGENTS.md](AGENTS.md)

## 1. Overview 概述

风格由 Terry 选定（2026-10-11）：**界面隐身，内容做主**。参考 Apple 网站的视觉语言 —— 大量留白、单一蓝色强调色、近黑文字、浅色 / 近黑表面交替、几乎没有边框和阴影、胶囊形主按钮。

在 CareKind，"内容"不是产品照片，而是**护士的记录**。所以同一套语言翻译为：

- 记录与居民身份是主角，界面元素退后
- 只有一个强调色（蓝）表示"可以点"；**状态色**是单独一层，只表示系统状态（草稿、已确认、错误、离线、需核对），绝不表示临床严重程度
- 浅色主题用于白天与办公室；**近黑主题用于夜班**（原风格的深色区块正好对应）
- 为护理场景加强：触控目标 48px、正文 17px 起、动态字号到 200%、所有颜色组合达到 WCAG 2.2 AA（见 §10 偏差表）

**适用范围（scope）**：未标注 `scope` 的 token 与组件三端通用；`scope: web` 只用于营销网站；`scope: admin-web` 只用于管理后台。

## 2. Colors 颜色

### 强调色（唯一可交互色）
- `{colors.primary}` #0066cc —— 所有链接、主按钮、选中态。白底对比度 5.57:1
- `{colors.primary-focus}` #0071e3 —— 键盘焦点环（2px 实线）
- `{colors.primary-on-dark}` #2997ff —— 深色表面上的链接。`{colors.primary}` 在深色表面上只有 2.68:1，**不得**作为深色底上的文字

### 表面
- `{colors.canvas}` 白色：默认背景
- `{colors.canvas-parchment}` #f5f5f7：交替区块、顶栏、居民身份条背景
- `{colors.surface-pearl}` #fafafc：次要按钮填充
- `{colors.surface-tile-1/2/3}`：夜班主题的表面（1 = 默认，2 = 叠在 1 上的卡片，3 = 最底层 / 媒体）
- `{colors.surface-black}`：只用于全屏媒体背景
- `{colors.scrim}`：对话框、底部面板下方的遮罩

### 文字
- `{colors.ink}` #1d1d1f：浅色表面上的全部正文与标题（不用纯黑）
- `{colors.on-dark}` 白色：深色表面上的文字；`{colors.body-muted-on-dark}` / `{colors.ink-muted-on-dark}`：深色表面上的次要文字
- `{colors.ink-muted}` #6e6e73：次要文字、说明、元数据（5.07:1；原风格的 #7a7a7a 不达标，已替换）

### 线条
- `{colors.hairline}`：只作装饰性分隔；不得作为控件唯一的边界
- `{colors.border-input}` #86868b：输入框、选择项、次要按钮的边界（3.62:1，满足 WCAG 1.4.11）

### 状态色（CareKind 新增）

| 状态 | 前景 | 背景 | 夜班前景 | 必须同时有 |
|---|---|---|---|---|
| AI 草稿 | `status-draft` | `status-draft-bg` | `status-draft-on-dark` | 虚线边框 + 文字 "AI draft" |
| 已确认 | `status-confirmed` | `status-confirmed-bg` | `status-confirmed-on-dark` | 勾选图标 + 文字 "Confirmed" |
| 错误（系统） | `status-error` | `status-error-bg` | `status-error-on-dark` | 警示图标 + 文字说明 |
| 需核对（低置信度） | `status-attention` | `status-attention-bg` | `status-attention-on-dark` | 点状下划线 + "Check" |
| 离线 | `status-offline` | `status-offline-bg` | `ink-muted-on-dark` | 离线图标 + 文字 |

- 颜色永远不是唯一信号（WCAG 1.4.1）：每个状态都有形状、图标与文字
- **禁止**用状态色或任何颜色表示居民的风险、严重程度、优先级（如"红色 = 高跌倒风险"）—— TGA 边界（[tga-samd-assessment](../../03-legal-compliance/tga-samd-assessment.md)），建议 hazard H-18
- 无装饰性渐变

## 3. Typography 字体

- **字体栈**：`{typography.font-display}` / `{typography.font-text}` —— 先用系统字体（Apple 设备上即 SF Pro，Android 上 Roboto，Windows 上 Segoe UI），Inter 作为可打包的开源后备
- **不打包 SF Pro 字体文件**：其许可只面向 Apple 平台（未经律师核实）；我们只通过 `system-ui` 调用系统已安装的字体
- 用 Inter 替代时：显示字号再收紧 `-0.01em`；正文行高 1.47 → 1.44

| Token | 字号 / 字重 / 行高 | 用途 |
|---|---|---|
| `hero-display` | 56 / 600 / 1.07 | 营销网站主标题（web） |
| `display-lg` | 40 / 600 / 1.10 | 营销区块标题（web） |
| `display-md` | 34 / 600 / 1.18 | App 页面大标题 |
| `title` | 28 / 600 / 1.14 | 卡片组标题、居民名大号显示 |
| `tagline` | 21 / 600 / 1.19 | 顶栏标题、分组标题 |
| `body` | 17 / 400 / 1.47 | 默认正文、记录内容 |
| `body-strong` | 17 / 600 / 1.24 | 正文强调、居民姓名 |
| `button` | 17 / 600 / 1.18 | 按钮文字 |
| `caption` / `caption-strong` | 14 / 400 或 600 | 说明、元数据、次要标签 |
| `fine-print` | 12 / 400 | 只用于营销网站法律小字（web） |

规则：
- 字重只用 400 / 600（原风格的 300 细体在 App 中**不用**，弱光下难读；500 不用）
- 标题负字距；12px 及以下不用负字距
- 护士 App 与管理后台中文字不小于 14px；记录正文不小于 17px
- 支持系统动态字号放大到 200%，不截断、不重叠（必要时换行或改为纵向排列）
- 文案用简单英语（读者可能英语为第二语言），语气见 [品牌语气规则](../../07-marketing-operations/brand-and-messaging.md)

## 4. Layout 布局

- 基准单位 8px；token：`{spacing.xxs}` 4 · `xs` 8 · `sm` 12 · `md` 16 · `lg` 24 · `xl` 32 · `xxl` 48 · `section` 80（只用于营销网站区块）
- **App**：单列；左右边距 16px（平板 24px）；卡片间距 12px；主要操作放在屏幕下半部（单手拇指可达），用 `{component.action-bar}`
- **管理后台**：内容最大宽度 1440px；文字为主的页面 980px；卡片网格间距 20–24px
- **营销网站**：全宽区块浅 / 深交替，区块之间无间隙，颜色变化即分隔
- 留白优先于分隔线：先加空间，再考虑边框

## 5. Elevation 层次

| 级别 | 处理 | 用途 |
|---|---|---|
| Flat | 无阴影无边框 | 页面、区块、列表 |
| Hairline | 1px `rgba(0,0,0,0.08)` | 卡片、顶栏与内容的分隔 |
| Frosted | 80% 半透明 + 背景模糊 | 顶栏、底部操作栏；系统"减少透明度"打开时改为不透明 |
| Scrim | `{colors.scrim}` | 对话框、底部面板 |
| Media | `{elevation.media}` | **只**用于营销网站的产品图片；App 中不用阴影 |

## 6. Shapes 形状

| Token | 值 | 用途 |
|---|---|---|
| `rounded.none` | 0 | 全宽区块（web） |
| `rounded.sm` | 8px | 输入框、紧凑工具按钮、卡片内图片 |
| `rounded.md` | 11px | 次要胶囊按钮 |
| `rounded.lg` | 18px | 卡片、居民身份条、草稿卡 |
| `rounded.pill` | 9999px | 主按钮、次要胶囊按钮、搜索框、选择项 —— "这是一个操作" |
| `rounded.full` | 50% | 圆形图标按钮、居民头像 |

不混用：紧凑工具 = sm，卡片 = lg，操作 = pill。

## 7. Components 组件

### 7.1 基础组件

- **`button-primary`** —— 蓝色胶囊，`{typography.button}`，最小高度 48px。一屏最多一个主按钮。按下：`scale(0.95)`；焦点：`{component.button-focus}`
- **`button-secondary-pill`** —— 透明底蓝色描边胶囊，用于并列的第二个操作
- **`button-pearl-capsule`** —— 浅色次要按钮；边界用 `{colors.border-input}`（原风格的 3px 浅灰环对比度不足）
- **`button-dark-utility`** —— 管理后台的紧凑工具按钮（如导出、筛选），最小高度 40px（admin-web，桌面精确点击）
- **`button-icon-circular`** —— 48×48 圆形图标按钮；必须有读屏标签
- **`text-link` / `text-link-on-dark`** —— 浅色 / 深色表面上的链接
- **`card`** —— 白底、1px hairline、18px 圆角、24px 内边距，无阴影
- **`input` / `input-error`** —— 48px 高；错误时 2px 红色边框 + 图标 + 文字说明（不只靠颜色）；错误文字写"发生了什么 + 怎么改"
- **`search-input`** —— 胶囊形搜索框
- **`selection-chip` / `-selected`** —— 胶囊形选择项；选中 = 2px 焦点蓝边框 + 勾选图标
- **`top-bar-frosted`** —— 52px 半透明顶栏，左侧页面标题（`tagline`），右侧最多一个主操作
- **`action-bar`** —— 底部操作栏（单手可达），放当前页的主按钮（如 "Confirm section"）

### 7.2 安全关键组件（规格由 T-0005 定稿，Clinical Lead 审阅前不得用于生产）

| 组件 | 视觉 | 对应 hazard |
|---|---|---|
| `resident-identity-chip` | 米白底；姓名（body-strong）+ 第二标识（房号或照片）；同名居民时显示提示条 | H-03、H-09 |
| `draft-card` | 紫色**虚线**边框 + "AI draft" 标签 | H-01、H-08 |
| `draft-card-edited` | 紫色实线边框 + "Edited draft" | H-01 |
| `draft-card-confirmed` | 绿色细边框 + 勾选 + "Confirmed" + 确认人与时间 | H-08 |
| `low-confidence-mark` | 琥珀底 + 点状下划线 + "Check"，逐个点开确认 | H-02 |
| `section-confirm` | 每个关键段落单独确认；**没有**"全部确认" | H-08 |
| `system-banner-offline` / `-error` | 持续显示直到问题解决；说明内容是否已安全保存 | H-06 |
| `privacy-shield` | App 进入后台时只显示应用名；锁屏通知不含居民或健康信息 | 隐私 |

### 7.3 常用组件（v0.2.0）

**输入**
- **`select`**（下拉选择）—— 外观同 `input`，右侧 `ink-muted` 下拉箭头；选项列表用 `menu`。选项多于 7 个时改用带搜索的 `bottom-sheet`（App）或带 `search-input` 的菜单（管理后台）。手机上优先用系统原生选择器
- **`checkbox`** —— 24px 方框在 48px 点击区内；选中 = `primary` 填充 + `on-primary` 勾。标签点击也能切换
- **`radio`** —— 24px 圆；选中 = `primary` 外环 + 中心圆点。一组至少 2 项，默认不预选会影响记录内容的选项
- **`switch`** —— 只用于立即生效的设置（如夜班主题）；标签在左、开关在右。关闭 = `border-input` 轨道，开启 = `primary`。不要用开关代替"确认"
- **`textarea`** —— 外观同 `input`，最小 120px 高，可选字数提示（`caption`）
- **`date-time-input`** —— 澳洲格式：日期 DD/MM/YYYY，时间 24 小时制 HH:MM；用系统原生选择器；"现在"一键填入
- **`file-upload`**（管理后台）—— 米白上传区、**实线**边框（虚线只留给 AI 草稿）、说明可接受的格式和大小；每个文件一行：文件名 + 进度 + 移除；失败用 `status-error` 图标 + 原因 + 重试。上传的文件可能含个人信息：只上传到澳洲区域存储

**反馈**
- **`toast`** —— `ink` 底、`on-dark` 文字，底部、位于 `action-bar` 之上；4 秒后消失，同时只显示一个。只用于**已经完成**的结果（"Draft saved"），可带一个 `primary-on-dark` 的 "Undo"。需要处理的错误用 `system-banner-error`，不用 toast
- **`dialog`** —— `scrim` 遮罩 + `canvas` 卡片，`tagline` 标题，`body` 正文写清后果；手机上按钮纵向堆叠，主操作在上。删除等不可撤销操作必须用对话框确认，按钮文字写动作本身（"Delete draft"），不用红色按钮
- **`bottom-sheet`** —— App 中的选项列表、筛选、次要操作；顶部 36×5 拖动条，可下滑关闭
- **`progress`** —— 进度条（已知进度）或圆形加载（未知进度），都配文字说明（"Uploading 2 of 5"）；超过 10 秒的等待必须显示进度条和剩余说明
- **`empty-state`** —— 居中：一句标题 + 一句说明 + 一个次要按钮，告诉用户下一步做什么（"No drafts yet. Dictate your first note."）
- **`status-tag`** —— 不可点击的小胶囊，表示**记录或系统**状态（Draft、Confirmed、Synced、Offline、Check）；状态色背景 + 状态色图标 + `ink` 文字。**绝不**用来标记居民的风险、病情或优先级

**导航**
- **`tabs`**（分段控件）—— 同一页面内 2–4 个视图切换（如 "To review / Confirmed"）；米白轨道，选中段为白底
- **`tab-bar`**（App）—— 底部主导航，3–5 项，图标 + 文字；选中 `primary`。只出现在一级页面；详情页用 `action-bar`
- **`side-nav`**（管理后台）—— 左侧 240px 米白导航；选中项白底 + `primary` 文字 + 600 字重（不用左侧色条）
- **`menu`**（操作下拉菜单）—— `canvas` 底、`border-input` 细边、`rounded-lg`，每项 48px 高；不用阴影。也是 `select` 的选项列表

**数据展示**
- **`list-item`** —— 最小 56px 高；主文字 `body`、次要文字 `caption` + `ink-muted`、右侧箭头；分隔线 `hairline` 从左边距开始
- **`data-table`**（管理后台）—— 表头 `caption-strong` + `ink-muted`，行高 48px，数字等宽对齐，只用横向 `hairline` 分隔，无斑马纹；分页用 `button-secondary-pill`。窄屏时表格在自己的容器内横向滚动
- **`accordion`** —— 48px 标题行（`body-strong` + 箭头），展开显示正文；用于说明、设置分组，不用于隐藏需要审核的记录内容

### 7.4 营销网站组件（scope: web）

`marketing-tile-light` / `marketing-tile-dark`：全宽区块交替；标题 `display-lg`、一句话副标题、最多两个胶囊按钮、一张图。图片只用授权的真实护理场景，**不用真实居民照片**（除非有书面同意）。

## 8. Do / Don't

**Do**
- 所有可点击元素用 `{colors.primary}`（深色表面用 `{colors.primary-on-dark}`）
- 正文 17px / 400 / 1.47；标题 600 + 负字距
- 状态用"颜色 + 形状 + 图标 + 文字"四件套
- 主要操作放在底部操作栏，48px 起
- 按下态统一 `scale(0.95)`，并尊重"减少动态效果"
- 先用留白和表面颜色变化分组，再考虑边框

**Don't**
- 不加第二个品牌强调色；状态色不用于按钮或链接
- 不用任何颜色、徽章、图标表示居民的临床风险、严重程度或优先级（TGA）
- App 中不加阴影、不加渐变
- 不用 300 细体，不用 500 字重；App 中不出现小于 14px 的文字
- 不把 `{colors.hairline}` 当作控件唯一边界
- 不提供"全部一键确认"
- 虚线边框只用于 AI 草稿（`draft-card`），其他组件（包括上传区）一律实线
- 错误不用 toast：需要用户处理的问题用 `system-banner-error` 或行内错误；不可撤销的操作用 `dialog` 确认，不用红色按钮
- 设计稿、组件文档、截图中不出现真实居民信息（只用合成数据）

## 9. Responsive 响应式

| 端 | 断点 | 变化 |
|---|---|---|
| App 手机 | < 600dp | 单列；底部操作栏；大标题 34 → 28 |
| App 平板 | ≥ 600dp | 审核页可左右分栏（原文 / 草稿对照）；边距 24 |
| 管理后台 | 834 / 1068 / 1440px | 网格 2 → 3 → 4 列；1440px 锁定内容宽度 |
| 营销网站 | 419 / 640 / 834 / 1068 / 1440px | 主标题 56 → 40 → 34 → 28；区块内边距 80 → 48 |

触控目标最小 48×48（管理后台桌面工具按钮可为 40px 高）。

## 10. 与参考风格的偏差（CareKind 调整）

| 项 | 参考风格 | CareKind | 原因 |
|---|---|---|---|
| 次要灰字 | #7a7a7a | #6e6e73 | 原值 4.29:1，不满足 AA 4.5:1 |
| 控件边界 | #e0e0e0 / 4% 黑 | `border-input` #86868b | 原值 1.32:1，不满足 WCAG 1.4.11 的 3:1 |
| 触控目标 | 44px | 48px | 手套、单手（SPEC-003 §5.2） |
| 细体 300 | 少量使用 | App 中禁用 | 夜班弱光可读性 |
| 最小字号 | 10–12px | App 14px | 可读性、动态字号 |
| 错误 / 状态 | 未定义 | 新增状态色层 | 审核流程与 hazard 缓解需要 |
| 字体 | SF Pro | system-ui + Inter 后备 | 许可与跨平台（Android、Web） |
| 半透明顶栏 | 始终半透明 | 减少透明度时不透明 | 对比度与系统设置 |
| 阴影 | 产品图片专用 | App 不用 | 无产品图片场景 |

## 11. 维护（Iteration guide）

1. 一次只改一个组件；在 YAML 中改，再改正文说明
2. 新颜色必须先算对比度（正文 ≥ 4.5:1，大字与控件 ≥ 3:1），把比值写在 YAML 注释里
3. 变体（`-selected`、`-error`、`-on-dark`）在 `components:` 中单独成项
4. 版本号：新增 = 次版本，改值 / 删除 = 主版本；在 `changelog/CHANGELOG.md` 记录
5. 拿不准时：先加留白或换表面，再加装饰

## 12. 已知缺口

- 安全关键组件的交互细节、动效与读屏文案：T-0005（Dave）
- 无障碍走查清单：T-0003；无障碍相关法律尚未进入本地法律文件：T-0009
- 平台 token 产物（iOS / Android / Web）与 CI 对比度检查：T-0007（等移动端技术栈 DR）
- 图标集未选定（需开源许可、线性风格、48px 内可识别）
- 夜班主题下的管理后台不在范围内（管理后台默认浅色）
