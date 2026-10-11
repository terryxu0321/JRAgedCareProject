---
name: monthly-compliance-review
description: 月度合规检查 —— 扫描澳洲/NSW 法规变化，复核合规登记册状态，提出更新建议
trigger: 每月第一个周一（可定时）
skills: [regulatory-watch, compliance-check]
inputs: [月份（默认本月）]
outputs:
  - company-os/03-legal-compliance/regulatory-watch/YYYY-MM.md
human_checkpoints: 2
---

# 月度合规检查 Monthly Compliance Review

## Steps

1. 使用 skill `regulatory-watch`（需要联网）
2. 复核 `company-os/03-legal-compliance/compliance-register.md`：
   - 列出所有 ⬜/🟡 条目及其 Owner，标出超过 30 天无进展的
   - 列出本月或下月生效的 👀 条目（如 2026-12-10 自动化决策透明义务）
   - 把结果追加到同一份 regulatory-watch 报告的"登记册状态"一节
3. 若有新法规影响已上线或开发中的功能：对受影响的 spec 使用 skill `compliance-check`
4. 🛑 人工确认：Terry 审阅报告，决定哪些登记册修改建议被采纳
5. 仅在用户明确批准后：按批准的内容更新合规登记册，并在顶部"最近核实"日期处更新
6. 🛑 人工确认：列出需要提交律师的问题清单，由 Terry 决定是否发出（**不自动发送**）
