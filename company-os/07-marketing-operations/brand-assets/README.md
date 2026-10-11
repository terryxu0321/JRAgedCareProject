# 品牌素材 Brand Assets

> Owner: CEO ｜ 品牌说明见 [brand-and-messaging.md](../brand-and-messaging.md)

Logo 方案 C「声音里的心」：心形（关怀）里的声波（口述记录）。不使用十字、心电图、听诊器等医疗符号（TGA 边界，见 [市场合规](../marketing-compliance.md)）。

## 文件

| 文件 | 用途 |
|---|---|
| `carekind-logo-horizontal.svg` | 主 logo（浅色背景）：官网页头、one-pager、文档 |
| `carekind-logo-horizontal-dark.svg` | 深色背景版（透明底，用于 `#1F5F5B` 或更深的背景） |
| `carekind-mark.svg` | 单独图形标志（浅色背景），≥ 40px |
| `carekind-mark-mono.svg` | 单色版（`currentColor`）：传真、印章、单色打印 |
| `carekind-app-icon.svg` | App 图标（圆角方形，导出 PNG 时用 512px 或 1024px） |
| `carekind-favicon.svg` | ≤ 32px 的小尺寸：3 条声波、加粗线条，避免糊在一起 |

## 吉祥物：考拉小记

护士身边安静、可靠的记录伙伴。几何化平面风格（圆 + 椭圆，无描边、无渐变），标志性元素：青绿围巾、记事本、珊瑚声波。

| 文件 | 用途 |
|---|---|
| `mascot-koala-hello.svg` | 打招呼：引导页、欢迎邮件 |
| `mascot-koala-writing.svg` | 记录中：录音、草稿生成中 |
| `mascot-koala-done.svg` | 完成：护士确认提交后 |
| `mascot-koala-avatar.svg` | 头像：帮助中心、通知 |

使用边界：只用于护士端 App、培训、展会和内部周边；不穿护士服、不戴听诊器或十字，不出现在护理记录里，不用于给长者或家属的资料。

## PNG（透明背景）

`png/` 下是上面 SVG 的透明背景 PNG：横版 logo 1240 × 320，图形标志、App 图标、吉祥物 1024 × 1024，头像 512 × 512。PNG 里的文字是用系统字体（Segoe UI）渲染的，因为本机没有装 Nunito；需要严格一致时，先在设计工具里把文字转轮廓再导出。

## VI 手册

吉祥物设计风格、VI 基础规范、办公与数字应用、周边设计：设计画布 <https://claude.ai/artifact/AvKzpWHZzenJsXKbVcsLYo>（默认私有，需在页面的 Share 菜单分享）。

## 与 DESIGN.md 的分工

产品界面和网站的颜色、字体只用 [DESIGN.md](../../06-app-development/design-system/DESIGN.md) 的 token。下面的颜色只属于 logo、吉祥物、周边和印刷品，在界面里以图片形式出现，不作为界面 token 使用。

## 颜色

| 名称 | 色值 | 用途 |
|---|---|---|
| Deep Teal | `#1F5F5B` | 主色、声波、"Care" 文字 |
| Coral | `#E8875B` | 心形线条（图形，不用于文字） |
| Coral Text | `#C2410C` | 白底上的 "Kind" 文字（对比度约 5:1，WCAG AA） |
| Coral Light | `#F0A07E` | 深色背景上的心形与 "Kind" |
| Warm Gray | `#5F5E5A` | "AI" 字样 |

## 使用规则

- 不拉伸、不改颜色、不加阴影或渐变；四周留白 ≥ 心形高度的 1/4
- 文字部分使用 Nunito 字体（缺省时回退到系统字体）。**交付印刷或外部供应商前，需在设计工具里把文字转成轮廓（outline）**，否则在没装字体的电脑上效果会变
- 状态：内部草稿，尚未做商标检索（IP Australia），对外使用前需确认
