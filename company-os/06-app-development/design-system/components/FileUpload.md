# FileUpload

管理后台的文件上传（如导入名册 CSV）：米白上传区、**实线**边框，每个文件一行显示进度。

- 上传区：`canvas-parchment` 底、1px `border-input` 实线、`rounded-lg`、内边距 `spacing-lg`；写清可接受的格式与大小，并提供 "Choose file" 按钮（拖放是附加方式，不是唯一方式）。
- 虚线边框只留给 AI 草稿，上传区不用虚线。
- 文件行：文件名（`body`）+ 大小（`caption`）+ `progress` + 移除按钮；完成后显示 "✓ Uploaded"。
- 失败：`status-error` 图标 + 原因（"File is larger than 5 MB"）+ "Retry"。
- 上传的文件可能含个人信息：只存储在澳洲区域，日志不记录文件内容。
