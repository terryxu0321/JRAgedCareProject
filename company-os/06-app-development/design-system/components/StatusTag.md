# StatusTag

不可点击的小胶囊，标出**记录或系统**的状态：Draft、Confirmed、Synced、Offline、Check。

- `caption-strong`、`ink` 文字、`rounded-pill`、内边距 4×12；背景 `status-*-bg`，前面的符号用对应 `status-*` 颜色。
- 每个标签都有文字，颜色不是唯一信号。
- **绝不**用来标记居民的风险、病情、优先级或"重点关注"——这会越过 TGA 的产品边界（建议 hazard H-18）。
- 不可点击，所以不需要 48px 高；需要点击的筛选用 `selection-chip`。
