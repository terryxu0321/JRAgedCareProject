# Button

胶囊形蓝色主按钮是唯一的"主操作"信号；其他按钮安静地退后。

**变体**
- `button-primary` —— `primary` 填充、`on-primary` 文字、`rounded-pill`、`button` 字样，最小高度 `size-control-height`（48px）。一屏最多一个。
- `button-secondary-pill` —— 透明底、`primary` 1px 描边与文字。与主按钮并列时作为第二个操作。
- `button-pearl-capsule` —— `surface-pearl` 填充、`ink-muted-80` 文字、`border-input` 边界、`rounded-md`。卡片内的次要操作。
- `button-dark-utility` —— `ink` 填充、`on-dark` 文字、`rounded-sm`，40px 高。只用于管理后台的桌面工具按钮（导出、筛选）。
- `button-icon-circular` —— 48×48、`surface-chip-translucent`、`rounded-full`。必须有读屏标签（`aria-label`）。

**状态**：按下 `scale(0.95)`；键盘焦点 2px `primary-focus` 实线环、2px 间距；禁用时文字 `ink-muted` 并移除点击。不记录悬停态。

**使用者提供**：动词开头的标签（"Confirm section"、"Save draft"）、点击处理、图标按钮的 `aria-label`。

**不要**：不用状态色做按钮；不把两个主按钮并排；按钮不加阴影。
