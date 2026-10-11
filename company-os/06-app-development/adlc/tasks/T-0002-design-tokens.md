---
task:
  id: T-0002
  title: Design tokens（颜色、字体、触控、间距、动效）
  prd: SPEC-003
  requirements: [SPEC-003 §5.2]
  type: design
  status: ready
  priority: P0
  owner: dave
  executor: dave
  reviewer: terry
  safety_related: false
  hazards: []
  rdti: none
  rnd_log: ""
  due: 2026-10-24
  created: 2026-10-11
  updated: 2026-10-11
---

## 背景
[SPEC-003](../../specs/2026-10-design-system.md) §5.2。T-0001 已完成：基础 token 已在 [DESIGN.md](../../design-system/DESIGN.md) YAML 中（含首批对比度）。本任务负责校验、补全夜班主题与动态字号表现，并直接修改 DESIGN.md（唯一来源），不另建 token 文件。

## 验收标准
- [ ] 平台无关的 token JSON（颜色、字体、间距、圆角、阴影、动效），浅色与深色两套主题
- [ ] 系统状态色：草稿、已确认、错误、离线、低置信度；**不含**任何临床风险 / 严重程度色（§4、H-18）
- [ ] 每个前景 / 背景组合登记对比度：正文 ≥ 4.5:1，大字与 UI 元素 ≥ 3:1
- [ ] 字号支持放大到 200%；主要触控目标 ≥ 48×48 dp
- [ ] 动效可随"减少动态效果"关闭

## 执行记录（只追加）

## 评审结论
