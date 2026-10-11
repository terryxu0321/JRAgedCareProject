# Select

下拉选择：外观与 `input` 一致，右侧 `ink-muted` 箭头，选项列表用 `menu` 的样式。

- 48px 高、`border-input` 边界、`rounded-sm`；选中值用 `ink`，未选时占位文字用 `ink-muted`。
- 打开后：选项每项 48px，当前值前有 "✓" 并用 `primary` 文字。
- 选项多于 7 个：App 改用带搜索的 `bottom-sheet`，管理后台在菜单顶部加 `search-input`。
- 手机上优先用系统原生选择器。
- 标签在上方（`caption-strong`），不能只用占位文字。
