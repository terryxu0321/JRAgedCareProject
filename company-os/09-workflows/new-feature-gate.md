---
name: new-feature-gate
description: 新功能闸门 —— 开发前完成 spec、合规/TGA 检查与临床 hazard 识别，必要时起草决策记录
trigger: 每个新功能进入开发之前
skills: [spec-writer, compliance-check, decision-record]
inputs: [功能想法, 可选：相关反馈文件名]
outputs:
  - company-os/06-app-development/specs/YYYY-MM-<feature>.md
  - company-os/03-legal-compliance/checks/YYYY-MM-DD_<feature>.md
  - company-os/02-operating-rhythm/decisions/DR-NNN-<title>.md（需要时）
human_checkpoints: 2
---

# 新功能闸门 New Feature Gate

对应 [路线图 · 功能评估闸门](../01-strategy/roadmap.md) 的四个问题。

## Steps

0. 按 [产品设计与 PRD 法律参考规范](../11-rules/product-legal-rules.md)，通过 [法律参考索引](../11-rules/legal-reference-index.md) 查阅本功能相关的本地法律文件
1. 使用 skill `spec-writer` 起草 spec（含"法律依据"章节）
2. 使用 skill `compliance-check`（类型：feature）检查 spec
3. 判断闸门结果：
   - **TGA 判定改变**（会生成诊断/治疗/用药建议）→ ❌ 停止，使用 skill `decision-record` 起草 Type 1 DR，说明是否走医疗器械路径
   - **新数据类型 / 新子处理方 / 新 AI 模型** → 在输出中列出需要的 PIA 与子处理方清单更新
   - **新临床 hazard** → 在 spec 中列出建议的 hazard 条目，标注需 Clinical Lead 审阅
4. 运行 `python company-os/11-rules/check_rules.py`，不通过则回到第 1 步补充"法律依据"
5. 🛑 人工确认：Terry（Product Owner + Tech Lead）审阅 spec 与检查结果
6. 🛑 人工确认：涉及 AI 输出或临床内容 → 须 Clinical Lead 签字（未招到前，记录为"待 Clinical Lead"，不得标记为可发布）
7. 输出闸门结论：✅ 可进入开发 / ⚠️ 有条件 / ❌ 不通过，及所有文件路径
