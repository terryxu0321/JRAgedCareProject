# 09 · Workflows 工作流

> Owner: Terry（Tech Lead）｜ Claude Code 与 Codex 均可执行

Workflow = 多步骤的完整流程，由若干 [skills](../10-skills/README.md) 组成，带人工检查点。

## 如何运行

**交互式（推荐）** —— 在项目根目录打开 Claude Code 或 Codex，直接说：

> 运行 workflow weekly-operating-review

- Claude Code：也可输入 `/run-workflow weekly-operating-review`
- Codex：也可输入 `$run-workflow weekly-operating-review`

**非交互 / 定时自动执行**（在项目根目录）：

```bash
# Claude Code（headless）
claude -p "运行 workflow weekly-operating-review"

# Codex
codex exec "运行 workflow weekly-operating-review"
```

非交互模式下，workflow 执行到 🛑 人工检查点前的所有步骤，把待确认事项写在输出文件顶部，然后结束 —— **不会自动跳过人工确认**。

定时：可用 Windows 任务计划程序（Task Scheduler）调用上面的命令，或使用 Claude Code 的 `/schedule`（云端定时任务）。

> 自动执行需要工具有写文件和联网（regulatory-watch）权限；首次运行建议用交互模式确认权限设置。

## 工作流清单

| Workflow | 触发/节奏 | 用到的 skills | 输出 |
|---|---|---|---|
| [weekly-operating-review](weekly-operating-review.md) | 每周五 | feedback-synthesis → weekly-update | 周报草稿、反馈洞察 |
| [monthly-compliance-review](monthly-compliance-review.md) | 每月第一个周一 | regulatory-watch → compliance-check | 法规监测报告、登记册修改建议 |
| [new-feature-gate](new-feature-gate.md) | 每个新功能开发前 | spec-writer → compliance-check → decision-record | spec、合规检查、（需要时）DR |
| [team-member-onboarding](team-member-onboarding.md) | 新成员加入时 | onboard-team-member | 档案、名册、入职清单 |
| [incident-response](incident-response.md) | 发生安全/隐私/临床事件时 | compliance-check、decision-record | 事件日志、复盘草稿 |

## Workflow 文件格式

```markdown
---
name: <kebab-case，与文件名相同>
description: <一句话>
trigger: <何时运行>
skills: [skill-a, skill-b]
inputs: [必需输入]
outputs: [写入路径]
human_checkpoints: <数量>
---

# 标题
## Steps
1. ...（"使用 skill `x`"）
2. 🛑 人工确认：...
```

新增 workflow 不需要同步脚本 —— `run-workflow` skill 直接读取本文件夹。
