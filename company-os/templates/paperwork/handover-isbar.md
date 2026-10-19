# Clinical Handover (ISBAR) — 模板

> **内部模板，非法律意见、非临床意见。** 复制后填写，不改本模板；不写真实居民信息。

| 项目 | 说明 |
|---|---|
| 用途 | 交接班的书面 ISBAR 摘要，支撑口头交接（每位居民一段） |
| 何时使用 | 每次交接班；也可用于与 GP / 救护通话前核对（护士本人陈述部分） |
| 谁填写 | 交班 RN / EN；接班护士确认 |
| 保存年限 | 依机构政策（是否属法定记录【未核实】）；如并入 progress notes 则按 7 年 +州 |
| 法规依据 | SQS 3.3.2(d)（结构化沟通）；ACSQHC ISBAR poster（本地 `research/downloads/clinical-handover/`）；见 [documentation workflows §3](../../03-legal-compliance/research/aged-care-documentation-workflows.md)、[paperwork checklist §2](../../03-legal-compliance/research/aged-care-paperwork-checklist.md) |
| CareKind | ✅ I / S / B 只来自**已签字记录**（PRD D5）；⚠️ A / R 只逐字写护士本人说出的内容，CareKind 不生成；口头交接仍按机构流程 |

## Shift

| Field | Entry |
|---|---|
| Handover from | 【姓名】 【职位】 【班次 AM / PM / Night】 |
| Handover to | 【姓名】 【职位】 |
| Date / time | 【日期】 【HH:MM】 |
| Source | ☐ CareKind summary of signed records ☐ Written manually |

## Per resident（每位居民复制一段）

| ISBAR | Content | Source |
|---|---|---|
| **I — Identify** | 【居民代号】（两要素核对：【要素 1】+【要素 2】）；交班人【姓名 / 职位】 | 名册 |
| **S — Situation** | 【本班发生的情况，只写已记录的事实】 | 已签字记录【记录编号】 |
| **B — Background** | 【相关背景：care plan 摘录、近期事件】 | 已签字记录 / care plan |
| **O — Observations**（ISOBAR 可选） | 【口述或已记录的数值，如饮水 ___ mL】——不标"偏低 / 异常" | 已签字记录 |
| **A — Assessment** | "【护士本人原话】" ☐ 无（护士未陈述则留空，不得补写） | 护士口述【姓名】 |
| **R — Recommendation / Request** | "【护士本人原话】" ☐ 无（不生成护理或治疗建议） | 护士口述【姓名】 |

**Pinned from records（只来自记录，不做判断）**：

- ☐ Incident 【记录编号】
- ☐ Fall 【记录编号】
- ☐ Declined food / fluid 【记录编号】
- ☐ Behaviour change 【记录编号】
- ☐ Outstanding task 【护士陈述的未完成事项】

## Confirmation

| Field | Entry |
|---|---|
| Summary reviewed by handing-over nurse | 【姓名】 【日期时间】 |
| Verbal handover completed | ☐ Yes ☐ Bedside ☐ Nurses' station |
| Received by | 【姓名】 【职位】 【日期时间】 |
| Questions / clarifications | 【接班护士提问与回答】 |

> 本摘要不包含诊断、风险评分、恶化预警或用药建议。未签字草稿不进入交接摘要。
