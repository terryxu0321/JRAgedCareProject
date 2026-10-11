# ResidentIdentityChip

凡出现居民的地方，同时显示姓名和第二标识（房号或照片），减少把记录归到错误居民的风险（hazard H-03、H-09）。

- `resident-identity-chip` —— `canvas-parchment` 底、`rounded-lg`；姓名 `body-strong`，第二标识 `body`；头像 40px `rounded-full`（没有照片时显示姓名首字母）。
- **同名提示**：名册中有相同或相近姓名时，在下方显示一行提示（`caption-strong` + 符号），要求核对第二标识。
- 照片只用于人工核对，不做人脸识别。
- 使用者提供：显示名、房号或照片、是否存在同名居民。
- 示例只用合成数据。
- 安全关键组件：规格由任务 T-0005 定稿，Clinical Lead 审阅前不得用于生产。
