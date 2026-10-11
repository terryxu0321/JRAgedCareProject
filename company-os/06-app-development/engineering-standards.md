# 工程规范 Engineering Standards

> Owner: Terry（Tech Lead）｜ 复审: 每季度
> 本文件描述技术栈、环境与开发流程。**代码层面的硬性规范（SOLID、DRY、KISS、格式：Tab 缩进宽度 4、安全失败、隐私、测试、评审清单）见 [代码规范](../11-rules/code-rules.md)**，两者冲突时以代码规范为准。

## 技术栈（建议，待 DR 确认）

| 层 | 建议 | 理由 |
|---|---|---|
| 云 | AWS ap-southeast-2（Sydney），灾备 ap-southeast-4（Melbourne）；或 Azure Australia East/Southeast | 澳洲数据驻留；健康行业常见 |
| 移动端 | React Native / Flutter（护士手机/平板） | 一套代码覆盖 iOS/Android |
| Web 管理端 | React + TypeScript | |
| 后端 | TypeScript (Node) 或 Python | Python 便于 AI 管线 |
| AI | 澳洲区域托管的语音转写与 LLM 服务 | 见 [AI 治理](ai-governance.md) |
| 身份认证 | 支持客户 SSO（Entra ID / SAML / OIDC）+ MFA | 养老机构普遍使用 Microsoft 365 |
| 代码托管 | GitHub（私有），分支保护 | |

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
