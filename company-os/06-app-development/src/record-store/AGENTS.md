# AGENTS.md — record-store — 记录库与时间线

> AI 助手在本目录工作前必读。全局规则：根目录 `AGENTS.md` 与 `company-os/11-rules/`。人类说明：同目录 `README.md`。完成任务后按 `changelog-rules.md` 写 `changelog/CHANGELOG.md`。

## 职责
存储签字记录（只追加、带版本），提供老人时间线与完整性视图，执行保留与删除策略。

## 负责的功能（PRD 编号）
- 签字记录与版本（C4）
- 老人时间线、偏好汇总、记录型数据表格（L-01–L-04）
- "已转入机构系统"标记 S-08
- 保留与删除：原音签字后 ≤ 7 天删除（可配置），删除写审计（C7）

## 规则与边界
- 静态加密（P-4）；澳洲区域
- 保留期等常量只在一处定义（DRY）
- 机构护理系统是正式记录库（L-05）；未确认转入的记录不删除
- 数据表格只展示，不做异常判断或预警（TGA）

## 相关临床 hazard
- H-14 时间线被当作完整记录

## 必须覆盖的测试
- 只追加（无覆盖路径）
- 保留与删除按配置执行并留日志

## 参考
- `docs/PRD.md`
- `company-os/11-rules/code-rules.md`
- `company-os/06-app-development/clinical-safety-framework.md`
