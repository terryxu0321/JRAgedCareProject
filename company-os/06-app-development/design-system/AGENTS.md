# AGENTS.md — 06-app-development/design-system — 设计系统

> AI 助手在本目录工作前必读。全局规则：根目录 `AGENTS.md` 与 `company-os/11-rules/`。人类说明：同目录 `README.md`。完成任务后按 `changelog-rules.md` 写 `changelog/CHANGELOG.md`。

## 这个目录是什么
CareKind 设计规范。`DESIGN.md` 是唯一来源（YAML token + 用法说明）。

## 关键文件
- `DESIGN.md` —— token 与组件规范（SoT）
- `components/` —— 每个组件的用法说明与预览
- `build_design_html.py` → `design-system.html` —— 生成的离线单文件页面，**不要手改**；修改 DESIGN.md 或 `components/` 后重新运行脚本并一起提交
- `../specs/2026-10-design-system.md` —— SPEC-003 需求、法律依据、任务分配

## 在这里工作的规则
- **任何 UI 工作**（mobile-app、admin-web、营销页面、原型）先读 `DESIGN.md`，只用其中的 token 与组件；不内联颜色 / 字号，不另建第二份 token 文件
- 新颜色必须先算 WCAG 对比度（正文 ≥ 4.5:1，大字与控件 ≥ 3:1）并写在 YAML 注释里
- **禁止**设计表示居民临床风险、严重程度、优先级的颜色或组件（TGA 边界，建议 hazard H-18）
- 安全关键组件（§7.2）的改动属于 safety 任务：评审人 ≠ 负责人，Clinical Lead 审阅前不得用于生产
- 示例、截图、设计稿只用合成数据；不使用真实居民照片
- 不打包 SF Pro 等专有字体文件；不使用他人商标、Logo
- 风格或 token 的破坏性改动（改值、删除）须 Terry 确认，并升主版本号
