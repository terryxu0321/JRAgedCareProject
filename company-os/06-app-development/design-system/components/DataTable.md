# DataTable

管理后台的数据表：表头安静、行高 48px、只用横线分隔，数字等宽对齐。

- 表头 `caption-strong` + `ink-muted`；单元格 `body`；数字列右对齐、`tabular-nums`。
- 只用 1px `hairline` 横线，不用竖线和斑马纹。
- 状态列用 `status-tag`；行操作用 `menu`。
- 分页：底部 "Previous / Next"（`button-secondary-pill`）+ "Showing 1–20 of 64"（`caption`）。
- 窄屏时表格在自己的容器里横向滚动，页面本身不横向滚动。
- 审计日志等表格只显示必要字段，不显示健康信息正文。
