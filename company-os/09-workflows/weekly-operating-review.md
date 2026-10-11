---
name: weekly-operating-review
description: 每周运营回顾 —— 分析本周用户反馈，生成周报草稿，供周一例会使用
trigger: 每周五（可定时）
skills: [feedback-synthesis, weekly-update]
inputs: [周期（默认本周一至今天）]
outputs:
  - company-os/07-marketing-operations/feedback-insights/YYYY-MM-DD_synthesis.md
  - company-os/02-operating-rhythm/weekly/YYYY-Www.md
human_checkpoints: 1
---

# 每周运营回顾 Weekly Operating Review

## Steps

1. 确定周期（默认本周一至今天），说明所用日期
2. 检查 `company-os/08-feedback/raw/` 本周是否有新文件（**只读**）
   - 有 → 使用 skill `feedback-synthesis`
   - 无 → 记录"本周无新反馈"，跳到第 3 步
3. 使用 skill `weekly-update` 生成周报草稿，引用第 2 步的 insights 文件
4. 检查周报中 🟡/🔴 的 KR，为每个列出一个"下周建议动作"
5. 🛑 人工确认：Terry 审阅周报草稿，补充"待填"项（指标、信心值）
6. 列出所有输出文件
