---
name: onboard-team-member
description: Add a new CareKind AI team member - create their profile, add them to the team roster and onboarding compliance checklist, and list Fair Work/NSW onboarding steps. Use for "新成员入职", "加一个团队成员", "onboard", "add team member", "新员工".
---

# onboard-team-member

## 输入（缺少就问，不要猜）
- 姓名、职位、团队、汇报对象
- 可选：雇佣类型（全职/兼职/临时/承包商）、入职日期、工作城市

## 步骤
1. 读 `company-os/05-hr-teams/team-roster.md` 与 `team-members/README.md`，确认此人不存在
2. 以已有档案（如 `team-members/ahmad.md`）为格式，新建 `team-members/<firstname-lowercase>.md`；未知字段写 `[待填]`
3. 在 `team-roster.md` 名册表与"每人入职合规"表各加一行/一列
4. 在 `team-members/README.md` 表格加一行；更新对应 `teams/<team>/README.md` 的成员
5. 若雇佣类型为承包商：在输出中提醒 sham contracting 判定与 IP 转让条款
6. 输出一份本人适用的入职清单（来自 `hiring-and-onboarding.md`，含 NSW：icare 工伤、Workplace Surveillance 14 天通知）

## 禁止
- 不记录薪酬、TFN、银行、住址、签证细节、健康信息、背景调查结果
- 不推断此人的性别或代词（文中用姓名或"他们/they"）
