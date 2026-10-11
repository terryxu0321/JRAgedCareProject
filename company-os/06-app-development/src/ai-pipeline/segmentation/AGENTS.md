# AGENTS.md — ai-pipeline/segmentation — ② 拆分

> AI 助手在本目录工作前必读。全局规则：根目录 `AGENTS.md` 与 `company-os/11-rules/`。人类说明：同目录 `README.md`。完成任务后按 `changelog-rules.md` 写 `changelog/CHANGELOG.md`。

## 职责
把转写拆成语句（最小语义单元），保留每句的时间区间，作为归属与溯源的单位。

## 负责的功能（PRD 编号）
- 按句与话题切换拆分（A-02 前置）

## 规则与边界
- 无法拆分时整段作为一个语句，不丢内容

## 相关临床 hazard
- H-10 多位老人内容串写

## 必须覆盖的测试
- 一段话含多位老人时的拆分
- 拆分前后文字完全一致（不增不减）

## 参考
- `docs/PRD.md`
- `company-os/11-rules/code-rules.md`
- `company-os/06-app-development/clinical-safety-framework.md`
