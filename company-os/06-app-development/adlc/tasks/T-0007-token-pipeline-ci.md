---
task:
  id: T-0007
  title: Token 构建管线与 CI（对比度检查、无障碍检查、版本发布）
  prd: SPEC-003
  requirements: [SPEC-003 §5.6, SPEC-003 §8]
  type: code
  status: ready
  priority: P1
  owner: dave
  executor: dave
  reviewer: terry
  safety_related: false
  hazards: []
  rdti: none
  rnd_log: ""
  due: 2026-10-31
  created: 2026-10-11
  updated: 2026-10-11
---

## 背景
[SPEC-003](../../specs/2026-10-design-system.md) §5.6、§8。依赖 T-0002 的 token JSON。平台产物（iOS / Android / Web）须等移动端技术栈 DR；在此之前先做 Web（CSS 变量）与检查。

## 验收标准
- [ ] 从 token JSON 生成 Web 产物（CSS 变量）；平台产物留接口，待技术栈 DR
- [ ] 对比度检查脚本：所有登记的颜色对，不达标时 CI 失败
- [ ] 组件示例页的自动无障碍检查进 CI（0 个严重问题）
- [ ] token 变更有版本号与变更说明
- [ ] 遵守 code-rules（Tab 缩进、类型标注、无空 catch、最少依赖）；新依赖写明理由

## 执行记录（只追加）

## 评审结论
