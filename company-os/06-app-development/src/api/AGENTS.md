# AGENTS.md — api — API 网关与访问控制

> AI 助手在本目录工作前必读。全局规则：根目录 `AGENTS.md` 与 `company-os/11-rules/`。人类说明：同目录 `README.md`。完成任务后按 `changelog-rules.md` 写 `changelog/CHANGELOG.md`。

## 职责
所有客户端请求的入口：认证（SSO + MFA）、服务端权限校验（PRD C6）、请求边界校验、审计日志、限流。业务逻辑交给各服务。

## 负责的功能（PRD 编号）
- SSO / MFA 与会话管理（M-01）
- 权限矩阵 C6，服务端执行（P-6）
- 审计日志 M-04（P-7）
- 请求与响应 schema 校验（CORE-07、TY-3）

## 规则与边界
- 默认拒绝：新端点默认需要认证与最小权限（CORE-08）
- 交互式接口 p95 ≤ 500 ms，> 2 s 不合格（§11）
- 只在这里和外部集成处做输入校验；内部服务相互信任（CORE-07）
- 部署在澳洲区域；CORS 白名单

## 相关临床 hazard
- 越权访问他人记录（隐私事件）

## 必须覆盖的测试
- 每个角色 × 每个动作的权限测试
- 无效输入被拒绝且不泄露内部信息

## 参考
- `docs/PRD.md`
- `company-os/11-rules/code-rules.md`
- `company-os/06-app-development/clinical-safety-framework.md`
