# src — 代码仓库

按 [PRD Part C 架构](../../../docs/PRD.md) 划分模块。代码规范：[code-rules.md](../../11-rules/code-rules.md)。

| 模块 | 职责 | 主要 PRD 需求 |
|---|---|---|
| [mobile-app/](mobile-app/README.md) | 护理人员 App：开班、按键录音、离线队列、审核签字、时间线、交接 | R-*, S-*, L-*, H-01 |
| [api/](api/README.md) | API 网关、SSO/MFA、权限、边界校验、审计日志 | C6, M-04 |
| [ai-pipeline/](ai-pipeline/README.md) | AI 管线 7 步 | C2, C3, T-*, A-*, D-* |
| [review-service/](review-service/README.md) | 记录状态机、复核、事件快速通道、提醒与升级 | C4, C5, S-* |
| [record-store/](record-store/README.md) | 签字记录（只追加）、时间线、保留与删除 | C7, L-*, S-08 |
| [integrations/](integrations/README.md) | 导出、护理系统回写 | E-01, E-02 |
| [admin-web/](admin-web/README.md) | 机构管理：名册、用户、同意状态、模板、保留期（第一阶段合并进护士 Web App） | M-*, D8 |
| [super-admin/](super-admin/README.md) | Super Admin App（独立 React JS）：CareKind 平台方管理多家养老院；不接触居民健康信息 | SA-* |

**第一阶段前端**：护士 Web App（`mobile-app/` + `admin-web/`，浏览器 / PWA）与 Super Admin App（`super-admin/`）两个前端（PRD C1）。
