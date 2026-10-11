# SystemBanner

离线或出错时的持续横幅：一直显示到问题解决，并说明护士的内容是否已安全保存（hazard H-06）。

- `system-banner-offline` —— `status-offline-bg` 底、`ink` 文字、离线符号。
- `system-banner-error` —— `status-error-bg` 底、`ink` 文字、`status-error` 警示符号。
- 文字三段式：发生了什么 + 内容是否安全 + 下一步（如 "Retry"）。
- 放在顶栏下方，不遮挡记录内容；不自动消失。
- 只表示**系统**状态，不表示居民的任何临床状况。
- 读屏：`role="status"`（离线）或 `role="alert"`（错误）。
- 安全关键组件：规格由任务 T-0005 定稿，Clinical Lead 审阅前不得用于生产。
