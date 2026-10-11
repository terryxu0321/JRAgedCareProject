---
task:
  id: T-0009
  title: 补充无障碍法律到本地法律文件（DDA 1992、数字无障碍）
  prd: SPEC-003
  requirements: [SPEC-003 §6]
  type: compliance
  status: ready
  priority: P0
  owner: dave
  executor: claude-code
  reviewer: terry
  safety_related: false
  hazards: []
  rdti: none
  rnd_log: ""
  due: 2026-10-17
  created: 2026-10-11
  updated: 2026-10-11
---

## 背景
[SPEC-003](../../specs/2026-10-design-system.md) §6：本地法律文件未覆盖无障碍 / 残障歧视法，按 product-legal-rules L-4 须先补充再引用。执行者为 AI，负责人 ≠ 评审人（AS-4）。

## 验收标准
- [ ] 用 skill `regulatory-watch` 调研：Disability Discrimination Act 1992 对软件 / 数字服务的适用、Australian Human Rights Commission 关于数字无障碍的指引、政府与养老机构采购中的 WCAG 要求
- [ ] 结论写入 `03-legal-compliance/research/`（注明来源与查阅日期），更新 `11-rules/legal-reference-index.md` 加"无障碍"话题
- [ ] 更新 SPEC-003 §6 "无障碍"一行，链接到新本地文件
- [ ] 列出需律师确认的问题；标注"内部工作底稿，非法律意见"

## Agent brief
- 先读：`company-os/11-rules/product-legal-rules.md`、`legal-reference-index.md`、`10-skills/regulatory-watch/SKILL.md`、`03-legal-compliance/AGENTS.md`
- 约束：不修改合规登记册（根目录硬规则 6，只提建议）；不对外发送；引用官方来源
- 完成定义：上面四项验收全部勾选，`check_rules.py` 通过，CHANGELOG 已写
- 🛑 停在：需要修改合规登记册或改变产品边界时，停下等 Terry

## 执行记录（只追加）

## 评审结论
