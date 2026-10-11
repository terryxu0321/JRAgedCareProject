# AGENTS.md — review-service — 审核与状态机

> AI 助手在本目录工作前必读。全局规则：根目录 `AGENTS.md` 与 `company-os/11-rules/`。人类说明：同目录 `README.md`。完成任务后按 `changelog-rules.md` 写 `changelog/CHANGELOG.md`。

## 职责
管理记录状态机（PRD C4）、PCW → RN 复核、事件快速通道（C5）、未审核提醒与升级。

## 负责的功能（PRD 编号）
- 状态机：已采集 → … → 已签字 → 已复核 → 已导出
- 复核规则 S-05、翻译记录默认 RN 复核 T-04
- 事件快速通道：立即提醒、显示计时与"按机构流程判断"提示 —— **只提醒，不判定 SIRS**
- 提醒与升级 S-06
- 零编辑确认率 S-07（只做机构层汇总，不做个人排名）

## 规则与边界
- **不存在**自动提交或自动签字（F-5）
- 签字后只追加更正（F-4）
- 升级只通知人，不替人决定

## 相关临床 hazard
- H-08 / H-11 自动化偏见与积压
- H-12 签字延迟

## 必须覆盖的测试
- 状态机全部合法/非法转换
- 事件提醒时效
- 无自动提交路径

## 参考
- `docs/PRD.md`
- `company-os/11-rules/code-rules.md`
- `company-os/06-app-development/clinical-safety-framework.md`
