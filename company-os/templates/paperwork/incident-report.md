# Incident Report — 模板

> **内部模板，非法律意见、非临床意见。** 复制后填写，不改本模板；不写真实居民信息。

| 项目 | 说明 |
|---|---|
| 用途 | 机构 incident management system（IMS）中的事件记录：跌倒、皮肤撕裂、用药差错、行为事件、不明原因缺席、near miss 等 |
| 何时使用 | 事件发生或发现后尽快（通常本班内完成，机构政策【未核实】） |
| 谁填写 | 发现人 + 值班 RN；是否 reportable、Priority 由 CM / SIRS 负责人判定 |
| 保存年限 | 7 年（Rules s 154-150、s 164-25(2)） |
| 法规依据 | Rules s 164-25(1)（13 项记录要素）；Act s 16（reportable incident）；Rules s 165A-25 / 30 / 45（SIRS 时限）；SQS 2.5；见 [federal-law-summary §1.5](../../03-legal-compliance/research/federal-law-summary.md)、[documentation workflows §4](../../03-legal-compliance/research/aged-care-documentation-workflows.md)、[paperwork checklist §3](../../03-legal-compliance/research/aged-care-paperwork-checklist.md) |
| CareKind | ✅ 事件快速通道草稿（PRD C5 / D3），立即推送作者 + 值班 RN；❌ 不判定 reportable / Priority，不向 ACQSC 或警方提交 |

> 下表字段按本地研究文件对 s 164-25(1) 的描述整理；法定字段的准确名称与项数【未核实】，使用前须对照 Rules 最新汇编。

## 1. Incident details（s 164-25(1) 要素）

| # | Field | Entry |
|---|---|---|
| 1 | Description of the incident | 【只写看到、听到、做到的事实；原话加引号】 |
| 2 | Consequences / harm to the person | 【可观察到的伤害描述，如"右手腕擦伤约 2 cm"；不推断"可能骨折"】 |
| 3 | Date, time and place of incident | 【日期】 【时间】 【地点：如浴室】 |
| 4 | Date and time incident was identified | 【发现日期时间】（如与发生时间不同） |
| 5 | Persons involved / affected | 【居民代号】；其他涉事人【角色，不写真实姓名于模板】 |
| 6 | Witnesses（name, contact details） | 【证人角色 / 联系方式按机构系统】 ☐ 无证人 |
| 7 | Assessment of the incident【字段名未核实】 | 【护士本人陈述的评估；CareKind 不生成】 |
| 8 | Actions taken in response | 【例：扶回床上、通知 RN、按机构 post-falls 流程观察】 |
| 9 | Communication with affected persons / supporters | 【谁、何时、方式、告知内容】 |
| 10 | Whether reportable（SIRS） | 由机构人员在第 3 节判定后填写 |
| 11 | Investigation / outcome【字段名未核实】 | 【由 CM / 质量经理填写】 |
| 12 | Name and position of person recording | 【姓名】 【职位】 |
| 13 | Police notification details（if any）【字段名未核实】 | ☐ 不适用 ☐ 已报警：【日期时间】 【报案编号】 |

## 2. Notifications（护理沟通）

| Notified | Time | By | Method |
|---|---|---|---|
| ☐ RN on duty ☐ GP ☐ Supporter / Family ☐ CM ☐ Other【】 | 【HH:MM】 | 【姓名】 | ☐ In person ☐ Phone ☐ Message |

Open disclosure（只记录已发生的沟通，不写话术）：☐ 已进行 【日期时间】 【对象】 【由谁】

## 3. SIRS timing（仅供机构人员判断 —— CareKind 不判定）

> 提示："这可能需要按机构流程判断是否属于须上报事件（SIRS）。" CareKind 只显示计时，是否上报、上报内容由机构人员决定并在其系统中完成。

| Item | Entry |
|---|---|
| Clock start（first observed / became aware） | 【日期时间】 |
| Priority 1 deadline reference | 知悉后 24 小时内（5 天内补充信息）→ 【截止日期时间】 |
| Priority 2 deadline reference | 知悉后 30 个日历日内 → 【截止日期】 |
| Police（reasonable grounds） | 24 小时内（Rules s 164-40） |
| Decision by facility | ☐ Not reportable ☐ Priority 1 ☐ Priority 2 —— 判定人【姓名 / 职位】 【日期时间】 |
| Submitted to ACQSC | ☐ Yes 【日期时间】 【提交人】 【参考编号】 |
| Final report requested | ☐ Yes，84 天内 → 【截止日期】 |

## 4. AI assistance & sign-off

| Field | Entry |
|---|---|
| Drafted by | ☐ CareKind AI draft from author's dictation ☐ Written manually |
| Missing fields at review | 【CareKind 只提示"未记录：发现时间 / 证人 / 已通知谁"等字段】 |
| Reviewed and signed by | 【姓名】 【职位】 【签字日期时间】 |
| RN review | 【姓名】 【日期时间】 |
| Entered into facility IMS | ☐ Yes 【日期】 【负责人】 |

> 更正只追加（新版本 + 原因 + 更正人 + 时间），不覆盖。不在本记录中写原因推断（除非护士亲口说）、责任评估或风险等级。
