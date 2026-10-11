# Input

48px 高的文本输入框，边界用 `border-input`，出错时用图标加文字说明，不能只靠颜色。

- `input` —— `canvas` 底、`ink` 文字、`body` 字样、1px `border-input`、`rounded-sm`、内边距 12×16。
- `input-error` —— 2px `status-error` 边框，下方 `caption` 字号的 `status-error` 说明，前面带警示符号。说明写"哪里不对 + 怎么改"。
- 焦点：2px `primary-focus` 环。
- 每个输入框都要有可见的标签（不能只用占位文字），标签在上方，`caption-strong`。
- 使用者提供：标签、可选的帮助文字、错误文字。
