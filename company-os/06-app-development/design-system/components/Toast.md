# Toast

短暂提示一个**已经完成**的结果（"Draft saved"），4 秒后消失；需要处理的错误不用 toast。

- `ink` 底、`on-dark` 文字（`caption`）、`rounded-lg`、内边距 12×16；成功图标用 `status-confirmed-on-dark`。
- 可带一个操作链接（如 "Undo"），颜色 `primary-on-dark`；有操作时延长到 8 秒。
- 位置：屏幕底部，在 `action-bar` 或 `tab-bar` 之上；同时只显示一个。
- 读屏：`role="status"`。
- 不要：用 toast 报告需要用户处理的错误（用 `system-banner-error` 或行内错误）；在 toast 中写居民信息。
