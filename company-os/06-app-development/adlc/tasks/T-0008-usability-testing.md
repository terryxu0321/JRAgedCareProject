---
task:
  id: T-0008
  title: 可用性测试（合成数据原型，≥ 5 位护士顾问）
  prd: SPEC-003
  requirements: [SPEC-003 §8]
  type: eval
  status: ready
  priority: P1
  owner: dave
  executor: dave
  reviewer: terry
  safety_related: false
  hazards: [H-03, H-08]
  rdti: supporting
  rnd_log: ""
  due: 2026-11-20
  created: 2026-10-11
  updated: 2026-10-11
---

## 背景
[SPEC-003](../../specs/2026-10-design-system.md) §8。依赖 T-0004、T-0005。招募护士顾问须遵守[运营规范](../../../11-rules/operations-rules.md)；访谈原始记录由人写入 `08-feedback/raw/`，AI 不写。

## 验收标准
- [ ] 测试计划：任务脚本（口述 → 审核 → 确认）、夜班光线 / 手套 / 单手 / 被打断场景
- [ ] 原型只用合成数据
- [ ] ≥ 5 位参与者；记录"确认错误居民""未察觉草稿状态"次数（目标 0）与任务完成情况
- [ ] 结论与改进建议写入 `07-marketing-operations/feedback-insights/` 与 R&D 记录（`rnd_log` 填路径）

## 执行记录（只追加）

## 评审结论
