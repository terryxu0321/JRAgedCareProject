# Progress

告诉用户系统正在做什么：已知进度用进度条，未知进度用圆形加载，都配文字。

- 进度条：4px 高、`canvas-parchment` 轨道、`primary` 填充、`rounded-pill`；上方 `caption` + `ink-muted` 文字（"Uploading 2 of 5"）。
- 圆形加载：24px、`primary`；旁边写在做什么（"Writing draft…"）。
- 超过 10 秒的等待必须用进度条并说明还要多久或还剩几项。
- 读屏：`role="progressbar"` + `aria-valuenow`；系统开启"减少动态效果"时圆形加载改为静态图标 + 文字。
