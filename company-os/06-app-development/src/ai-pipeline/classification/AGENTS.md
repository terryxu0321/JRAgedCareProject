# AGENTS.md — ai-pipeline/classification — ④ 分类

> AI 助手在本目录工作前必读。全局规则：根目录 `AGENTS.md` 与 `company-os/11-rules/`。人类说明：同目录 `README.md`。完成任务后按 `changelog-rules.md` 写 `changelog/CHANGELOG.md`。

## 职责
判断语句属于哪种记录类型：progress note、ADL 子项、行为观察、伤口描述、陈述的生命体征、家属沟通、**事件**。

## 负责的功能（PRD 编号）
- 记录类型清单（D-01）
- 事件识别 → 触发 review-service 事件快速通道（C5）

## 规则与边界
- 不确定时归为 progress note（不丢内容）
- 记录类型清单只在一处定义（DRY），新增类型 = 新增注册，不改主流程（SOLID O）
- 只识别"是什么记录"，**不做**是否须上报 SIRS 的判断

## 相关临床 hazard
- H-04 事件被漏分类

## 必须覆盖的测试
- 跌倒、皮肤破损、拒食等事件的召回率

## 参考
- `docs/PRD.md`
- `company-os/11-rules/code-rules.md`
- `company-os/06-app-development/clinical-safety-framework.md`
