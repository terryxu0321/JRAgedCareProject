# DraftCard

AI 起草的记录在护士确认之前，永远以"草稿"的样子出现；三种状态用边框形状、图标和文字区分，不只靠颜色（hazard H-01、H-08，建议 H-17）。

- `draft-card` —— `status-draft-bg` 底、2px **虚线** `status-draft` 边框、标签 "AI draft"、`rounded-lg`、内边距 `spacing-md`。
- `draft-card-edited` —— 2px **实线** `status-draft` 边框、标签 "Edited draft"。
- `draft-card-confirmed` —— `status-confirmed-bg` 底、1px `status-confirmed` 边框、"✓ Confirmed" + 确认人与时间。
- 记录正文用 `body`（17px），不缩小。
- 卡片顶部放 `resident-identity-chip` 或居民姓名 + 第二标识。
- 夜班主题用 `status-draft-on-dark`、`status-confirmed-on-dark`。
- 不要：用状态色表示临床严重程度；在草稿上提供"全部确认"。
- 安全关键组件：规格由任务 T-0005 定稿，Clinical Lead 审阅前不得用于生产。
