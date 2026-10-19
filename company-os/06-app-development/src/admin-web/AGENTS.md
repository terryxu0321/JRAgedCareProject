# AGENTS.md — admin-web — 养老院管理端

> AI 助手在本目录工作前必读。全局规则：根目录 `AGENTS.md` 与 `company-os/11-rules/`。人类说明：同目录 `README.md`。完成任务后按 `changelog-rules.md` 写 `changelog/CHANGELOG.md`。

> **第一阶段（Terry 2026-10-19）**：**独立的** Web App（React + TypeScript），与护士端（`mobile-app/`）分开部署。CareKind 平台方的客户开通在 `super-admin/`，不在这里。

## 职责
客户方的管理端：公司管理员（老板）、院长、DON、行政与质量经理。层级：公司（租户）→ 多家养老院（地点）。员工属于公司，可分配到多家院。

## 负责的功能（PRD 编号）
- 公司总览 PA-06（只到养老院级）
- 公司与养老院 PA-01
- 完整员工名册与员工生命周期 PA-02
- 老人名册与生命周期 PA-03（状态变化实时更新 AI 归属候选范围）
- 同意状态管理 M-02、D8
- 记录审核与上报流程配置 PA-04（含 D-04、S-05）
- 新养老院上线流程 PA-05
- 保留策略 M-03、审计日志 M-04 / PA-07

## 规则与边界
- 服务端按 `organisation_id` 隔离租户、按 `facility_id` 限定院级权限；前端传入的 ID 不可信
- 总览与名册**不出现个人排名或个人效率指标**（PRD S-07）；不展示临床风险指标（TGA）
- 资质与筛查到期只提醒，不自动停用、不判定合规
- 老人离院 / 去世立即退出归属候选范围；转院跨州时提示重新确认同意
- 同意状态变更立即生效并写审计
- 名册照片只作人工核对，不做人脸识别
- 不做排班、考勤、工资、绩效（PRD A7）

## 相关临床 hazard
- 同意状态错误导致未同意老人被 AI 处理
- 已离院 / 已去世老人仍在候选范围，记录归属到错误的人（建议新增，见 SPEC-011 §6）

## 必须覆盖的测试
- 院级角色访问其他院、跨公司访问全部被拒绝
- 离院 / 去世 / 转院后归属候选范围正确更新
- 上线清单未完成时该院不能启用录音
- 同意撤回立即生效

## 参考
- `company-os/06-app-development/specs/2026-10-provider-admin-console.md`
- `docs/PRD.md`
- `company-os/11-rules/code-rules.md`
- `company-os/06-app-development/clinical-safety-framework.md`
