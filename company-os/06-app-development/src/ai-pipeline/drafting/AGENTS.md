# AGENTS.md — ai-pipeline/drafting — ⑥ 起草

> AI 助手在本目录工作前必读。全局规则：根目录 `AGENTS.md` 与 `company-os/11-rules/`。人类说明：同目录 `README.md`。完成任务后按 `changelog-rules.md` 写 `changelog/CHANGELOG.md`。

## 职责
用 LLM 把语句与字段生成为机构模板格式的记录草稿；同一老人同类内容合并。

## 负责的功能（PRD 编号）
- 草稿生成（D-01）
- 以人为本、尊重的措辞（产品原则 6）
- 每句链接来源语句（D-03、A-5）

## 规则与边界
- **只写护士说过的内容**（D-02）
- 提示词纳入版本控制与评审（A-1）
- 生成失败时返回原始转写供手动编辑，不返回空

## 相关临床 hazard
- H-01 幻觉
- H-05 临床建议

## 必须覆盖的测试
- 忠实性评测
- 禁止内容出现率为 0

## 参考
- `docs/PRD.md`
- `company-os/11-rules/code-rules.md`
- `company-os/06-app-development/clinical-safety-framework.md`
