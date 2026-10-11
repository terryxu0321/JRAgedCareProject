# Card

白底卡片，用 `hairline` 细边和 `rounded-lg` 圆角，不加阴影。

- `card` —— `canvas` 底、1px `hairline`、`rounded-lg`（18px）、内边距 `spacing-lg`。
- 卡片之间用 `spacing-sm`；放在 `canvas-parchment` 上时，表面变化本身就是分隔。
- 夜班主题：`surface-tile-2` 叠在 `surface-tile-1` 上，不需要边框。
- 标题 `body-strong`，元数据 `caption` + `ink-muted`。
- 不要给每个区块都套卡片：只有需要成为独立对象的内容才用。
