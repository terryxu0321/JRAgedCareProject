# Menu

操作下拉菜单（点"更多"按钮后出现）；也是 `select` 的选项列表样式。

- `canvas` 底、1px `border-input`、`rounded-lg`、4px 内边距；**不用阴影**。
- 每项 48px 高、`body` 字样；当前选中项前有 "✓" 并用 `primary`。
- 分组之间用 1px `hairline` 分隔。
- 不可撤销的项（如 "Delete draft"）放在最后、用分隔线隔开，点击后弹出 `dialog` 确认；不用红色文字。
- 键盘：上下键移动、Enter 选择、Esc 关闭并把焦点还给触发按钮。
