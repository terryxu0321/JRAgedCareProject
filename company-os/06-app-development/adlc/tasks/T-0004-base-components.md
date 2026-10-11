---
task:
  id: T-0004
  title: 基础组件设计规格
  prd: SPEC-003
  requirements: [SPEC-003 §5.4]
  type: design
  status: ready
  priority: P1
  owner: dave
  executor: dave
  reviewer: terry
  safety_related: false
  hazards: []
  rdti: none
  rnd_log: ""
  due: 2026-11-06
  created: 2026-10-11
  updated: 2026-10-11
---

## 背景
[SPEC-003](../../specs/2026-10-design-system.md) §5.4。依赖 T-0002（tokens）、T-0003（无障碍清单）。2026-10-11 Terry 要求把常用组件标准化：基础规格已写入 [DESIGN.md](../../design-system/DESIGN.md) v0.2.0 §7.1、§7.3（含 select、checkbox、radio、switch、textarea、date-time-input、file-upload、toast、dialog、bottom-sheet、progress、empty-state、status-tag、tabs、tab-bar、side-nav、menu、list-item、data-table、accordion），并有[可视页面](https://claude.ai/artifact/CbgRvJbxBDYAiVv3zZCa6k)。本任务改为：按 T-0003 走查清单逐个核对与补全（状态、读屏文案、动态字号 200% 表现），直接修改 DESIGN.md。

## 验收标准
- [ ] 按钮、输入框、列表、卡片、对话框、底部操作栏、Toast、标签页、导航、空状态、加载状态
- [ ] 每个组件：用途、全部状态（默认 / 按下 / 禁用 / 焦点 / 错误）、读屏标签与焦点顺序、正反例
- [ ] 只用 T-0002 的 token，不引入新颜色或字号
- [ ] 通过 T-0003 走查清单

## 执行记录（只追加）

## 评审结论
