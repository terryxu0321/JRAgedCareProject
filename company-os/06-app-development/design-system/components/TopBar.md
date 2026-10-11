# TopBar

52px 高的半透明顶栏：左边是页面标题，右边最多一个操作。

- `top-bar-frosted` —— 80% `canvas-parchment` + 背景模糊，底部 `elevation-hairline`；高度 `size-top-bar-height`。
- 标题用 `tagline`（21px / 600）。
- 右侧操作用 `text-link` 或一个小号主按钮；返回按钮用 48×48 的点击区。
- 系统开启"减少透明度"时改为不透明的 `canvas-parchment`，保证文字对比度。
- 固定在顶部时加上安全区内边距。
