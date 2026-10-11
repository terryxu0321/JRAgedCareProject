# Components 组件说明与预览

每个组件两份文件：

- `<Name>.md` —— 用法说明（何时用、使用者提供什么、Do / Don't）
- `<Name>.preview.html` —— 示例页面，只引用 `var(--token)`，由 `../build_design_html.py` 注入 DESIGN.md 的 token 后放进 `../design-system.html`

第一行 `<!-- @dsCard group="…" height=N subtitle="…" -->` 决定组件在页面中的分组、预览高度和副标题。`Cover.preview.html` 是页面顶部的封面。

组件的规格（token、尺寸）以 [../DESIGN.md](../DESIGN.md) 为准；这里只放说明和示例。
