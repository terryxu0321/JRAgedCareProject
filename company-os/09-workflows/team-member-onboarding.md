---
name: team-member-onboarding
description: 新成员入职 —— 建档、更新名册与团队页、生成个人入职清单（Fair Work + NSW）
trigger: 新成员确认加入时
skills: [onboard-team-member]
inputs: [姓名, 职位, 团队, 汇报对象, 可选：雇佣类型/入职日期/城市]
outputs:
  - company-os/05-hr-teams/team-members/<name>.md
  - company-os/05-hr-teams/team-roster.md（更新）
human_checkpoints: 1
---

# 新成员入职 Team Member Onboarding

## Steps

1. 收集输入（缺少必需项就问）
2. 使用 skill `onboard-team-member`
3. 生成第一周安排（来自 `company-os/05-hr-teams/hiring-and-onboarding.md` 第 4 节），附在输出中
4. 🛑 人工确认：Terry 确认档案与清单；合同、TFN、Super、背景调查等**由人在 HR/工资系统中完成**，不在此记录
5. 列出所有修改的文件
