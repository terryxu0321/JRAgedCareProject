# AGENTS.md — integrations — 导出与护理系统集成

> AI 助手在本目录工作前必读。全局规则：根目录 `AGENTS.md` 与 `company-os/11-rules/`。人类说明：同目录 `README.md`。完成任务后按 `changelog-rules.md` 写 `changelog/CHANGELOG.md`。

## 职责
把签字记录导出（复制/PDF）或回写到机构护理系统（Leecare、Telstra Health 等）。

## 负责的功能（PRD 编号）
- 导出 E-01（含签字人、时间、版本）
- 回写适配器 E-02：`CareSystemAdapter` 接口，每个系统一个实现（SOLID O/D）
- 回执、失败重试与告警

## 规则与边界
- 外部系统的响应是边界，必须校验（CORE-07）
- 新集成对象须登记子处理方/供应商并更新 DPA
- 失败不得丢失记录，也不得重复写入

## 相关临床 hazard
- 回写到错误老人或重复写入

## 必须覆盖的测试
- 适配器契约测试
- 失败重试幂等

## 参考
- `docs/PRD.md`
- `company-os/11-rules/code-rules.md`
- `company-os/06-app-development/clinical-safety-framework.md`
