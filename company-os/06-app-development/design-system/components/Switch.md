# Switch

只用于**立即生效**的设置（如夜班主题、提示音）：标签在左、开关在右。

- 轨道 51×31 `rounded-pill`；关闭 = `border-input`，开启 = `primary`；滑块 27px `canvas` 圆。
- 整行 48px 高，整行可点。
- 不要用开关代替"确认"或"提交"，也不要用在表单里等待保存的字段上（用 `checkbox`）。
- 读屏：`role="switch"` + `aria-checked`。
