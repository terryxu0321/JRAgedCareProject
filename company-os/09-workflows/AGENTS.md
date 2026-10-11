# AGENTS.md — 09-workflows — 工作流

> AI 助手在本目录工作前必读。全局规则：根目录 `AGENTS.md` 与 `company-os/11-rules/`。人类说明：同目录 `README.md`。完成任务后按 `changelog-rules.md` 写 `changelog/CHANGELOG.md`。

## 这个目录是什么
多步骤流程，由 skill `run-workflow` 执行，带人工检查点。

## 关键文件
- `weekly-operating-review.md`
- `monthly-compliance-review.md`
- `new-feature-gate.md`
- `team-member-onboarding.md`
- `incident-response.md`

## 在这里工作的规则
- 🛑 人工检查点必须停下；非交互模式下把待确认事项写在输出顶部后结束
- 只写 workflow 声明的 outputs 位置
- 新增 workflow 按 README 中的格式（frontmatter + Steps）
