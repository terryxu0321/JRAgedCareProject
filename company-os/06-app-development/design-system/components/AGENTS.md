# AGENTS.md — design-system/components — 组件说明与预览

> AI 助手在本目录工作前必读。全局规则：根目录 `AGENTS.md` 与 `company-os/11-rules/`。人类说明：同目录 `README.md`。完成任务后按 `changelog-rules.md` 写 `changelog/CHANGELOG.md`。

## 这个目录是什么
每个组件的用法说明 `<Name>.md` 与示例 `<Name>.preview.html`；`../build_design_html.py` 把它们和 DESIGN.md 合成 `../design-system.html`。

## 关键文件
- `<Name>.md`、`<Name>.preview.html`
- `Cover.preview.html` —— 页面封面

## 在这里工作的规则
- 规格（token、尺寸、颜色）只在 `../DESIGN.md` 定义；这里的说明和示例只引用 token 名，不写新的颜色值
- 预览只用 `var(--token)`；示例只用合成数据（如 "Sample Resident A · Room 12"）
- 预览第一行保留 `<!-- @dsCard group="…" height=N -->` 标记
- 新增组件：先在 DESIGN.md 的 YAML 与 §7 中定义，再加这两份文件，然后运行 `python company-os/06-app-development/design-system/build_design_html.py`
- 安全关键组件（ResidentIdentityChip、DraftCard、LowConfidenceMark、SectionConfirm、SystemBanner、PrivacyShield）的改动属于 safety 任务（评审人 ≠ 负责人，Clinical Lead 审阅）
