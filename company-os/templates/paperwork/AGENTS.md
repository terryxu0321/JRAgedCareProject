# AGENTS.md — templates/paperwork — 养老护理 Paperwork 模板

> AI 助手在本目录工作前必读。全局规则：根目录 `AGENTS.md`、上级 `company-os/templates/AGENTS.md` 与 `company-os/11-rules/`。人类说明：同目录 `README.md`。完成任务后按 `changelog-rules.md` 写 `changelog/CHANGELOG.md`。

## 这个目录是什么
CareKind AI MVP 的关键 paperwork Markdown 模板：5 个机构护理记录结构（CareKind 起草 → 护理人员审核签字）+ 3 个上线与合规文件（居民 AI 告知同意、员工监控通知、机构上线清单）。字段依据见 `company-os/03-legal-compliance/research/aged-care-paperwork-checklist.md` 与 `aged-care-documentation-workflows.md`。

## 关键文件
- 护理记录：`progress-note.md`、`incident-report.md`、`handover-isbar.md`、`care-plan-review-notes.md`、`restrictive-practice-use-record.md`
- 上线与合规：`resident-ai-consent-notice.md`、`staff-workplace-surveillance-notice.md`、`facility-go-live-checklist.md`

## 在这里工作的规则
- **复制后填写，不改模板**：使用时复制到目标位置（试点文件夹或机构系统）再填写；模板本身只在字段依据变化时修改，并写 CHANGELOG
- **不写真实居民信息**：只用 `【居民代号】`、"居民 A" 等占位；不写姓名、房号、出生日期、记录号（根 `AGENTS.md` 硬规则 2）
- **非法律意见**：每个模板开头保留"内部模板，非法律意见"；同意书与员工通知的措辞标"需律师确认"，律师确认前不得对外使用
- **不复制许可受限原文**：`research/downloads/` 中第三方模板（如 DSA BSP）和有版权的标准化量表只参考结构，不搬原文或评分项
- **产品边界**：不加诊断、风险评分、"风险等级"颜色或标签、治疗/用药建议字段；SIRS 只做计时栏，判定由机构人员完成；ISBAR 的 A / R 只写护士本人陈述（TGA 边界，PRD F1）
- **AI 辅助标记**：护理记录模板保留"AI 辅助起草 / 审核人 / 签字时间"栏（ACSQHC Ambient scribe scenario）
- 法规条款名称不确定时标【未核实】，不要自行补全条款原文；新增法规依据先进 `03-legal-compliance/`，再引用（根 `AGENTS.md` 硬规则 9）
- 链接到 `../../03-legal-compliance/` 下的真实文件，移动文件时保持相对链接可用
