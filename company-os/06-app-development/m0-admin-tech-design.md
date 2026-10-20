# M0 管理端技术设计（Super Admin + 机构管理端）

> Owner：Terry ｜ v0.1 · 2026-10-20 ｜ 状态：🟡 M0 实施依据（Terry 2026-10-20 授权"PRD 未完成先补完再开发"）
> 需求来源：[docs/PRD.md](../../docs/PRD.md) G2 M0、[SPEC-010 Super Admin](specs/2026-10-super-admin-console.md)、[SPEC-011 机构管理端](specs/2026-10-provider-admin-console.md)、[SPEC-009 同意管理](specs/2026-10-consent-management.md)。本文件只补充"怎么实现"，需求与边界以上述文件为准；冲突时以 spec 为准。
> 范围：**只做管理端**。不含护士端、AI 管线、营销网站、Demo 环境部署。

## 1. M0 实施选择

技术栈状态见 [工程规范](engineering-standards.md)。课程表中标 ⏳ 的项目，M0 先按下表实施；后续 ADR 可替换（实现都放在接口后面）。

| 项 | M0 做法 | 说明 |
|---|---|---|
| 构建工具 | Vite（两个前端） | React + TypeScript |
| 数据校验 | zod，schema 只在 `carekind-shared` 定义一份 | 前后端共用类型（code-rules D-3） |
| API | NestJS，REST，前缀 `/api/v1` | 模块化单体 |
| 数据库 | PostgreSQL；**不用 Docker**（Terry 2026-10-20）：本地开发与测试用 PGlite（npm 安装的嵌入式 PostgreSQL，数据存在本地文件夹，已加入 `.gitignore`）；ORM 用 Drizzle（同一套代码可切换到托管 PostgreSQL 的 `pg` 驱动） | 托管数据库待定 |
| 多租户隔离 | 共享表 + 每张业务表 `organisation_id`（院级数据另有 `facility_id`）；API 层从登录凭证取租户，所有查询经租户作用域；跨租户自动化测试必须全部拒绝 | 数据库层 RLS / schema 隔离由技术 ADR-0002 决定（待写） |
| 认证 | 邮件邀请 + 密码登录；密码用 argon2 / bcrypt 哈希；JWT（Bearer）；实现放在 `AuthProvider` 接口后，日后换托管身份服务 | 不做 MFA、不做 IP allowlist |
| 邀请 | **不发邮件**（AGENTS 硬规则 3）：API 生成一次性邀请链接，界面显示给邀请人复制 | 有效期 7 天 |
| 共享代码引用 | `carekind-shared` 以 `file:` 依赖引用（meta repo 内相对路径 `../../packages/carekind-shared`），先 `npm run build` | M0 本地开发；发布方式待定 |
| 设计 | `carekind-shared` 从 [DESIGN.md](design-system/DESIGN.md) 生成 `tokens.css`（CSS 变量）；组件按 DESIGN.md 实现，管理端用 `scope: admin-web` 组件 | 一页一个表单、一个 submit（DESIGN §7.3） |
| 测试 | 全部用 Vitest（API 原定 Jest，因 ESM + 装饰器元数据改用 Vitest + SWC）；API 每个测试文件用内存 PGlite 实例跑迁移 | 只用合成数据 |
| 代码规范 | [code-rules.md](../11-rules/code-rules.md)：Tab 缩进 4、单文件 ≤ 1000 行、禁用 `any`、导出写明类型、无 TODO | ESLint + Prettier（`useTabs: true, tabWidth: 4`） |
| 端口 | API 3000；Super Admin 5173；机构管理端 5174 | CORS 只放行这两个本地源 |
| Git | 每个子仓库在分支 `m0-admin` 上本地提交；**不 push**；meta repo 只更新 submodule 指针 | AGENTS"Never push automatically" |

## 2. 角色

| 角色 | 所在层 | 能进哪个前端 | 范围 |
|---|---|---|---|
| `platform_admin` | 平台（`platform_admins` 表，不属于任何公司） | Super Admin | 全部公司，**不可见居民与员工明细**（SA-05） |
| `org_admin` | 公司 | 机构管理端 | 本公司全部养老院 |
| `facility_manager` | 院 | 机构管理端 | 分配到的院 |
| `don` | 院 | 机构管理端 | 分配到的院 |
| `admin_officer`（行政 / 质量） | 院 | 机构管理端 | 分配到的院 |
| `rn` / `en` / `pcw` | 院 | 护士端（M0 不做） | — |
| `no_app`（厨房、清洁等） | 院 | 无账号 | 只在名册中 |

院级角色存在 `staff_assignments`（一名员工可在多家院、每院角色不同）。`org_admin` 是员工上的公司级标记。

**机构管理端权限**（✓ = 允许；院级角色只限分配到的院）：

| 操作 | org_admin | facility_manager | don | admin_officer |
|---|---|---|---|---|
| 公司总览 | ✓（全部院） | ✓（本院） | ✓（本院） | ✓（本院） |
| 新增养老院 | ✓ | — | — | — |
| 编辑养老院资料 | ✓ | ✓ | — | — |
| 员工名册、资质、生命周期 | ✓ | ✓ | — | ✓ |
| 老人名册与生命周期 | ✓ | ✓ | ✓ | ✓ |
| 同意状态 | ✓ | ✓ | ✓ | ✓ |
| 审核与上报流程配置 | ✓ | ✓ | ✓ | — |
| 上线清单与启用 | ✓ | ✓ | — | — |
| 审计日志 | ✓ | ✓ | — | — |

## 3. 数据模型

所有表有 `id`（UUID）、`created_at`、`updated_at`。除平台表外都有 `organisation_id`。

| 表 | 主要字段 |
|---|---|
| `platform_admins` | email、name、password_hash、is_active |
| `platform_defaults` | 单行：enabled_record_types、pcw_requires_rn_review、audio_retention_days_max（≤ 7）、ai_processing_enabled、facility_limit |
| `organisations` | name、abn、contact_name、contact_email、status（`active` / `suspended`）+ 配置上限（同 platform_defaults 字段，创建时复制默认值） |
| `facilities` | organisation_id、name、address、state（`NSW` `VIC` `QLD` `WA` `SA` `TAS` `ACT` `NT`）、beds、timezone、status（`configuring` / `live` / `suspended`） |
| `staff` | organisation_id、given_name、family_name、position、employment_type（`full_time` / `part_time` / `casual` / `agency`）、is_org_admin、has_app_access、email（开通 App 时必填）、password_hash、lifecycle（`recorded` / `invited` / `pending_training` / `active` / `deactivated`）、training_completed_at |
| `staff_assignments` | staff_id、facility_id、role（第 2 节院级角色或 `rn` `en` `pcw` `no_app`）；(staff_id, facility_id) 唯一 |
| `credentials` | staff_id、kind（`ahpra_registration` / `worker_screening` / `police_check` / `carekind_training`）、reference（如注册号）、expires_at；到期提醒在查询时按 60 / 30 天计算，不自动停用 |
| `invites` | organisation_id（平台邀请公司管理员时同样有）、staff_id、token_hash、expires_at、used_at |
| `residents` | organisation_id、facility_id、given_name、preferred_name、family_name、room、status（`pre_admission` / `in_residence` / `temporary_leave` / `transferring` / `departed` / `deceased` / `archived`）；**不存出生日期、照片**（M0 不需要，YAGNI） |
| `resident_events` | resident_id、type（`admit` / `temporary_leave` / `return` / `transfer_out` / `transfer_accept` / `depart` / `death` / `archive`）、from_facility_id、to_facility_id、occurred_at、recorded_by |
| `consents` | resident_id（唯一）、status（`consented` / `not_consented` / `withdrawn` / `unknown`）、source（`self` / `supporter` / `substitute_decision_maker`）、jurisdiction、basis_note、recorded_by、recorded_at；无记录 = `unknown`，按未同意处理 |
| `workflow_settings` | facility_id（唯一）、pcw_requires_rn_review、review_record_types、unreviewed_reminder_minutes、escalate_to（`on_duty_rn` / `don`）、incident_notify_roles、transfer_to_facility_system_days、transfer_owner_staff_id |
| `golive_items` | facility_id、key（`contract_signed` / `staff_register_imported` / `resident_register_imported` / `consent_recorded` / `staff_notice_sent` / `training_completed` / `record_transfer_agreed`）、completed_at、completed_by、notice_sent_on（仅 `staff_notice_sent`） |
| `audit_log` | organisation_id（平台操作可为空）、actor_type（`platform_admin` / `staff`）、actor_id、action、entity、entity_id、occurred_at、summary（**不含健康信息与居民姓名**）；**只追加**：数据库触发器拒绝 UPDATE / DELETE |

状态规则（写成有测试的纯函数）：
- 老人：只有 `in_residence` 进入将来的 AI 归属候选（导出 `isAttributionCandidate()`）；`transfer_out` 后状态 `transferring`，接收院 `transfer_accept` 后改归新院并把同意重置为 `unknown`（跨州时界面提示按新州规则重新确认，SPEC-011 §3.1）
- 员工：`deactivated` 立即使其所有 token 失效；`has_app_access` 且未完成培训的员工不能登录护士端（M0 只记录状态）
- 上线：所有 `golive_items` 完成，且 NSW 院的 `staff_notice_sent` 日期距今 ≥ 14 天，才能把院设为 `live`（其他州只记录日期）

## 4. API（`/api/v1`）

请求与响应的 zod schema 全部在 `carekind-shared`；路径常量也在 shared 中定义一份。

**认证**：`POST /auth/login`（`audience: platform | org`）、`POST /auth/accept-invite`（token + 新密码）、`GET /auth/me`

**平台（仅 platform_admin）**
- `GET /platform/organisations`、`POST /platform/organisations`、`GET /platform/organisations/:id`、`PATCH /platform/organisations/:id`
- `POST /platform/organisations/:id/suspend`、`POST /platform/organisations/:id/reactivate`
- `PUT /platform/organisations/:id/limits`
- `GET /platform/organisations/:id/facilities`（只读：名称、州、状态）
- `GET /platform/organisations/:id/admins`、`POST /platform/organisations/:id/admin-invites`、`POST /platform/admins/:staffId/deactivate`
- `GET /platform/defaults`、`PUT /platform/defaults`
- `GET /platform/usage`（按公司、按养老院：养老院数、开通 App 的员工数、近 7 天登录员工数；片段数与签字数显示"暂无数据（护士端未上线）"）
- `GET /platform/audit`
- 平台接口响应**不得**包含 `residents`、`consents`、员工姓名或邮件以外的明细（公司管理员邀请除外）；有自动化字段扫描测试

**机构（staff 登录，按公司与可访问的院限定）**
- `GET /org/overview`：按院汇总 —— 上线状态、在住老人数、同意覆盖率（consented / in_residence）、在岗员工数、App 启用率、60 天内到期资质数；记录及时率、待审核、待归属显示"暂无数据（护士端未上线）"。**不出现个人指标**
- 养老院：`GET /org/facilities`、`POST /org/facilities`、`GET /org/facilities/:id`、`PATCH /org/facilities/:id`
- 上线：`GET /org/facilities/:id/go-live`、`PATCH /org/facilities/:id/go-live/items/:key`、`POST /org/facilities/:id/go-live/activate`
- 流程：`GET /org/facilities/:id/workflow-settings`、`PUT /org/facilities/:id/workflow-settings`（值不得超出公司上限）
- 员工：`GET /org/staff`（可按院筛选）、`POST /org/staff`、`POST /org/staff/import`（CSV）、`GET /org/staff/:id`、`PATCH /org/staff/:id`、`PUT /org/staff/:id/assignments`、`POST /org/staff/:id/invite`、`POST /org/staff/:id/training-complete`、`POST /org/staff/:id/deactivate`、`GET/POST /org/staff/:id/credentials`、`PATCH/DELETE /org/staff/:id/credentials/:credentialId`
- 老人：`GET /org/facilities/:id/residents`、`POST /org/facilities/:id/residents`、`POST /org/facilities/:id/residents/import`（CSV）、`GET /org/residents/:id`、`PATCH /org/residents/:id`、`POST /org/residents/:id/events`、`GET /org/residents/:id/consent`、`PUT /org/residents/:id/consent`
- `GET /org/audit`

错误统一为 `{ error: { code, message } }`，`message` 不含健康信息。所有写操作写 `audit_log`。

## 5. 页面

两个前端都用 `side-nav` 布局；列表用 `data-table`；每页一个表单、一个 submit；不可撤销操作用 `dialog` 确认；空状态用 `empty-state`；只用 DESIGN.md token。

**Super Admin（`carekind-super-admin`）**：登录 → 公司列表 → 新建公司 → 公司详情（资料、配置上限、养老院只读列表、公司管理员与邀请、停用 / 恢复）→ 平台默认配置 → 用量 → 审计日志

**机构管理端（`carekind-admin-web`）**：登录 / 接受邀请 → 公司总览 → 养老院列表 → 新增养老院 → 养老院详情（资料、上线清单、流程配置）→ 员工列表（按院筛选、CSV 导入）→ 员工详情（资料、分配、资质、邀请、培训、停用）→ 老人列表（按院）→ 老人详情（资料、生命周期事件、同意）→ 审计日志

## 6. 开发用种子数据

只用**合成数据**，文件名与注释标明"合成数据，仅用于开发与测试"（code-rules CORE-09 允许）：1 位平台管理员；2 家公司（隔离测试用）；公司 A 有 3 家院（NSW × 2、VIC × 1），约 12 名员工（含多院兼职与无 App 员工）、约 30 位老人（含同名、转院、离院）。姓名用明显虚构的名字，不用真人信息。

## 7. 完成标准（M0 管理端）

- [ ] `carekind-shared`：schema、类型、路径常量、API 客户端、`tokens.css` 生成脚本；单元测试通过
- [ ] `carekind-api`：上述接口；迁移与种子；测试覆盖跨租户拒绝、院级权限、平台接口字段扫描（SA-05）、老人生命周期、同意重置、上线闸门（含 NSW 14 天）、审计只追加
- [ ] 两个前端：上述页面，连真实 API 可走通；Vitest 覆盖表单校验与权限显示
- [ ] 所有子仓库 `npm run lint`、`npm run typecheck`、`npm test` 通过；meta repo `check_rules.py` 通过
- [ ] 各子仓库只有代码、测试、配置和一个简短 README；文档写在 meta repo

## 8. 实现记录（2026-10-20）

**结果**：shared `c572345`（111 个测试）、super-admin `9cf6011`（27）、admin-web `ba1b872`（36）、api `ae68da2`（59），均在各仓库 `m0-admin` 分支。联调脚本（合成数据）22/22 通过：两个前端可访问、CORS 只放行 5173 / 5174、平台登录、创建公司、邀请公司管理员（返回链接、不发邮件）、平台响应不含居民与同意数据、接受邀请、新建养老院 / 员工 / 老人、同意记录、生命周期（含非法事件被拒）、上线闸门、总览无个人数据、审计写入、跨公司读取被拒。

**实现中的补充规则**（待 Terry 确认）：
- 临时离院的老人可直接记录离院或去世（放宽 SPEC-011 §3.1 图）
- 新密码至少 14 位（不做 MFA 的补偿）
- 只有公司管理员能授予或修改公司管理员身份；不能停用自己；院级角色只能改本院分配；转院接收后清空房号
- 默认值：平台默认养老院上限 10、原音保留 7 天；新养老院未审核提醒 60 分钟、记录转入机构系统 7 天（PRD 未给默认值）
- 数据模型增加：`staff.last_login_at`（用量统计）、`audit_log.facility_id`（院级查看审计）
- PGlite 只有一个连接：所有查询必须在同一个事务里进行；开发数据库要用 Ctrl+C 正常停止，强制结束可能损坏 `.data/`（删除后重新 seed 即可）

**合同缺口**（下一轮补）：
1. 没有"重发邀请"接口（现为重新邀请，旧链接作废）；Super Admin 只有一种平台角色，"只读支持"角色未实现
2. 用量没有按周统计、没有待归属比例（护士端上线后才有数据）
3. 机构用户读不到公司上限：流程配置表单无法预先限制可选记录类型，靠服务端报错
4. DON 不能调用员工列表：流程配置里的"记录转入负责人"对 DON 不可选
5. 老人列表不含同意状态；事件历史只有养老院 ID
6. 平台修改 AI 开关或保留期上限时，"通知公司管理员"尚未实现（不发邮件，需站内通知方案）
