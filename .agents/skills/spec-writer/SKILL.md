---
name: spec-writer
description: Draft a CareKind AI product feature spec or PRD with the mandatory legal-references (based on local legal files in company-os/03-legal-compliance), TGA, privacy, clinical-safety and evaluation sections. Use for "产品设计",  "写需求", "写 spec", "PRD", "新功能需求文档", "feature spec".
---

# spec-writer

## 输入
- 功能想法（一句话即可）
- 相关用户反馈（可选：`08-feedback/raw/` 中的文件名，**只读引用**）

## 参考
- **`company-os/11-rules/product-legal-rules.md`（必须遵守）与 `company-os/11-rules/legal-reference-index.md`（查找本地法律文件）**
- `docs/PRD.md`（总 PRD；spec 不得与其冲突，并链接回对应章节）
- `company-os/06-app-development/specs/README.md`（模板）
- `company-os/06-app-development/product-principles.md`
- `company-os/06-app-development/clinical-safety-framework.md`
- `company-os/03-legal-compliance/tga-samd-assessment.md`

## 步骤
0. **先查本地法律文件**：按 `legal-reference-index.md` 找出与本功能相关的话题，阅读对应的 `company-os/03-legal-compliance/` 文件（工作文件 → research 总结 → 必要时 downloads 原件）。本地文件没有覆盖的问题，先用 skill `regulatory-watch` 补充到本地，再引用；不能只凭记忆或网络搜索
1. 用模板起草：问题（引用护士原话时注明来源文件，**原话逐字引用，不改写**）、目标与度量、用户流程、范围/不做什么
2. 对照产品原则自查（HITL、忠实于输入、可追溯、失败要安全）
3. 填写检查项：TGA 判定、可能的临床 hazard（建议 H-编号与内容）、隐私影响、新子处理方
4. 写评测计划（评测集、指标、Clinical Lead 抽样）
5. 填写 **"法律依据 Legal References"** 章节（模板见 `product-legal-rules.md`）：每个话题列出本地文件链接、相关章节和对设计的具体影响
6. 使用 skill `compliance-check` 检查草稿，把结论链接进 spec 与"法律依据"章节
7. 运行 `python company-os/11-rules/check_rules.py`，必须通过
8. 🛑 人工确认：Product Owner（Terry）审阅

## 输出
`company-os/06-app-development/specs/YYYY-MM-<feature-name>.md`

## 禁止
- 不设计诊断/治疗/用药建议类功能；如用户要求，说明 TGA 影响并建议先写 DR
- 不直接修改 hazard log —— 在 spec 中列出建议新增项
