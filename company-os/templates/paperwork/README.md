# templates/paperwork — 养老护理 Paperwork 模板

> **内部模板，非法律意见、非临床意见。** 创建：2026-10-19 ｜ Owner：Terry（临床字段待 Clinical Lead 复核）｜ 复审：每季度，或 Aged Care Rules 2025 新汇编发布时。

CareKind AI MVP 用到的关键 paperwork，整理成可直接复制使用的 Markdown 模板。说明用简体中文，字段名用英文（养老机构实际使用英文）。

## 怎么用

1. 复制模板到目标位置（如试点文件夹），再填写；不要直接改模板。
2. `【…】` 是占位字段，例如 `【居民代号】`、`【日期时间】`。模板中不写任何真实居民信息。
3. 护理记录类模板是 **CareKind 草稿 → 护理人员审核签字** 的结构；正式记录库是机构护理系统（PRD C7）。
4. 标"需律师确认"的模板（6、7、8 中的通知/同意部分），律师确认前不得对外使用。
5. 标【未核实】的字段名或条款，使用前须核对 Aged Care Rules 2025 最新汇编。

## 模板索引

| # | 模板 | 用途 | 谁填 | 法规依据 | CareKind 能否起草 |
|---|---|---|---|---|---|
| 1 | [progress-note.md](progress-note.md) | 每班 progress note / ADL 记录 | PCW、EN、RN | SQS 2.7、3.2；NMBA RN 1.6 | ✅ 核心场景，HITL 签字后入记录 |
| 2 | [incident-report.md](incident-report.md) | 事件记录 + SIRS 计时栏 | 发现人 + 值班 RN；SIRS 判定由 CM | Rules s 164-25、s 154-150；Act s 16；Rules s 165A | ✅ 事件字段；❌ 不判定 SIRS |
| 3 | [handover-isbar.md](handover-isbar.md) | 交接班 ISBAR 摘要 | 交班 RN / EN | SQS 3.3.2(d)；ACSQHC ISBAR | ✅ I/S/B 来自已签字记录；⚠️ A/R 只写护士原话 |
| 4 | [care-plan-review-notes.md](care-plan-review-notes.md) | Care plan 复审 / case conference 记录 | RN / CM + 居民 / Supporter | SQS 3.1.2、3.1.4、3.1.5；Rules s 148-80 | ✅ 会议记录；❌ 不改写 care plan |
| 5 | [restrictive-practice-use-record.md](restrictive-practice-use-record.md) | 限制性措施使用 / 监测记录 | RN / EN | Rules s 162-30、162-35、162-60 | ✅ 使用记录；❌ 不建议措施、不录入同意 |
| 6 | [resident-ai-consent-notice.md](resident-ai-consent-notice.md) | 居民 / 支持决策人 AI 处理告知与同意 | 机构取得；管理员录入状态 | APP 3、APP 5；Ahpra AI 指南；ACSQHC scenario | ❌ CareKind 提供模板，同意由机构取得（需律师确认） |
| 7 | [staff-workplace-surveillance-notice.md](staff-workplace-surveillance-notice.md) | 员工书面通知（工作场所监控） | 机构（雇主）HR / DON | NSW Workplace Surveillance Act 2005；ACT Workplace Privacy Act 2011 | ❌ CareKind 提供模板，机构发出（需律师确认） |
| 8 | [facility-go-live-checklist.md](facility-go-live-checklist.md) | 机构上线清单 | CareKind 上线负责人 + 机构管理员 / DON | PRD D1；DPA；APP 8、APP 11 | — 内部清单 |

缩写：SQS = Strengthened Aged Care Quality Standards；Rules = Aged Care Rules 2025；Act = Aged Care Act 2024；HITL = 人工审核签字。

## 字段依据（本地文件）

- [aged-care-paperwork-checklist.md](../../03-legal-compliance/research/aged-care-paperwork-checklist.md) —— 文档 × 保存年限 × 法规依据 × CareKind 能否起草
- [aged-care-documentation-workflows.md](../../03-legal-compliance/research/aged-care-documentation-workflows.md) —— 流程、ISBAR、best practice（第 11、12 节）
- [federal-law-summary.md](../../03-legal-compliance/research/federal-law-summary.md) —— s 164-25、s 162-60 等条款摘要
- [state-by-state-comparison.md](../../03-legal-compliance/research/state-by-state-comparison.md) —— 录音同意与工作场所监控州差异（§2）
- [recording-consent.md](../../03-legal-compliance/recording-consent.md) —— 录音同意统一标准（DR-004）
- [paperwork-templates-index.md](../../03-legal-compliance/research/paperwork-templates-index.md) —— 已下载的官方模板与指南

## 统一规则（所有模板）

- 只写看到、听到、做到的事实；居民原话加引号；区分"观察时间"与"签字时间"
- 不设诊断、风险评分、"风险等级"颜色或标签字段（TGA 边界，PRD F1）
- 签字后不覆盖，更正 = 追加新版本 + 原因 + 更正人 + 时间（PRD C4）
- 护理记录保留"AI 辅助起草 / 审核人"标记
