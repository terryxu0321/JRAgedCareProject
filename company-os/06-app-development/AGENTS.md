# AGENTS.md — 06-app-development — App 开发

> AI 助手在本目录工作前必读。全局规则：根目录 `AGENTS.md` 与 `company-os/11-rules/`。人类说明：同目录 `README.md`。完成任务后按 `changelog-rules.md` 写 `changelog/CHANGELOG.md`。

## 这个目录是什么
产品原则、临床安全框架、AI 治理、信息安全、工程规范、specs、R&D 记录与代码（`src/`）。

## 关键文件
- `product-principles.md`
- `product-feature-map.md` —— MVP 功能 → spec 映射与 best practice 汇总
- `clinical-safety-framework.md` —— hazard log
- `ai-governance.md`
- `engineering-standards.md`
- `security/`
- `specs/`
- `design-system/DESIGN.md` —— 设计规范唯一来源（token + 组件）；任何 UI 工作先读
- `adlc/tasks/` —— 任务文件
- `rnd-log/`
- `src/` —— 代码与模块说明

## 在这里工作的规则
- 产品范围以 `docs/PRD.md` 为准；新功能走 workflow `new-feature-gate`
- 写代码前读 `company-os/11-rules/code-rules.md`（核心 15 条、Tab 缩进宽度 4、单文件 ≤ 1000 行）
- 不修改 hazard log，只在 spec 中提出建议条目
- 实验记录写入 `rnd-log/`（R&D Tax Incentive 证据）
