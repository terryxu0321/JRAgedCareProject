# 工程规范 Engineering Standards

> Owner: Terry（Tech Lead）｜ 复审: 每季度
> 本文件描述技术栈、环境与开发流程。**代码层面的硬性规范（SOLID、DRY、KISS、格式：Tab 缩进宽度 4、安全失败、隐私、测试、评审清单）见 [代码规范](../11-rules/code-rules.md)**，两者冲突时以代码规范为准。

## 技术栈（MVP）

> 状态：✅ 已决定（Terry 2026-10-19，与课程结果一致）｜ 🟡 方向已定、供应商待选 ｜ ⏳ 待定。**产品代码统一使用 TypeScript**（Company OS 内部工具脚本如 `check_rules.py` 仍为 Python，不属于产品代码）。

### 前端

| 部分 | 技术 | 说明 |
|---|---|---|
| 护士端 | ✅ Web App，React + TypeScript | PRD C1、SPEC-004–009 |
| 机构管理端 | ✅ **独立的** Web App，React + TypeScript | SPEC-011 |
| Super Admin | ✅ 独立的 React JS app，TypeScript；不做 IP allowlist | SPEC-010 |
| Demo 环境 | ✅ 独立部署，React + TypeScript，只用虚构数据 | 销售演示与培训；不连生产 |
| Mobile App | ✅ React Native + TypeScript，列入路线图，第一阶段不做 | |
| Marketing website | ✅ 纯 HTML + CSS，不用 Next.js；页面脚本用 TypeScript 写、`tsc` 编译；只做英文 | SPEC-012 |
| 设计系统 | ✅ `06-app-development/design-system` 的 token，以 CSS 变量引入 | DESIGN.md |
| 构建工具 | ⏳ Vite（待定） | |

### 后端与 AI

| 部分 | 技术 | 说明 |
|---|---|---|
| 语言 | ✅ 全部 TypeScript（Node.js） | 前后端共享类型 |
| API 框架 | ✅ **NestJS**（Terry 2026-10-19） | 模块化单体，按 `src/` 模块分 module |
| 数据校验 | ⏳ zod，类型和校验共用一份定义 | 只在边界校验（code-rules CORE-07） |
| 语音转写 | ✅ ElevenLabs，数据在澳洲（零保留、不训练；真实录音前 DPA 书面确认） | PRD C1、G4 #10 |
| 起草用的 LLM | 🟡 云厂商托管、澳洲区域（如 AWS Bedrock Sydney），零保留，锁定模型版本 | 见 [AI 治理](ai-governance.md)；换版本须跑评测集 |
| 模型调用 | ✅ 客户端不直接调用模型，全部经过后端 | 密钥不出后端；护栏统一执行 |
| Tier 3 实时推送 | ⏳ WebSocket 或 Web Push | 如事件草稿立即提醒（SPEC-008） |
| 认证 | ⏳ 托管身份服务（邮件邀请 + 密码登录） | PRD C1 |

### 工程流程

| 部分 | 技术 | 状态 |
|---|---|---|
| 代码仓库 | GitHub：本仓库为 **meta repo**（Company OS + 规范 + spec），每个应用一个**独立仓库**，以 git submodule 引入（Terry 2026-10-19，取代课程表中的单个 `carekind-app` monorepo） | ✅ |
| 仓库结构 | 多仓库：5 个应用仓库 + 1 个共享仓库 `carekind-shared`（见下方"仓库清单"） | ✅ |
| CI/CD | GitHub Actions，在云端运行，不在本机跑 | ✅ |
| 环境 | dev / staging / production / demo；生产数据不进入其他环境（见下方"环境"） | ✅ |
| 代码规范 | [code-rules.md](../11-rules/code-rules.md)：Tab 缩进 4、单文件不超过 1000 行、禁用 `any`、只用合成测试数据 | ✅ |

#### 仓库清单（2026-10-19 已创建并加为 submodule）

均为 `terryxu0321` 下的**公开**仓库（与 meta repo 一致：不得提交密钥、真实居民或个人数据、本地绝对路径）。每个仓库有自己的 GitHub Actions CI 和发布流程。

**所有文档只保存在 meta repo**（Terry 2026-10-19）：PRD、spec、模块说明、规范、决策记录、CHANGELOG、设计系统文档都在本仓库。子仓库只放代码、测试和运行所需的配置；唯一例外是一个简短的 `README.md`，说明本仓库是什么并链接到 meta repo 中对应的模块说明。在子仓库工作的 AI 助手须先读 meta repo 的根 `AGENTS.md` 与对应模块的 `AGENTS.md`。

| 仓库 | 内容 | 在 meta repo 中的 submodule 路径 | 对应模块说明 |
|---|---|---|---|
| `carekind-nurse-web` | 护士端 Web App（React + TS） | `apps/carekind-nurse-web` | [src/mobile-app/](src/mobile-app/README.md) |
| `carekind-admin-web` | 机构管理端 Web App（React + TS） | `apps/carekind-admin-web` | [src/admin-web/](src/admin-web/README.md) |
| `carekind-super-admin` | Super Admin App（React + TS） | `apps/carekind-super-admin` | [src/super-admin/](src/super-admin/README.md) |
| `carekind-marketing-site` | 营销网站（HTML + CSS，脚本 TS） | `apps/carekind-marketing-site` | [src/marketing-site/](src/marketing-site/README.md) |
| `carekind-api` | 后端：NestJS API + AI 管线 worker（含 ai-pipeline、review-service、record-store、integrations 等模块，模块化单体） | `services/carekind-api` | [src/api/](src/api/README.md) 等后端模块 |
| `carekind-shared` | 共享代码：设计 token（CSS 变量）、zod schema 与 TS 类型、API 客户端 | `packages/carekind-shared` | [design-system/](design-system/DESIGN.md) |

- 各应用通过 git 依赖或包管理引用 `carekind-shared` 的**固定版本**（不直接引用 meta repo 路径）；类型和校验只在 `carekind-shared` 定义一份
- meta repo 只记录每个 submodule 的提交指针；功能开发在各自仓库完成，meta repo 定期更新指针
- `company-os/06-app-development/src/` 下的模块说明是需求与边界的唯一来源；子仓库不复制这些说明，只在 README 中链接回来
- Mobile App（React Native）以后单独建 `carekind-mobile`；Demo 环境是同一批仓库的独立部署（虚构数据），不另建仓库

### 数据与基础设施

| 部分 | 技术 | 状态 |
|---|---|---|
| 部署区域 | 澳洲境内（AWS Sydney） | 🟡 |
| 数据库 | PostgreSQL（托管）；M0 本地开发与测试用 PGlite + Drizzle，**不用 Docker**（[M0 技术设计](m0-admin-tech-design.md)） | ⏳ |
| 多租户隔离 | 行级安全或 schema 隔离（技术 ADR-0002，待写） | ⏳ |
| 对象存储 | S3：音频短期保留、到期自动删除；不用 CDN | ✅ |
| 审计日志 | 只追加，不能修改 | ✅ |
| 加密 | 全部静态加密 + KMS；日志里不记健康信息 | ✅ |
| 基础设施即代码 | CDK 或 Terraform | ⏳ |
| 后台任务 / AI 管线 | Node.js + TypeScript worker + 队列（如 SQS） | 建议 |

## 环境

**生产数据不进入其他任何环境。**

| 环境 | 数据 | 访问 |
|---|---|---|
| dev（含本地） | **仅合成数据** | 开发者 |
| staging | 合成数据 / 经批准的去标识化数据 | 开发者 |
| demo | **只用虚构数据**；独立部署（独立前端、后端与数据库），不连 staging / production | 销售演示、培训、试点前展示 |
| production | 真实数据 | 最小权限、即时授权（JIT）、全量审计 |

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
