# AGENTS.md — ai-pipeline/extraction — ⑤ 字段抽取

> AI 助手在本目录工作前必读。全局规则：根目录 `AGENTS.md` 与 `company-os/11-rules/`。人类说明：同目录 `README.md`。完成任务后按 `changelog-rules.md` 写 `changelog/CHANGELOG.md`。

## 职责
按机构模板从语句中抽取字段值（如"喝了 200 毫升"）。事件按 Rules s164-25 的要素生成字段。

## 负责的功能（PRD 编号）
- 模板字段抽取（D-04）
- 事件要素字段与"未记录"提示（D-05，只提示记录字段）
- 限制性措施字段（D-06，由 Clinical Lead 审定）

## 规则与边界
- 只抽取**明确说出**的值；未说的字段留空，不推断、不填默认值（F-1、CORE-09）

## 相关临床 hazard
- H-01 编造字段值

## 必须覆盖的测试
- 未提及的字段保持为空

## 参考
- `docs/PRD.md`
- `company-os/11-rules/code-rules.md`
- `company-os/06-app-development/clinical-safety-framework.md`
