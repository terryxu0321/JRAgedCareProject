# AGENTS.md — super-admin — Super Admin App

> AI 助手在本目录工作前必读。全局规则：根目录 `AGENTS.md` 与 `company-os/11-rules/`。人类说明：同目录 `README.md`。完成任务后按 `changelog-rules.md` 写 `changelog/CHANGELOG.md`。

## 职责
CareKind 平台方使用的独立 React JS 应用（桌面浏览器）：管理客户公司（租户，层级 平台 → 公司 → 养老院）。只调用 `api` 的平台接口，不直接访问数据库。

## 负责的功能（PRD 编号）
- 公司（租户）开通 / 编辑 / 停用，只读查看其养老院 SA-01
- 公司配置上限与平台默认值 SA-02
- 公司管理员账号 SA-03（MVP 不做 MFA 与 IP allowlist）
- 去标识用量与平台审计 SA-04

## 规则与边界
- **不提供**居民名册、记录、原音、转写的任何查看入口（SA-05）；平台接口也不返回这些字段
- 租户隔离由服务端强制，前端传入的租户 ID 不可信（SA-01a）
- 用量只做养老院级汇总，不出现个人排名（PRD S-07）
- 所有平台操作写审计；停用养老院需二次确认，不删除数据
- UI 只用 `design-system/DESIGN.md` 的 token 与组件

## 相关临床 hazard
- 租户隔离失效导致跨院看到居民记录（建议新增，见 SPEC-010 §6）

## 必须覆盖的测试
- 跨租户访问全部被拒绝
- 平台接口响应不含居民健康信息字段
- 非 Super Admin 角色无法访问平台接口

## 参考
- `company-os/06-app-development/specs/2026-10-super-admin-console.md`
- `docs/PRD.md`（C1、C6、E6）
- `company-os/11-rules/code-rules.md`
