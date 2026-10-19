# AGENTS.md — admin-web — 管理后台

> AI 助手在本目录工作前必读。全局规则：根目录 `AGENTS.md` 与 `company-os/11-rules/`。人类说明：同目录 `README.md`。完成任务后按 `changelog-rules.md` 写 `changelog/CHANGELOG.md`。

> **第一阶段（Terry 2026-10-19）**：本模块不单独部署，作为护士 Web App（`mobile-app/`）中按角色显示的功能模块实现。CareKind 平台方的多养老院管理在 `super-admin/`，不在这里。

## 职责
机构管理员与 DON 使用的 Web 后台。

## 负责的功能（PRD 编号）
- 名册导入、用户与角色、SSO（M-01）
- 同意状态管理（M-02、D8）
- 模板与复核规则配置（D-04、S-05）
- 保留策略（M-03）
- 审计日志查看（M-04）
- 记录完整性看板（L-04）

## 规则与边界
- 仅管理员 / DON 可访问，服务端校验权限（P-6）
- 同意状态变更立即生效并写审计
- 名册照片只作人工核对，不做人脸识别

## 相关临床 hazard
- 同意状态错误导致未同意老人被 AI 处理

## 必须覆盖的测试
- 权限与审计
- 同意撤回立即生效

## 参考
- `docs/PRD.md`
- `company-os/11-rules/code-rules.md`
- `company-os/06-app-development/clinical-safety-framework.md`
