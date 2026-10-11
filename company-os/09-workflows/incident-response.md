---
name: incident-response
description: 事件响应 —— 安全/隐私/临床安全事件的记录、NDB 评估辅助与复盘草稿（辅助人做决定，不替代）
trigger: 发现疑似数据泄露、安全事件或临床安全问题时
skills: [compliance-check, decision-record]
inputs: [事件描述, 发现时间, 发现人]
outputs:
  - company-os/03-legal-compliance/incidents/INC-YYYY-NNN.md
human_checkpoints: 3
---

# 事件响应 Incident Response

> ⚠️ 这是辅助流程。**遏制措施、是否通知 OAIC/客户/个人，由人决定并执行。** 依据：`company-os/03-legal-compliance/data-breach-response-plan.md`

## Steps

1. 立即提醒用户：先通知事件负责人（Privacy Officer / Terry），按数据泄露响应计划第 1 步遏制（隔离系统、吊销凭据、保留证据）
2. 建立事件日志 `company-os/03-legal-compliance/incidents/INC-YYYY-NNN.md`：时间线、已采取动作、决策人。**不记录任何可识别居民的信息**，只记录类别与数量
3. 分类：SEV1（居民安全/数据泄露）/ SEV2 / SEV3；类型：临床安全 / 隐私 / 安全 / 可用性
4. 若涉及个人信息：按 NDB 三个问题整理评估材料（未授权访问/披露？可能严重伤害？补救是否消除风险？），并计算 30 天评估截止日期
5. 🛑 人工确认：是否构成"合格数据泄露"由 Privacy Officer 决定（必要时咨询律师）
6. 起草通知草稿（客户、OAIC 表格要点、受影响个人）—— **只生成草稿，不发送**
7. 🛑 人工确认：通知内容与发送由人完成
8. 事件结束后：按 `company-os/templates/incident-postmortem.md` 起草复盘；需要流程变更时使用 skill `decision-record`
9. 🛑 人工确认：复盘审阅，更新 hazard log / 合规登记册的建议由 Terry 批准
