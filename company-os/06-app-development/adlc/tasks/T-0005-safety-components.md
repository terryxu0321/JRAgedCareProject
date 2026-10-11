---
task:
  id: T-0005
  title: 安全关键组件设计规格（身份条、草稿卡、低置信度、逐段确认、原文对照、状态横幅、隐私遮罩）
  prd: SPEC-003
  requirements: [SPEC-003 §5.3]
  type: design
  status: ready
  priority: P0
  owner: dave
  executor: dave
  reviewer: terry
  safety_related: true
  hazards: [H-01, H-02, H-03, H-06, H-07, H-08, H-09]
  rdti: none
  rnd_log: ""
  due: 2026-11-06
  created: 2026-10-11
  updated: 2026-10-11
---

## 背景
[SPEC-003](../../specs/2026-10-design-system.md) §5.3。这些组件承载 HITL 审核与多项 hazard 的缓解措施，属于 safety 任务：评审人 ≠ 负责人（AS-3），Clinical Lead 审阅后才能用于生产。

## 验收标准
- [ ] 7 个组件的规格：用途、状态、交互、读屏说明、正反例
- [ ] 居民身份条始终显示姓名 + 第二标识；同名提示
- [ ] 草稿卡三态（AI 草稿 / 已修改 / 已确认）用形状 + 文字 + 图标区分，不只靠颜色
- [ ] 逐段确认：不提供"全部一键确认"
- [ ] 无任何表示临床风险等级的视觉（H-18、TGA）
- [ ] 建议 hazard H-17、H-18 的缓解措施写入规格
- [ ] Clinical Lead 审阅（未到岗时记录"待 Clinical Lead"）

## 执行记录（只追加）

## 评审结论
