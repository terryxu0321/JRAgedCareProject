# Dialog

需要用户停下来决定时才用：`scrim` 遮罩 + `canvas` 卡片，标题说问题，正文说后果。

- 卡片 `rounded-lg`、内边距 `spacing-lg`、最宽 400px；标题 `tagline`，正文 `body`。
- 按钮：主操作 `button-primary` + 取消 `button-secondary-pill`；手机上纵向堆叠，主操作在上。
- 按钮文字写动作本身（"Delete draft" / "Keep draft"），不写 "OK / Cancel"。
- 不可撤销的操作（删除草稿）必须用对话框确认；**不用红色按钮**，后果写在正文里。
- 打开时焦点移到对话框内，关闭后回到触发按钮；`role="dialog"` + `aria-modal="true"`。
