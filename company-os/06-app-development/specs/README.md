# 功能需求 Specs

每个功能一份，文件名：`YYYY-MM-feature-name.md`。模板：

```markdown
# [功能名]

- Owner / 状态 / 目标发布
- Assignee: [唯一一位名册成员 —— 用 skill assign-prd 分配]

## 问题（护士原话）
## 目标与度量（节省多少时间？如何测？）
## 用户流程
## 范围 / 不做什么

## 法律依据 Legal References
（必填 —— 按 company-os/11-rules/legal-reference-index.md 查阅本地法律文件；
 每个话题：本地文件链接 + 章节 + 对设计的影响；需律师确认事项；合规检查链接）

## 检查
- [ ] 法律依据已填写，`python company-os/11-rules/check_rules.py` 通过
- [ ] TGA 判定：是否生成诊断/治疗/用药建议？（必须为否）
- [ ] 临床 hazard 已加入 hazard log：H-__
- [ ] 隐私：新数据类型？需 PIA？
- [ ] 新子处理方/新模型？
- [ ] 可访问性与多语言

## 评测计划
```

## 总 PRD

产品级需求在 **[docs/PRD.md](../../../docs/PRD.md)**。本文件夹只放单个功能的详细设计，并链接回 PRD。

## 现有 specs

- [2026-10-shift-voice-to-resident-records.md](2026-10-shift-voice-to-resident-records.md) —— 核心 MVP：班次语音 → 按老人归属 → 草稿 → 审核（内容见 PRD）
- [2026-10-adlc-delivery-lifecycle.md](2026-10-adlc-delivery-lifecycle.md) —— 内部研发流程：ADLC（AI 协作开发生命周期）—— 任务分配、PRD 阶段管理与状态记录（草稿，待 Terry 审阅）
- MVP P0 功能 spec（2026-10-19，草稿，待 Terry 审阅与 `assign-prd` 分配；总览见 [product-feature-map.md](../product-feature-map.md)）：
	- [2026-10-shift-voice-capture.md](2026-10-shift-voice-capture.md) —— SPEC-004 班次语音采集与转写
	- [2026-10-resident-attribution.md](2026-10-resident-attribution.md) —— SPEC-005 居民归属引擎
	- [2026-10-draft-generation-guardrails.md](2026-10-draft-generation-guardrails.md) —— SPEC-006 草稿生成与护栏
	- [2026-10-review-and-sign-off.md](2026-10-review-and-sign-off.md) —— SPEC-007 审核签字（HITL）
	- [2026-10-incident-fast-track.md](2026-10-incident-fast-track.md) —— SPEC-008 事件快速通道与 SIRS 计时提醒
	- [2026-10-consent-management.md](2026-10-consent-management.md) —— SPEC-009 居民同意管理
	- [2026-10-super-admin-console.md](2026-10-super-admin-console.md) —— SPEC-010 Super Admin 控制台（独立 React JS，客户公司开通与配置）
	- [2026-10-provider-admin-console.md](2026-10-provider-admin-console.md) —— SPEC-011 养老院管理端（公司 + 多家养老院：员工、老人、流程、总览）
	- [2026-10-marketing-website.md](2026-10-marketing-website.md) —— SPEC-012 营销网站（纯 HTML + CSS；文案受 ACL / TGA 约束）
- [2026-10-design-system.md](2026-10-design-system.md) —— SPEC-003 Design System：tokens、基础组件、安全关键组件、文案与无障碍规范；任务 T-0001 至 T-0009 见 [adlc/tasks/](../adlc/tasks/README.md)（草稿，待 Terry 审阅）
