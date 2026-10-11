---
name: run-workflow
description: Run a CareKind AI company workflow defined in company-os/09-workflows/ step by step. Use when the user says "run workflow X", "运行 workflow", "执行工作流", "跑一下周报流程/合规月检/新功能闸门/入职流程", or names any file in 09-workflows.
---

# run-workflow

执行 `company-os/09-workflows/` 中定义的工作流。

## 步骤

1. **定位 workflow**：在 `company-os/09-workflows/` 中找到与用户请求匹配的文件（按文件名或 frontmatter 的 `name`）。找不到 → 列出可用 workflow 并询问。
2. **读取全文**，包括 frontmatter 中的 `inputs`、`outputs`、`skills`、`human_checkpoints`。
3. **收集输入**：缺少必需输入时，先问用户；可推断的（如今天日期、本周范围）直接推断并说明。
4. **逐步执行** workflow 的 Steps：
   - 步骤写"使用 skill `X`"时，读取 `company-os/10-skills/X/SKILL.md` 并按其执行
   - 每完成一步，用一句话报告结果
5. **人工检查点**：到达 `🛑 人工确认` 的步骤时，**停下**，展示草稿/结论，等待用户确认后再继续。非交互模式（如 `claude -p`、`codex exec`）下：完成检查点之前的所有步骤，把待确认事项写入输出文件顶部的"待人工确认"区，然后结束。
6. **结束**：列出所有新建/修改的文件路径，以及待人工处理的事项。

## 规则

- 只写入 workflow 声明的 `outputs` 位置
- 遵守 `company-os/10-skills/README.md` 的共同红线（尤其：不碰 `08-feedback/raw/`、不对外发送）
- 任何步骤失败：停止、说明原因，不跳过
