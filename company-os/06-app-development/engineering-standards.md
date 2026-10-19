# 工程规范 Engineering Standards

> Owner: Terry（Tech Lead）｜ 复审: 每季度
> 本文件描述技术栈、环境与开发流程。**代码层面的硬性规范（SOLID、DRY、KISS、格式：Tab 缩进宽度 4、安全失败、隐私、测试、评审清单）见 [代码规范](../11-rules/code-rules.md)**，两者冲突时以代码规范为准。

## 技术栈（MVP）

> ✅ = Terry 2026-10-19 已决定；其余为建议，待技术栈 DR 确认。**产品代码统一使用 TypeScript**（Company OS 内部工具脚本如 `check_rules.py` 仍为 Python，不属于产品代码）。

| 层 | MVP 选型 | 理由 |
|---|---|---|
| 语言 | ✅ **TypeScript**（前端、后端、worker 统一） | 一种语言贯穿全栈，类型共享，团队只学一套 |
| 养老院 Web App（护士端 + 管理端） | ✅ React + TypeScript，浏览器 / PWA；不做原生 mobile app（构建工具建议 Vite） | PRD C1 |
| Super Admin App | ✅ 独立 React + TypeScript 应用 | PRD C1、SPEC-010 |
| 营销网站 | ✅ 纯 HTML + CSS；少量脚本用 TypeScript 写、`tsc` 编译为 JS；不用框架 | SPEC-012 |
| 后端 API | Node.js + TypeScript，模块化单体（框架建议 Fastify 或 NestJS，待 DR） | 与前端共享类型；MVP 不拆微服务 |
| 后台任务 / AI 管线 | Node.js + TypeScript worker + 队列（如 SQS） | 转写与起草耗时，不阻塞接口 |
| 数据库 | PostgreSQL，按 `organisation_id` 隔离 + 行级安全 | SPEC-010 / 011 多租户 |
| 对象存储 | ✅ **S3**（原音加密，7 天生命周期删除；营销网站静态托管）；✅ **不做 CDN** | PRD C1 |
| 语音转写 | ✅ **ElevenLabs**（数据在澳洲、零保留、不训练；DPA 书面确认前只用合成数据） | PRD C1、G4 #10 |
| LLM | 澳洲区域托管（待选），不训练、零保留 | 见 [AI 治理](ai-governance.md) |
| 云 | AWS ap-southeast-2（Sydney） | 澳洲数据驻留 |
| 身份认证 | ✅ MVP：邮件邀请 + 密码，**不做 MFA**（仅合成数据阶段）；接入真实数据前加回 SSO（Entra ID / SAML / OIDC）+ MFA | PRD C1、G4 #11 |
| 代码托管 | GitHub，分支保护；monorepo（`apps/`、`packages/`、`services/`） | |

## 环境

| 环境 | 数据 | 访问 |
|---|---|---|
| local / dev | **仅合成数据** | 开发者 |
| staging | 合成数据 / 经批准的去标识化数据 | 开发者 |
| production | 真实数据 | 最小权限、MFA、即时授权（JIT）、全量审计 |

## 开发流程

1. 功能需求写在 `specs/`（含 TGA、隐私、临床影响三项检查）
2. 分支开发 → PR → 至少 1 人 review → CI 通过 → 合并
3. 影响 AI 输出的变更 → 必须跑临床评测集
4. 发布说明记录：变更内容、评测结果、已知限制

## PR 检查清单

```markdown
- [ ] 测试覆盖新逻辑
- [ ] 无密钥/凭据/真实居民数据进入代码或日志
- [ ] 日志中不记录健康信息明文（或已脱敏）
- [ ] 若影响 AI 输出：评测集回归已通过，Clinical Lead 已签字
- [ ] TGA 判定：本变更不引入诊断/治疗/用药建议
- [ ] 隐私：未收集新类型数据（否则附 PIA 链接）
- [ ] 新增依赖/第三方服务已登记（子处理方清单）
```

## 安全编码

- 依赖扫描（Dependabot/Renovate）、SAST、密钥扫描
- OWASP ASVS / Mobile MASVS 作为参考基线
- 所有健康数据：传输 TLS 1.2+，静态加密（KMS 管理密钥）
- 年度第三方渗透测试（首个大客户上线前完成一次）
