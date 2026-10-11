# AGENTS.md — ai-pipeline/guardrails — ⑦ 护栏

> AI 助手在本目录工作前必读。全局规则：根目录 `AGENTS.md` 与 `company-os/11-rules/`。人类说明：同目录 `README.md`。完成任务后按 `changelog-rules.md` 写 `changelog/CHANGELOG.md`。

## 职责
草稿显示前的最后一道关：忠实性核对、禁止内容过滤、关键项标记。是 TGA 边界与临床安全的技术保障。

## 负责的功能（PRD 编号）
- 忠实性核对：每句须对应来源语句，否则删除并标记
- 禁止内容过滤：诊断/治疗/用药建议/风险判断 → 阻止并记录（D-07）
- 关键项标记：药名、剂量、数字、事件（S-03）

## 规则与边界
- 护栏规则只在本模块定义（DRY）
- 任何放宽护栏的改动 = Type 1 决策：须 DR + Clinical Lead 签字
- 校验失败的内容不得进入草稿（F-3）

## 相关临床 hazard
- H-01、H-05

## 必须覆盖的测试
- 禁止内容样本 100% 拦截
- 忠实性反例全部被删除

## 参考
- `docs/PRD.md`
- `company-os/11-rules/code-rules.md`
- `company-os/06-app-development/clinical-safety-framework.md`
