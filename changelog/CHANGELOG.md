# CHANGELOG

> AI 与重要人工改动的任务级记录。**最新在最上面，只追加不修改。** 规范：[changelog-rules.md](../company-os/11-rules/changelog-rules.md)
> 逐次文件编辑的自动记录在 [ai-edits.jsonl](ai-edits.jsonl)（Claude Code hook 生成）。

---

## 2026-10-20 · Claude Code · M0 管理端完成：API 完成并联调通过

- **请求人**：Terry（`CAREKIND_MEMBER` 未设置，待确认）
- **请求**：电脑恢复后继续开发（未使用云端任务，API agent 在本地续做）
- **改动**：
	- `carekind-api` `ae68da2`（`m0-admin`，agent 已 push）：全部接口、迁移（审计只追加触发器）、合成种子数据、59 个测试；修复 PGlite 单连接死锁与强制结束损坏数据库的问题
	- meta repo：更新 `services/carekind-api` submodule 指针；`m0-admin-tech-design.md` 测试行改为 Vitest，新增 §8 实现记录（补充规则、默认值、合同缺口）
- **检查**：本地启动 API（3000）、Super Admin（5173）、机构管理端（5174），用临时目录中的联调脚本调用共享 API 客户端，22/22 通过；`check_rules.py` 通过
- **待确认**：§8 中的补充规则与默认值；6 项合同缺口排入下一轮

---

## 2026-10-20 · Claude Code · M0 管理端开发（多 agent）：shared、Super Admin、机构管理端完成；API 转云端继续

- **请求人**：Terry（`CAREKIND_MEMBER` 未设置，待确认）
- **请求**：按 PRD 开发第一阶段管理端（不含护士端），可多 agent 并行；电脑没电前改为云端继续，下次打开时更新本地仓库
- **改动**（子仓库，均在 `m0-admin` 分支，已按 Terry 要求 push 到 GitHub；未合并 main）：
	- `carekind-shared` `c572345`：zod schema 与类型、业务规则纯函数、类型化 API 客户端、从 DESIGN.md 生成的 `tokens.css`；111 个测试通过
	- `carekind-super-admin` `9cf6011`：8 个页面，27 个测试通过
	- `carekind-admin-web` `ba1b872`：公司总览、养老院（上线清单、流程配置）、员工、老人（生命周期、同意）、审计；36 个测试通过
	- `carekind-api` `bbf7b28`：**未完成（WIP）**，NestJS + Drizzle + PGlite；本地 agent 因断电停止，交由一次性云端会话继续；Claude 把测试中 3 处被 SECRET 检查误报的测试值（伪造 token、错误密码）改为命名常量
	- meta repo：更新 4 个 submodule 指针
- **检查**：各子仓库 agent 报告 build / typecheck / lint / test 通过（API 除外，未完成）；`check_rules.py` 通过
- **待确认**：shared 与两个前端 agent 列出的合同缺口（重发邀请、按周用量、机构用户读取公司上限、DON 读取员工、居民列表显示同意状态等）待联调后汇总给 Terry；API 完成后需联调

---

## 2026-10-20 · Claude Code · carekind-blog 仓库与每日 8:00 草稿任务；根目录列出全部 submodule

- **请求人**：Terry（`CAREKIND_MEMBER` 未设置，待确认）
- **请求**：在 marketing ops 建立单独的 blog 仓库，每天早上 8 点查找澳洲本地养老行业新闻并撰写文章，保存成 md；把新增的 repo submodule 更新到根目录 README、CLAUDE.md、AGENTS.md。Terry 确认：`carekind-blog` 挂在 07 下、Claude 云端定时任务、公开仓库 + 草稿待审、英文
- **改动**：
	- GitHub（外部）：新建公开仓库 `terryxu0321/carekind-blog`（README、`drafts/`、`posts/`、格式配置），已推送初始提交；本仓库新增 submodule `company-os/07-marketing-operations/carekind-blog`
	- Claude 云端 routine "CareKind daily aged care blog draft"（`trig_014iJYD41XExw8fWTUMsZiby`）：cron `0 21 * * *` UTC（悉尼 08:00 AEDT），Sonnet 5.5，只写 `drafts/` 并 push；创建后清除了服务端自动挂上的 Gmail 等连接器
	- 新增 `07-marketing-operations/blog-editorial-guide.md`（每日草稿规则、格式、内容规则、发布前审核清单）；`07-marketing-operations/README.md`、`AGENTS.md` 登记
	- 根 `README.md`（新增"代码与内容仓库"表）、`AGENTS.md`（submodule 表与"先读"文件）、`CLAUDE.md`（submodule 与 hook 说明）；`engineering-standards.md` 仓库清单加 blog
- **原因与决策**：blog 文章是内容而非文档，放子仓库；写作规则是文档，留 meta repo。仓库公开，草稿一推送即公开可见，所以草稿也按市场合规规则写，标 `draft-pending-review`，AI 从不写 `posts/`；定时任务不挂连接器，避免对外发送（硬规则 3）
- **检查**：`check_rules.py` 通过；routine 创建成功，下次运行 2026-10-20T21:07Z（悉尼 10-21 08:07）
- **待确认**：⚠️ 2027-04-04 夏令时结束后 cron 改为 `0 22 * * *`；云端运行须能 push 到 `carekind-blog`（如首次运行报权限错误，需在 GitHub 上授权 Claude 访问该仓库）；草稿是否公开可见可接受，Terry 已选择公开

---

## 2026-10-20 · Claude Code · 先做管理端、表单设计规则、M0 管理端技术设计

- **请求人**：Terry（`CAREKIND_MEMBER` 未设置，待确认）
- **请求**：PRD 规划先做 Super Admin 与机构管理端，以 design system 为设计参考；design system 增加规则"一个页面只有一个表单、一个 submit"；第一阶段只做管理端，PRD 没完成先补完再开发（可多 agent，不含护士端）；不用 Docker
- **改动**：
	- `docs/PRD.md`：G2 M0 改为管理端（SPEC-010 + SPEC-011），AI 管线与护士端移到 M1；C1 新增建设顺序与设计参考
	- `design-system/DESIGN.md` v0.2.0 → v0.3.0：§7.3 新增"表单"规则、§8 Don't 新增一条；重新生成 `design-system.html`（安装了 PyYAML）
	- 新增 `m0-admin-tech-design.md`（实施选择、角色与权限、数据模型、API、页面、种子数据、完成标准）；`06-app-development/README.md`、`AGENTS.md` 登记
	- `specs/2026-10-super-admin-console.md`、`2026-10-provider-admin-console.md` 表头加阶段与设计参考；`src/super-admin/AGENTS.md`、`src/admin-web/AGENTS.md` 加设计组件说明
	- `engineering-standards.md` 数据库行注明 M0 用 PGlite + Drizzle、不用 Docker
- **原因与决策**：课程表中 ⏳ 的项（Vite、zod、认证、数据库、多租户）M0 先按技术设计实施，均放在接口后可替换；邀请不发邮件，只生成链接（硬规则 3）；多租户 M0 在 API 层隔离 + 跨租户测试，数据库层 RLS 待 ADR-0002；不用 Docker，本地数据库用 PGlite（曾短暂启动 Docker Desktop，已关闭）
- **检查**：`check_rules.py` 通过（exit 0）
- **待确认**：ADR-0002（多租户隔离）、托管身份服务、托管数据库；M0 技术设计待 Terry 审阅

---

## 2026-10-19 · Claude Code · 删除产品文档中的 MFA；创建 6 个子仓库并加为 submodule

- **请求人**：Terry（`CAREKIND_MEMBER` 未设置，待确认）
- **请求**：把 MFA 整个删掉（如果有）；按刚才的规划建立 repo 以及 submodule
- **改动**：
	- 删除 MFA：`docs/PRD.md`（C1 表与决定说明、M-01、SA-03、G4 #11 删除）、`engineering-standards.md`（Super Admin、认证、production 环境）、`specs/2026-10-super-admin-console.md`、`src/api/` 与 `src/super-admin/` 的 README 和 AGENTS、`src/README.md`
	- GitHub（外部）：新建 6 个公开仓库 `carekind-nurse-web`、`carekind-admin-web`、`carekind-super-admin`、`carekind-marketing-site`、`carekind-api`、`carekind-shared`，各含一个链接回 meta repo 的 README 与 `.editorconfig`、`.gitattributes`，已推送初始提交
	- 本仓库：新增 `.gitmodules` 与 6 个 submodule（`apps/`、`services/`、`packages/`）；**通过 Bash 新建**（hook 未记录）`apps/`、`services/`、`packages/` 各自的 README.md、AGENTS.md、CLAUDE.md
	- 根 `AGENTS.md`（meta repo 已建成、submodule 用法、根目录说明）；`engineering-standards.md` 仓库清单标为已创建
- **原因与决策**：只删产品文档里的 MFA；公司内部 IT 政策中的 MFA（员工设备、Google Workspace、`information-security-policy.md`、`company-rules.md` C-1.3、05-hr-teams）保留未改，待 Terry 决定；子仓库除 README 外不放文档
- **检查**：`check_rules.py` 通过（exit 0）；`git submodule status` 显示 6 个 submodule 均指向各仓库 `main`
- **待确认**：本仓库的 submodule 提交尚未 push；`carekind-shared` 的引用方式（git 依赖或包管理）待定

---

## 2026-10-19 · Claude Code · 本仓库改为 meta repo，应用代码拆为独立仓库（文档全部留在 meta repo）

- **请求人**：Terry（`CAREKIND_MEMBER` 未设置，待确认）
- **请求**：护士端、机构管理端、Super Admin、营销网站、API 都是单独的独立 repo，本 repo 变成 meta repo，独立 repo 作为 submodule 加入；所有文档就保存在 meta repo 里。Terry 确认：`carekind-` 前缀、公开、另建 `carekind-shared`、本次只更新文档
- **改动**：`engineering-standards.md`（工程流程表 + 仓库清单与文档规则）；`docs/PRD.md` C1 工程流程表；根 `AGENTS.md`（meta repo 说明）；`06-app-development/README.md`、`src/README.md`、`src/AGENTS.md`
- **原因与决策**：按 Terry 决定取代课程表中的单个 `carekind-app` monorepo；后端各模块合并在 `carekind-api` 一个仓库（模块化单体）；类型与校验只在 `carekind-shared` 定义一份；Demo 环境是同批仓库的独立部署，不另建仓库；子仓库只放代码、测试、配置和一个链接回 meta repo 的简短 README
- **检查**：`check_rules.py` 通过（exit 0）
- **待确认**：仓库尚未创建，submodule 尚未添加（Terry 选择只更新文档）；`carekind-shared` 的引用方式（git 依赖或包管理）待定

---

## 2026-10-19 · Claude Code · 工程流程与数据基础设施和课程结果对齐

- **请求人**：Terry（`CAREKIND_MEMBER` 未设置，待确认）
- **请求**：按老师的"工程流程"和"数据与基础设施"两张表保持一致
- **改动**：`docs/PRD.md` C1 新增两张表；`engineering-standards.md` 用两张表替换原"基础设施"表，环境表注明生产数据不进入其他环境；`06-app-development/README.md`、`src/AGENTS.md` 改为产品代码放在 `carekind-app` 仓库、以 git submodule 引入
- **原因与决策**：照课程结果原样记录，包括状态（✅ / 🟡 / ⏳）；多租户隔离从"行级安全"改为"行级安全或 schema 隔离，待技术 ADR-0002"；未创建 `carekind-app` 仓库或 submodule（只记录决定）
- **检查**：`check_rules.py` 通过（exit 0）
- **待确认**：仓库结构、托管数据库、多租户隔离（ADR-0002 待写）、IaC（CDK / Terraform）

---

## 2026-10-19 · Claude Code · 技术栈与课程结果对齐（前端 + 后端与 AI），API 框架定为 NestJS

- **请求人**：Terry（`CAREKIND_MEMBER` 未设置，待确认）
- **请求**：与老师的技术栈结果保持一致（前端表、后端与 AI 表）；API 框架用 NestJS
- **改动**：
	- `docs/PRD.md` C1：架构图改为四个独立前端；新增"前端"与"后端与 AI"两张技术栈表（含状态）；B2 改称机构管理端；G2 M1；版本说明
	- `engineering-standards.md`：技术栈拆为前端 / 后端与 AI / 基础设施三张表；环境表新增 demo（只用虚构数据，独立部署）
	- 护士端恢复为第一阶段完整 Web App（撤销"最小演示页"）：`specs/2026-10-shift-voice-capture.md`、`2026-10-review-and-sign-off.md`、`2026-10-incident-fast-track.md`、`src/mobile-app/`
	- 机构管理端改为独立 Web App：`specs/2026-10-provider-admin-console.md`、`src/admin-web/`、`src/README.md`、`src/AGENTS.md`、`06-app-development/README.md`、根 `AGENTS.md`
	- 营销网站只做英文、token 以 CSS 变量引入：`specs/2026-10-marketing-website.md`、`src/marketing-site/`
- **原因与决策**：Terry 要求以课程结果为准；Demo 环境作为独立部署环境记录，不新建代码模块；Vite、zod、实时推送、认证服务保持"待定"；LLM 方向已定（云厂商澳洲区域、零保留、锁定版本），供应商待选
- **检查**：`check_rules.py` 通过（exit 0）
- **待确认**：Vite、zod、Tier 3 实时推送（WebSocket / Web Push）、托管身份服务、LLM 具体供应商

---

## 2026-10-19 · Claude Code · ElevenLabs 数据在澳洲、统一 TypeScript、护士端第一阶段只做最小演示页

- **请求人**：Terry（`CAREKIND_MEMBER` 未设置，待确认）
- **请求**：ElevenLabs 可以用，数据在澳洲；统一 TypeScript；护士端 Web App 与 mobile app 可以规划但可以不做（Terry 选择：只做最小演示页）
- **改动**：`docs/PRD.md`（C1 护士端范围、TS、ElevenLabs 说明、架构图、G4 #10、G2 M1）；`engineering-standards.md` 技术栈表改为 MVP 选型（TS 全栈、S3 不做 CDN、ElevenLabs、不做 MFA）；`specs/2026-10-shift-voice-capture.md`、`2026-10-review-and-sign-off.md`、`2026-10-incident-fast-track.md`（第一阶段范围说明）、`2026-10-marketing-website.md`（脚本用 TS）、`2026-10-design-system.md`（移动端 DR 待决项关闭）；`src/mobile-app/`、`src/marketing-site/`、`src/ai-pipeline/transcription/` 的 README 与 AGENTS、`src/README.md`；`security/vendors-and-subprocessors.md`（ElevenLabs 区域改为澳洲）
- **原因与决策**：ElevenLabs 按 Terry 确认视为澳洲存储与处理，不再需要数据驻留 DR；公开文档截至当日未列澳洲区域，故保留"真实录音前在 DPA 书面确认（含处理环节）"的条件。Company OS 内部脚本仍为 Python，不属于产品代码。护士端演示页保留安全底线（第二标识、逐项确认、人工签字、未同意丢弃）
- **检查**：`check_rules.py` 通过（exit 0）
- **待确认**：ElevenLabs DPA / 合同条款；后端框架（Fastify / NestJS）与 LLM 供应商待技术栈 DR
- **补充**：Terry 同日决定规划中的 mobile app 用 React Native + TypeScript（`engineering-standards.md`、PRD C1、`src/mobile-app/`、`specs/2026-10-design-system.md` 已同步）

---

## 2026-10-19 · Claude Code · MVP 决定：去掉 MFA、转写用 ElevenLabs、S3 不做 CDN

- **请求人**：Terry（`CAREKIND_MEMBER` 未设置，待确认）
- **请求**：MFA（含 super admin 的 IP allowlist）去掉；语音转写只用 Terry 已有的 ElevenLabs，不用别的；对象存储用 S3，不做 CDN
- **改动**：`docs/PRD.md`（C1 决定说明与架构图、M-01、SA-03、G4 #10 #11）；`specs/2026-10-super-admin-console.md`、`2026-10-provider-admin-console.md`、`2026-10-shift-voice-capture.md`、`2026-10-marketing-website.md`；`src/api/`、`src/super-admin/`、`src/ai-pipeline/transcription/` 的 README 与 AGENTS、`src/README.md`；`security/vendors-and-subprocessors.md`（ElevenLabs 行，按 Terry 指示登记）
- **原因与决策**：按 Terry 决定执行，并加上前提条件 —— MVP 只处理合成数据；接入真实居民或员工数据前须加回 MFA，并解决 ElevenLabs 的数据驻留问题
- **检查**：`check_rules.py` 通过（exit 0）；ElevenLabs 官方数据驻留文档 2026-10-19 核查：区域为美国（默认）、欧盟、印度、新加坡，未列澳洲，驻留主要指存储
- **待确认**：
	- ⚠️ **ElevenLabs 与产品边界"数据与 AI 处理留在澳洲"冲突**（AGENTS 硬规则 4）：处理真实居民录音前须确认澳洲处理，或先写 DR 变更数据驻留边界并取得律师意见（APP 8、NSW HPP 14、VIC HPP 9）
	- ⚠️ 不做 MFA 与 `information-security-policy.md`（Essential Eight）不一致；本次未修改该政策，试点前须由 Terry 决定加回 MFA 或修订政策

---

## 2026-10-19 · Claude Code · 营销网站 SPEC-012（纯 HTML + CSS）

- **请求人**：Terry（`CAREKIND_MEMBER` 未设置，待确认）
- **请求**：缺少一个用来宣传 CareKind 的 marketing website；技术栈用纯 HTML，不用 Next.js
- **改动**：新增 `specs/2026-10-marketing-website.md`（SPEC-012）与模块 `src/marketing-site/`（README / AGENTS / CLAUDE）；`docs/PRD.md` C1 说明与 G2 M1；`src/README.md`、`src/AGENTS.md`、`06-app-development/README.md`、`specs/README.md` 索引
- **原因与决策**：网站文案即 TGA 意义上的预期用途，所以按 spec 管理；规则沿用 `marketing-compliance.md` 与 `brand-and-messaging.md`（禁用医疗用途词、无证据不写数字、不点名比较、Spam Act 单独同意、考拉不上网站）；纯 HTML + CSS + 少量原生 JS，与产品数据完全分离
- **检查**：`check_rules.py` 通过（exit 0；仅 ASSIGN 警告）
- **待确认**：隐私政策、使用条款、intended purpose 对外措辞 —— 律师；表单后台 / 分析工具选定后登记子处理方；SPEC-012 待 `assign-prd`

---

## 2026-10-19 · Claude Code · 养老院管理端：公司 → 多家养老院、员工与老人管理、四个流程

- **请求人**：Terry（`CAREKIND_MEMBER` 未设置，待确认）
- **请求**：养老院管理端要能管理护士、老人和本院全部员工；一家公司可能有多家、多地点养老院；要有流程管理，因为买单的是养老院 business owner。Terry 确认：四个流程都做（老人生命周期、员工生命周期、记录审核与上报、新养老院上线）；完整员工名册；老板看跨院汇总并可进入单院
- **改动**：
	- 新增 `specs/2026-10-provider-admin-console.md`（SPEC-011）
	- `docs/PRD.md`：层级改为 平台 → 公司（租户）→ 养老院；B2 新增公司管理员（买单者）与院长；B3 新增公司、养老院概念；C1 图与说明；C6 公司管理员说明；E6 新增 PA-01–PA-06，SA-01–SA-03 改为按公司；A7 注明员工名册不做排班/工资/绩效；G2 M1
	- 重写 `specs/2026-10-super-admin-console.md`（SPEC-010 改为开通客户公司，删除"不做集团层级"）
	- 修改 `src/admin-web/`、`src/super-admin/` 的 README 与 AGENTS，`src/api/AGENTS.md`、`src/README.md`、`src/AGENTS.md`、`06-app-development/README.md`、`specs/README.md`、`product-feature-map.md`、根 `AGENTS.md`
- **原因与决策**：租户 = 公司，养老院为其下地点，员工属于公司可多院分配，老人属于一家院；老人状态决定 AI 归属候选范围（降低错误老人风险）；总览只到养老院级、不做个人排名（员工监控合规）、不展示临床风险指标（TGA）；资质到期只提醒不判定
- **检查**：`check_rules.py` 通过（exit 0；仅 ASSIGN 警告）
- **待确认**：
	- 完整员工名册引入**员工个人信息与资质**这一新数据类型 → 需更新 PIA；也让产品向 HR 方向扩展，与 PRD A7 的边界需持续把关
	- 同公司内转院时旧院记录对新院员工的可见范围 —— Clinical Lead 与律师
	- SPEC-011 待 Terry 审阅与 `assign-prd`

---

## 2026-10-19 · Claude Code · 第一阶段前端：护士 Web App + 独立 Super Admin App（多养老院）

- **请求人**：Terry（`CAREKIND_MEMBER` 未设置，待确认）
- **请求**：第一阶段也要做 super admin 管理多个养老院、可配置，单独的 React JS app；护士端先做 web app，不做 mobile app。Terry 确认：super admin = CareKind 平台方；机构管理员页面放进护士 Web App
- **改动**：
	- `docs/PRD.md` → v0.2：C1 架构图与"第一阶段前端"说明；B2 新增平台管理员角色；C6 权限表加 Super Admin 列（不可见居民记录）；E6 新增 SA-01–SA-04；R-02 完整离线队列降为 P1（重试不丢失仍必须）；E7 设备；G2 M1
	- 新增 `specs/2026-10-super-admin-console.md`（SPEC-010）
	- 新增模块 `src/super-admin/`（README / AGENTS / CLAUDE）
	- 修改 `src/mobile-app/`、`src/admin-web/` 的 README 与 AGENTS（第一阶段实现方式）、`src/api/AGENTS.md`（多租户隔离）、`src/README.md`、`src/AGENTS.md`、`06-app-development/README.md`、`specs/README.md`、`product-feature-map.md`、`specs/2026-10-shift-voice-capture.md`（R-02）、根 `AGENTS.md`（架构说明）
- **原因与决策**：不改文件夹名（避免 20+ 处链接失效）——`mobile-app/` 第一阶段以 Web App 实现，`admin-web/` 作为其中按角色显示的模块；Super Admin 不接触居民健康信息，满足最小必要与处理方角色；未改变 TGA、录音模式、HITL、数据驻留边界，故不需 DR
- **检查**：`check_rules.py` 通过（exit 0；仅 ASSIGN 警告）
- **待确认**：SPEC-010 待 Terry 审阅与 `assign-prd`；DPA 中"不访问居民数据"与运维排障（break-glass）的平衡、用量数据去标识粒度 —— 律师；集团层级（平台 → 集团 → 养老院）留到后续

---

## 2026-10-19 · Claude Code · 多 agent 调研：各州法规、竞品解法、真实流程与 paperwork → MVP 功能 spec 与模板

- **请求人**：Terry（`CAREKIND_MEMBER` 未设置，待确认）
- **请求**：启动多个 agent 并行调研澳洲各州 aged care 法规、竞争对手如何解决问题、best practice、真实流程图与所需 paperwork；再据此分析产品功能、写对应 PRD、把 paperwork 转成 Markdown 模板；学习项目 MVP，调研差不多即收尾；合并进 main
- **改动**：
	- 新增 `company-os/03-legal-compliance/research/`：`state-deep-dive-nsw-vic-act.md`、`state-deep-dive-qld-wa-sa-tas-nt.md`（州法深挖 + 对 `state-by-state-comparison.md` 的纠错建议）、`aged-care-documentation-workflows.md`（9 个流程 Mermaid 图 + 临床/AI 文档 best practice）、`aged-care-paperwork-checklist.md`（约 60 种文档总表）
	- 新增 `company-os/07-marketing-operations/competitor-research/how-competitors-solve-it.md`（竞品解法、patterns、市场空白、应避免做法、对比表）
	- 新增 `company-os/06-app-development/product-feature-map.md`（问题 → 解决方案 → 功能映射 + best practice 汇总）
	- 新增 6 份 P0 spec：SPEC-004 班次语音采集、SPEC-005 居民归属、SPEC-006 草稿生成与护栏、SPEC-007 审核签字、SPEC-008 事件快速通道、SPEC-009 同意管理
	- 新增 `company-os/templates/paperwork/`（README / AGENTS / CLAUDE + 8 个模板：progress note、事件记录、ISBAR、care plan 复审、限制性措施使用、居民 AI 同意书、员工监控通知、机构上线清单）
	- 修改索引：`research/README.md`、`competitor-research/README.md`、`06-app-development/README.md` 与 `AGENTS.md`、`specs/README.md`、`templates/README.md` 与 `AGENTS.md`
- **原因与决策**：按 Terry 要求缩为 MVP 规模（12 份 spec → 6 份 P0；模板 8 个）；spec 不改产品边界（按键口述、HITL、documentation-only、澳洲驻留），只细化 PRD；Assignee 未指定，待 `assign-prd`；纠错建议与 competitor-matrix 更新只列出，未改原文件、合规登记册和 hazard log
- **检查**：`check_rules.py` 通过（exit 0；仅 ASSIGN 警告，含 6 份新 spec）；各 agent 已逐个核对相对链接
- **待确认**：
	- 法律：模式 A 单人口述不算"私人对话"需律师书面确认；NSW HPP 14 / VIC HPP 9 / TAS / NT 管"出州"，托管区域须写进合同；同意书与员工通知措辞；居民无能力时谁可代为同意
	- TGA：2026-10-16 报道 TGA 审查 12 款 scribe 中 8 款可能属器械（官方原文未直接打开）；SPEC-008 计时与缺失字段提示的边界须监管顾问确认
	- 竞品：voize（德国）已做"口述→自动归属居民"，归属不能宣称独有
	- `federal-law-summary.md` §1.8 关于 care minutes 的表述与新指南不一致，建议修正
	- SPEC-004/005/006 建议 hazard 编号 H-19–H-24，SPEC-007–009 未编号，待 Clinical Lead 统一

---

## 2026-10-19 · Claude Code · 新增 10 个用户画像（谁买 / 谁用 / 谁受益 / 谁审核）

- **请求人**：Terry（`CAREKIND_MEMBER` 未设置，待确认）
- **请求**：总结产品的用户画像，设置 10 种常见画像，从谁买、谁用、谁受益、谁审核几个维度思考，写进项目
- **改动**：
  - 新增 `docs/user-personas.md` —— 四维定义、画像总览矩阵、P1–P10 画像卡、画像关系图、对产品/销售/设计的含义、待验证假设、法律依据
  - 修改 `docs/PRD.md` —— B2 末尾加一行链接到画像文档（不改产品边界）
  - 修改 `docs/README.md`、`docs/AGENTS.md` —— 文档索引加入 `user-personas.md`
- **原因与决策**：放在 `docs/` 与 PRD 并列，因为画像供产品、销售、设计共用；画像以 PRD B2/C6/D1、ICP 和销售流程为依据；`08-feedback/raw/` 尚无原始反馈，所以全部标为待验证假设，不写姓名、代词，不编造数字；“审核”分为记录复核与采购把关两层；画像冲突时的取舍顺序为居民安全 > RN 复核责任 > 一线效率 > 管理需求
- **检查**：`check_rules.py` 通过（exit 0，仅既有 ASSIGN 警告）；新文件相对链接均存在
- **待确认**：画像与取舍顺序需 Terry 审阅；P4 质量与风险经理是否在中小机构与 DON 合并，待 M0 访谈验证

---

## 2026-10-11 · Claude Code · 吉祥物「考拉小记」、透明 PNG、VI 手册与周边设计

- **请求人**：Terry（`CAREKIND_MEMBER` 未设置，待确认）
- **请求**：设计吉祥物（三个方向中选定考拉），细化并导出 SVG；导出 logo 与吉祥物的透明背景 PNG；出一套吉祥物设计风格、VI 设计图和周边设计图
- **改动**：
  - 新增 `brand-assets/mascot-koala-hello.svg`、`-writing.svg`、`-done.svg`、`-avatar.svg`
  - 通过脚本生成（hook 未捕获）：`brand-assets/png/` 下 8 个透明背景 PNG（headless Chrome 渲染，脚本在会话临时目录，未入库）
  - 修改 `brand-assets/README.md` —— 吉祥物、PNG、VI 手册链接；`brand-and-messaging.md` —— 吉祥物一行
  - 仓库外：设计画布 VI 手册（4 张图板：吉祥物风格、VI 规范、办公与数字应用、周边），私有
- **原因与决策**：吉祥物定位为“记录助手”而非护士，不带医疗符号，不进入护理记录与面向长者的资料（TGA 边界、尊重长者语气规则）；名片、工牌等用 `[姓名]` 等占位，不编造人员信息；周边标语取自品牌文件中的候选
- **检查**：PNG 已确认为 RGBA（透明）且尺寸正确；`check_rules.py` 通过（exit 0，仅既有 ASSIGN 警告）
- **合并说明**：推送时远程 `main` 已合并 DESIGN.md（单一蓝色 #0066cc）。Terry 选定“两套并存”：DESIGN.md 管界面与网站 token，青绿 + 珊瑚只用于 logo、吉祥物、周边与印刷品 —— 已写入 `brand-and-messaging.md` 与 `brand-assets/README.md`
- **待确认**：吉祥物英文名；标语定稿；商标检索；PNG 文字转轮廓后重导出

---

## 2026-10-11 · Claude Code · 设计 Logo（方案 C「声音里的心」）并导出 SVG

- **请求人**：Terry（`CAREKIND_MEMBER` 未设置，待确认）
- **请求**：设计 logo；给出 A/B/C 三个方向后，选定方案 C（心形 + 声波），细化并导出 SVG
- **改动**：
  - 新增 `company-os/07-marketing-operations/brand-assets/` —— 6 个 SVG（横版、深色横版、图形标志、单色、App 图标、favicon）与 `README.md`（文件用途、颜色、使用规则）
  - 修改 `company-os/07-marketing-operations/brand-and-messaging.md` —— "视觉（待设计）"改为草稿：logo 与色值
  - 修改 `company-os/07-marketing-operations/README.md` —— 目录结构加入 `brand-assets/`
- **原因与决策**：小尺寸下 5 条声波会糊在一起，所以 favicon 单独做了 3 条、加粗的版本；珊瑚色 `#E8875B` 在白底上对比度不足，文字改用 `#C2410C`（WCAG AA）；不使用医疗符号（TGA 措辞边界）。`brand-assets/` 是模块内子目录，按 AC-1 不要求三件套，只加 README（与 `competitor-research/` 一致）
- **检查**：`check_rules.py` 通过（exit 0，仅既有 ASSIGN 警告）
- **待确认**：商标检索（IP Australia）；文字转轮廓需在设计工具中完成；设置 `CAREKIND_MEMBER`

---

## 2026-10-11 · Claude Code · 离线单文件 design-system.html（由 DESIGN.md 生成）

- **请求人**：Terry
- **请求**：生成单文件 design-system.html 放进仓库；另：不要自动 push
- **改动**：
  - 新增 `company-os/06-app-development/design-system/build_design_html.py` —— 读取 DESIGN.md 的 YAML token 与正文、`components/` 的说明与预览，生成单文件页面（标准库 + PyYAML）
  - 新增 `design-system/design-system.html`（生成文件，196 KB）—— 规范全文、颜色（生成时计算对比度）、字体、间距 / 圆角 / 尺寸 / 层次 / 动效、35 个组件（沙盒 iframe 实时预览 + 用法）、封面；无外部资源，可离线打开
  - 新增 `design-system/components/`（README / AGENTS / CLAUDE + 35 个 `<Name>.md` 与 36 个 `<Name>.preview.html`）—— 从设计系统页面的源文件复制入库（通过命令复制，hook 未捕获）
  - 修改 `design-system/README.md`、`design-system/AGENTS.md`、根目录 `AGENTS.md`（新增构建命令；写明"不自动 push，本地提交并列出改动，用户要求时才 push"）
- **原因与决策**：HTML 不手写，由脚本从 DESIGN.md 生成，避免两份规范（DRY）；组件平铺在一个目录，只需一套三件套；预览放在沙盒 iframe 中，避免与页面样式冲突
- **检查**：结构检查（35 个组件、36 个 iframe、23 个导航链接、无外部 URL、所有 `var(--…)` 已定义、标签闭合）；`check_rules.py` 通过
- **待确认**：本次**未 push**，等 Terry 确认后再推送；浏览器中目视检查由 Terry 进行

---

## 2026-10-11 · Claude Code · 仓库公开后的隐私检查与调整

- **请求人**：Terry
- **请求**：（告知）GitHub 仓库已改为 public
- **改动**：
  - 修改 `company-os/11-rules/hook_log_change.py` —— 仓库外的文件不再写入 `ai-edits.jsonl`（不再记录本机绝对路径）
  - 修改根目录 `AGENTS.md` 环境说明 —— 仓库已公开；提交的内容对所有人可见，不得提交密钥、真实居民或个人信息、本机绝对路径、`research/downloads/` 中有许可限制的 PDF
- **原因与决策**：扫描结果：无密钥、文件内容中无邮箱或电话；已提交的 `ai-edits.jsonl` 有 2 行本机绝对路径（memory 与临时脚本）和 Windows 用户名，按规则不手工修改该文件；5 个已推送提交的作者邮箱是个人邮箱，修改需要重写历史并强制推送，由 Terry 决定
- **检查**：hook 单元测试（仓库内文件记录、仓库外文件跳过）；`check_rules.py` 通过
- **待确认**：是否重写历史隐藏提交邮箱；以后提交改用 GitHub noreply 邮箱；是否添加 LICENSE；设计系统页面仍为私有

---

## 2026-10-11 · Claude Code · DESIGN.md v0.2.0 常用组件标准化 + 给人看的设计系统页面

- **请求人**：Terry
- **请求**：生成给人看的 HTML 版 design md；常用组件（如 dropdown、upload、toast）全部按 DESIGN.md 做标准化设计
- **改动**：
  - 修改 `company-os/06-app-development/design-system/DESIGN.md` → v0.2.0：新增 20 个组件的 YAML 规格与 §7.3 说明（select、menu、checkbox、radio、switch、textarea、date-time-input、file-upload、toast、dialog、bottom-sheet、progress、empty-state、status-tag、tabs、tab-bar、side-nav、list-item、data-table、accordion），共 47 个组件定义；新增规则：虚线只用于 AI 草稿、错误不用 toast、不可撤销操作用 dialog 且不用红色按钮
  - 发布设计系统页面（claude.ai Design System 类型，私有）：https://claude.ai/artifact/CbgRvJbxBDYAiVv3zZCa6k —— 品牌手册、tokens（由脚本从 DESIGN.md YAML 生成，值完全一致）、35 个组件卡片（说明 + 静态实时预览，只用合成数据）、封面
  - 修改 `design-system/README.md`（链接页面）、T-0004 背景（改为在 DESIGN.md 上核对与补全）
- **原因与决策**：DESIGN.md 仍是唯一来源，页面是镜像；新组件只用现有 token，没有新增颜色；App 中无阴影，菜单与下拉用 `border-input` 细边分隔；`status-tag` 明确只表示记录 / 系统状态（TGA）；上传区用实线以保留"虚线 = AI 草稿"的信号；日期 DD/MM/YYYY、24 小时制
- **检查**：DESIGN.md YAML 解析通过、全部 `{token}` 引用可解析（47 个组件）；tokens.json 由脚本生成（36 色、14 个文字样式）；页面发布成功（74 个文件）；`check_rules.py` 通过
- **待确认**：页面为私有，需 Terry 从 Share 菜单分享给团队；图标集未选（预览中用文字符号代替）；夜班主题尚未作为独立主题（T-0002）；DESIGN.md 更新后需同步页面

---

## 2026-10-11 · Claude Code · DESIGN.md：设计规范唯一来源（Terry 选定的极简风格）

- **请求人**：Terry
- **请求**：把 Terry 选定的设计风格（参考 Apple 网站视觉语言的规范文本）保存为 CareKind 的 design system 与 design md，作为设计规范的唯一来源
- **改动**：
  - 新增 `company-os/06-app-development/design-system/DESIGN.md` —— YAML token（36 色、字体、间距、尺寸、圆角、层次、动效、27 个组件）+ 用法说明、Do / Don't、响应式、偏差表；新增同目录 README / AGENTS / CLAUDE
  - 修改 SPEC-003 §5.6（交付物指向 DESIGN.md）；T-0001 标记 `done`（Terry 直接选定方向）；T-0002 背景改为在 DESIGN.md 上校验与补全
  - 修改根目录 `AGENTS.md`（规则表：任何 UI 工作先读 DESIGN.md）、`06-app-development/AGENTS.md`、`07-marketing-operations/brand-and-messaging.md`（视觉一节指向 DESIGN.md）
- **原因与决策**：保留参考风格的核心（单一蓝色强调色、近黑文字、浅 / 近黑表面、胶囊按钮、无阴影无渐变），按 SPEC-003 与 WCAG 调整：次要灰字 #7a7a7a → #6e6e73（原 4.29:1 不达标）、控件边界改用 #86868b（原 1.32:1）、触控 44 → 48px、App 禁用 300 细体与 < 14px 文字、新增状态色层（草稿 / 已确认 / 错误 / 需核对 / 离线，全部 ≥ 4.5:1，浅色与夜班两套）并禁止用于临床风险；不打包 SF Pro（许可面向 Apple 平台，未经律师核实），用 system-ui + Inter 后备；不使用他人商标。token 只存在 DESIGN.md 一处（DRY），平台产物由 T-0007 生成
- **检查**：脚本计算 33 组颜色对比度；YAML 解析通过、全部 `{token}` 引用可解析（脚本放在会话临时目录，未入库）；`check_rules.py` 通过（exit 0，仅既有 ASSIGN 警告）
- **待确认**：SF Pro 许可结论待核实；图标集选型；Dave 在 T-0002 / T-0005 中按 DESIGN.md 继续

---

## 2026-10-11 · Claude Code · Design System spec（SPEC-003）、任务分配给 Dave，规则改为"整份 PRD 归一人"

- **请求人**：Terry
- **请求**：给 CareKind AI 做 design system，把任务分配好；追加：整份 PRD 与全部任务分配给一个人（Dave），并更新分配规则与 skill
- **改动**：
  - 新增 `company-os/06-app-development/specs/2026-10-design-system.md`（SPEC-003，L3）—— 原则、tokens、基础组件、安全关键组件（H-01/02/03/06/07/08/09）、文案、无障碍、法律依据、评测计划、任务表；`Assignee: Dave`（Terry 确认）
  - 新增 `company-os/03-legal-compliance/checks/2026-10-11_design-system.md` —— 有条件通过
  - 新增 `company-os/06-app-development/adlc/`、`adlc/tasks/`（各含 README / AGENTS / CLAUDE）与任务 T-0001 至 T-0009（ADLC §6.1 格式，状态 `ready`，Terry 确认）：负责人 / 执行者均为 Dave（T-0009 由 Claude Code 代执行），评审人 Terry
  - 修改 `company-os/11-rules/prd-assignment-rules.md` —— 新增 §3a"整份 PRD 归一人（含全部任务）"；§4、§7 去掉"协作者 / 按任务分人"
  - 修改 `company-os/10-skills/assign-prd/SKILL.md` —— 新增"同步任务"步骤；禁止把同一 PRD 的任务分给不同成员、禁止自审
  - 修改 ADLC spec §6.3 新增 AS-7；DR-007 补充说明；`specs/README.md`、`10-skills/README.md`
  - 通过脚本生成（hook 未捕获）：`sync_skills.py` → `.claude/skills/`、`.agents/skills/`
- **原因与决策**：SPEC-003 含 HITL 审核安全组件，按分配规范定为 L3 → Senior（Dave）。无障碍法律本地未覆盖，按 L-4 不凭记忆引用，建 T-0009 先补充本地文件。设计系统禁止临床严重程度 / 风险等级类组件（TGA）。只启用 ADLC 的任务文件部分，未实现阶段管理与 `adlc.py`。评审人 ≠ 执行者（AS-2），默认 Terry
- **检查**：`check_rules.py` 通过（exit 0；其余 3 份 PRD 未分配 WARN）；`work_items.py` 显示 9 个任务与 SPEC-003 均在 Dave 名下；skill 已同步
- **待确认**：Terry 审阅 SPEC-003 正文；H-17、H-18 待 Clinical Lead；设计工具选型；移动端技术栈 DR；Dave 一人承担 9 个任务，截止日是否需要放宽（WIP 上限 3）

---

## 2026-10-11 · Claude Code · 初始化 git 仓库

- **请求人**：Terry
- **请求**：把本项目建成 git 仓库
- **改动**：
  - `git init -b main`，首次提交 `87d312e` 包含全部 271 个现有文件（通过命令执行，hook 未捕获）
  - 新增 `.gitattributes` —— 统一 LF 换行（与 `.editorconfig` 一致，避免 Windows `core.autocrlf` 转成 CRLF）；PDF / 图片 / Office 文件按二进制处理
  - 修改 `.gitignore` —— 忽略 `.claude/worktrees/`（Claude Code 后台会话的隔离工作区）
  - 修改根目录 `AGENTS.md` 环境说明 —— 由"不是 git 仓库"改为本地 git 仓库说明
- **原因与决策**：沿用已有 `.gitignore`（排除密钥、缓存、本地 Claude 设置、`research/downloads/` 中约 80MB 的法律 PDF）；暂存前确认无 `.env`、密钥、`__pycache__`、PDF 被纳入。成为 git 仓库后，后台会话须在 worktree 中修改，因此以上三处改动在分支 `worktree-git-setup` 上提交，待合并。未添加远程仓库、未推送（对外发布须先确认）
- **检查**：`git status` / `git ls-files` 核对提交内容；`check_rules.py` 通过
- **待确认**：合并分支 `worktree-git-setup`；是否创建 GitHub 私有仓库并推送（ADLC spec 中 GitHub 为 Phase 2，需登记子处理方）；仓库位于 OneDrive，`.git` 被同步可能产生冲突 —— 建议对本文件夹选"始终保留在此设备上"，或日后迁出 OneDrive

---

## 2026-10-11 · Claude Code · 成员工作记录、待办提醒与 AI 每日站会（work-log-rules）

- **请求人**：Terry
- **请求**：成员用 AI 操作仓库时自动记录每个人的工作；记录每人分配的工作并可随时提醒未完成项，作为规则。追加：每位成员在 AI 中提交站会（写成 skill），提醒未完成 PRD、新分配 PRD、Blocker，并存档每人的站会报告。补充说明：这是学习项目，Ahmad / Matt / Dave 为假设成员
- **改动**：
  - 新增 `company-os/11-rules/work-log-rules.md`（WL-1 至 WL-8）与 `DR-008-member-work-log-and-standup.md`（提议中，附员工书面通知草稿）
  - 新增 `company-os/11-rules/work_items.py` —— 每人未完成工作（PRD Assignee + ADLC 任务）、单人工作记录（CHANGELOG 请求人 + ai-edits）、SessionStart 提醒（含"今天站会未交"）
  - 新增 `company-os/11-rules/standup.py` —— 提交前提醒（新分配 / 不再负责的 PRD、上次计划与 Blocker）、每日汇总
  - 新增 skill `company-os/10-skills/standup/`、`work-status/`；新增目录 `company-os/02-operating-rhythm/standups/`（README / AGENTS / CLAUDE）
  - 修改 `hook_log_change.py` —— 记录 `member`（来自 `CAREKIND_MEMBER`）；`.claude/settings.json` —— 新增 SessionStart hook
  - 修改 `operating-cadence.md`（站会改为在 AI 中提交）、`changelog-rules.md`（请求人 = 当前成员）、`02-operating-rhythm/AGENTS.md`、`10-skills/README.md`、`11-rules/README.md` 与 `AGENTS.md`、根目录 `AGENTS.md`（命令、规则表、学习项目说明）、`CLAUDE.md`（hook 说明）
  - 通过脚本生成（hook 未捕获）：`sync_skills.py` → `.claude/skills/`、`.agents/skills/`（12 个 skill）
- **原因与决策**：待办只读 PRD Assignee 与 ADLC 任务，不另建清单（DRY）；ADLC 任务目录尚未建立，届时自动生效。成员身份用环境变量，Terry 可扮演任一假设成员练习。为避免员工监控风险，不统计数量 / 耗时 / 提交率 / 排名，工作记录只能按单人查看；NSW Workplace Surveillance Act 通知义务在有真实员工后适用（setup-checklist §F）。提醒他人只出草稿，不对外发送
- **检查**：`check_rules.py` 通过（exit 0，仅既有 ASSIGN 警告）；`settings.json` JSON 有效；手工测试：全队待办、`--me` 未设置 / 已设置、`--log`、非名册成员报错、站会上下文（含用替身数据测试"新分配 PRD"）、站会汇总、hook 写入 `member` —— 均符合预期，测试用站会文件已删除；skill 已同步
- **待确认**：DR-008 是否确认；Terry 在自己机器上设置 `CAREKIND_MEMBER`；ADLC 任务目录何时建立；SessionStart hook 需新会话才生效

---

## 2026-10-11 · Claude Code · 更新团队成员级别与特点

- **请求人**：Terry
- **请求**：Dave 是 Senior，Ahmad 是 Junior，Matt 擅长 DevOps；Ahmad 有产品思维和审美能力 —— 更新到团队资料
- **改动**：
  - 修改 `company-os/05-hr-teams/team-roster.md` —— Ahmad 级别 Junior、Dave 级别 Senior、Matt 主方向"后端与基础设施（DevOps）"；更新日期
  - 修改 `team-members/ahmad.md`、`matt.md`、`dave.md` 的"技能"一节
  - 修改 `teams/engineering/README.md` —— 成员表改为 级别 + 特点，并指向名册为准
  - 修改 `company-os/11-rules/prd-assignment-rules.md` §3 第 2 步 —— 选人时参考个人档案"技能"
- **原因与决策**：DevOps 归入规范中的"后端与基础设施"方向；未给出的信息（Matt 级别；Ahmad、Dave 主方向；技术栈）保持 `[待填]`，不推断
- **检查**：`check_rules.py` 通过（exit 0）
- **待确认**：Matt 的级别；Ahmad 与 Dave 的主方向

---

## 2026-10-11 · Claude Code · PRD 分配规范：按难度与成员级别、方向分配

- **请求人**：Terry
- **请求**：设置 PRD 分配规则，按每个成员的特点（全栈 / 简单任务、Junior / Senior、方向）分配，并给出建议
- **改动**：
  - 新增 `company-os/11-rules/prd-assignment-rules.md` —— 成员级别（Junior/Mid/Senior/Lead）与主方向；PRD 难度 L1–L3（改变 AI 输出、HITL、签字记录、认证/数据驻留、回写、≥3 模块 → L3）；选人顺序 门槛 → 方向 → 负荷上限 → 轮换；Junior 成长任务；制衡；公平与反歧视；与 ADLC 任务级分配的分工
  - 新增 `company-os/02-operating-rhythm/decisions/DR-007-prd-assignment-by-level.md` —— 状态"提议中"，未登记到 decision-log
  - 修改 `company-os/05-hr-teams/team-roster.md` —— 新增"级别""主方向"两列（Terry = Lead，其余 `[待填]`）；待决定项改为填写级别与主方向
  - 修改 `team-members/ahmad.md`、`matt.md`、`dave.md` —— "主要方向"改为指向名册（唯一来源）
  - 修改 `company-os/10-skills/assign-prd/SKILL.md` 步骤 3 与输出 —— 按新规范判定难度、给建议、对不满足门槛的指定发出提示
  - 修改 `company-os/11-rules/README.md`、`AGENTS.md`，根目录 `AGENTS.md` 规则表 —— 登记新规范
  - 通过脚本生成（hook 未捕获）：`python company-os/10-skills/sync_skills.py` → `.claude/skills/`、`.agents/skills/`
- **原因与决策**：级别与方向只由 Terry 评定，AI 不推断、不编造（硬规则 7）；级别匹配不加自动检查，由 🛑 确认把关（KISS）；负荷上限只是规范中的数字，未写入 `rule_config.py`（无脚本使用）。与同日 ADLC spec 不冲突：ADLC §6 管任务级执行者/评审人，本规范管 PRD 级 Assignee
- **检查**：`check_rules.py` 通过（exit 0；3 条 WARN：现有 PRD 未分配）；skill 已同步，两份副本均包含新规范引用
- **待确认**：DR-007 是否确认；Ahmad / Matt / Dave 的级别与主方向；负荷上限（Junior 1、Mid 2、Senior 2、Lead 1）是否合适；反歧视条款未经律师核实

---

## 2026-10-11 · Claude Code · 新增 ADLC（AI 协作开发生命周期）spec：任务分配、PRD 阶段管理与状态记录

- **请求人**：Terry
- **请求**：为在项目中实施 ADLC 写一份 PRD —— 能分配任务、用 ADLC 管理所有 PRD、记录 PRD 状态
- **改动**：
  - 新增 `company-os/06-app-development/specs/2026-10-adlc-delivery-lifecycle.md` —— SPEC-002：S0–S8 阶段与闸门、PRD 元数据与只追加状态历史、生成式登记表 `docs/prd-registry.md`、任务文件与分配规则 AS-1 至 AS-6、AI 执行者权限、功能需求 AD-*、实施计划与验收、法律依据
  - 新增 `company-os/03-legal-compliance/checks/2026-10-11_adlc.md` —— 合规检查：有条件通过
  - 修改 `company-os/06-app-development/specs/README.md` —— "现有 specs"加入本 spec
- **原因与决策**：ADLC 是内部研发流程，放在 specs/ 按 spec-writer 走（含法律依据），不改动总 PRD；不改变产品边界，故无需 Type 1 DR。第一阶段只用仓库文件 + Python 标准库脚本（非 git 仓库、无新子处理方），GitHub 同步列为 Phase 2 并建议 Type 2 DR。复用同日新增的 `assign-prd`：Owner/Assignee 仍以 PRD 表头为唯一来源，ADLC 元数据不重复存储，S5 前必须已有 Assignee。为规避 NSW 员工监控风险，看板不做个人统计/排名/耗时。本次只写 spec，未实现脚本、未修改 `docs/PRD.md`、hazard log、隐私计划或合规登记册（只在检查中建议）
- **检查**：`check_rules.py` 通过（exit 0；仅 ASSIGN 警告：3 份 PRD 未分配 Assignee）；两个新文件相对链接 0 断链
- **待确认**：🛑 Terry 审阅 spec；本 spec 的 Assignee（`assign-prd`）；律师确认 ADLC 工作记录是否构成 NSW Workplace Surveillance Act 下的计算机监控；RDTI 记录保存要求需先用 `regulatory-watch` 补充本地文件；建议 hazard H-16 待 Clinical Lead；是否在 PRD D10 加 ADLC 链接

## 2026-10-11 · Claude Code · 新增 skill assign-prd：每个 PRD 有且仅有一个 Assignee

- **请求人**：Terry
- **请求**：新增一个 skill，把 PRD 分配给团队成员，每个 PRD 有且仅有一个负责人（Assignee）
- **改动**：
  - 新增 `company-os/10-skills/assign-prd/SKILL.md` —— 分配 / 改派 / 一览；🛑 Terry 确认后才写入；只写一行 `Assignee`
  - 修改 `company-os/11-rules/check_rules.py` —— 新增 ASSIGN 检查：多于一行、多个名字、占位或非名册成员 → 失败；未分配 → WARN
  - 新增 `company-os/02-operating-rhythm/decisions/DR-006-prd-single-assignee.md` —— 状态"提议中"，未登记到 decision-log
  - 修改 `company-os/10-skills/README.md`（技能清单）、`company-os/06-app-development/specs/README.md`（模板加 Assignee 行）、`company-os/11-rules/README.md` 与 `AGENTS.md`（检查列表加 ASSIGN）
  - 通过脚本生成（hook 未捕获）：`python company-os/10-skills/sync_skills.py` → `.claude/skills/assign-prd/`、`.agents/skills/assign-prd/`
- **原因与决策**：PRD 范围 = `docs/PRD.md` + `specs/*.md`（不含 README）。Assignee 写在 PRD 头部作为唯一来源，不另建登记表（DRY）；Assignee 与 Owner（产品决策人）区分。未分配暂为 WARN，避免在负责人确定前阻塞检查；没有替现有 PRD 选择负责人
- **检查**：`check_rules.py` 通过（2 条 WARN：两份现有 PRD 未分配）；临时文件测试 11 种 Assignee 写法，结果均符合预期；skill 已同步
- **待确认**：DR-006 是否确认并登记；`docs/PRD.md` 与 `specs/2026-10-shift-voice-to-resident-records.md` 分别由谁负责；确认后是否把"未分配"升级为失败

---

## 2026-10-10 · Claude Code · /init：改进根目录 CLAUDE.md 与 AGENTS.md

- **请求人**：Terry
- **请求**：运行 `/init`，为以后的 Claude Code 会话生成/改进 CLAUDE.md
- **改动**：
  - 修改 `CLAUDE.md` —— 加入 `/init` 标准开头；保留 `@AGENTS.md` 导入；新增"Claude Code only"一节（hooks 行为、嵌套 CLAUDE.md、skills 调用方式）
  - 修改 `AGENTS.md` —— 新增"Commands"（check_rules、sync_skills、手动测试 hook；如实说明尚无构建/测试命令）与"How the pieces fit"（PRD 架构 → src 模块、法律文件 → PRD → 检查、规则/skills/workflows/hooks 的关系）及 Windows/OneDrive 环境注意事项
- **原因与决策**：命令与架构对 Claude 和 Codex 都有用，写在共享的 AGENTS.md（DRY）；只有 Claude 有的 hook 行为写在 CLAUDE.md 导入行之后（AC-2）。未读取用户目录下的 Codex 配置，改为提示用户用 `/import`
- **检查**：`check_rules.py` 通过；hook 已自动记录本次编辑
- **待确认**：是否用 `/import` 导入 `~/.codex/config.toml` 中的设置；支出审批金额

## 2026-10-10 · Claude Code · 更正：hooks 已在当前会话生效

- **请求人**：Terry
- **请求**：（更正上一条记录）
- **改动**：无文件改动；修改 `company-os/06-app-development/README.md` 目录结构（列出 src 模块）
- **原因与决策**：上一条"待确认"写到 `.claude/settings.json` 需 `/hooks` 或重启才生效。实际 `changelog/ai-edits.jsonl` 已开始自动记录本会话的编辑，说明 hooks 已生效（同一 matcher 下的文件大小 hook 同时生效）
- **检查**：`ai-edits.jsonl` 已有自动记录；`check_rules.py` 通过；189 个 Markdown 文件 0 断链
- **待确认**：运营规范中的支出审批金额待 Terry 决定

## 2026-10-10 · Claude Code · 新增 changelog 规范、AI 上下文文件层级、核心 15 条代码规范与文件大小自动重构

- **请求人**：Terry
- **请求**：rules 增加核心 15 条代码要求；代码超过 1000 行自动触发重构；每个层级（根目录、仓库、功能、主要模块、部门）都有 CLAUDE.md 和 README；AI 每次修改记录到 changelog
- **改动**：
  - 新增 `changelog/`（CHANGELOG.md、ai-edits.jsonl、README.md、AGENTS.md、CLAUDE.md）
  - 新增 `company-os/11-rules/changelog-rules.md`、`ai-context-rules.md`、`any-whitelist.md`、`rule_config.py`、`hook_file_size.py`、`hook_log_change.py`
  - 新增 `company-os/10-skills/refactor-large-file/`
  - 新增 `.claude/settings.json`（PostToolUse：记录变更 + 检查文件大小）、`.gitignore`
  - 新增各层 `AGENTS.md` + `CLAUDE.md`（及缺失的 `README.md`），含 `company-os/06-app-development/src/` 下按 PRD 架构划分的模块骨架说明
  - 修改 `company-os/11-rules/code-rules.md`（§0 核心 15 条、§10 文件大小、§11 性能底线、§12 类型）、`check_rules.py`（新增 SIZE / SECRET / CATCH / PLACE / ANY / CONTEXT 检查）、`company-os/10-skills/sync_skills.py`（类型标注、修正空 except、命名）、根目录 `AGENTS.md`
- **原因与决策**：
  - 文件大小阈值、文件分类只在 `rule_config.py` 定义（DRY）
  - 每层目录：`AGENTS.md` 存内容（Codex 只读此文件名），`CLAUDE.md` 只写 `@AGENTS.md` 导入同一内容，避免两份维护
  - changelog 放根目录 `changelog/`（与 `docs/` 同为全仓库共用）；逐次编辑只记元数据，不记文件内容（隐私）
  - 约 80 MB 官方 PDF 下载目录排除在 git 之外，保留在 OneDrive
- **检查**：`check_rules.py` 通过；hook 用模拟输入测试（1200 行 → exit 2、900 行 → 预警、JSON 不计入；变更日志正确写入且坏输入不阻断）；内容检查的 6 个反例全部被拦截
- **待确认**：新建的 `.claude/settings.json` 需在 Claude Code 中打开一次 `/hooks` 或重启后生效；运营规范中的支出审批金额待 Terry 决定

## 2026-10-10 · Claude Code · 公司 OS 初始搭建（回溯记录）

- **请求人**：Terry
- **请求**：为 CareKind AI 搭建符合澳洲法律的 Company OS，并逐步完善
- **改动**（按时间顺序，摘要）：
  - 建立 `company-os/` 00–05（公司基础、战略、运作节奏、法律合规、财务、HR 与团队），之后按要求把 App 开发、市场运营、用户反馈并入 06–08，新增 09 工作流、10 技能库、11 规范
  - 两个调研子任务：竞争对手调研（`07-marketing-operations/competitor-research/`）、澳洲法律与各州对比 + 59 份官方模板（`03-legal-compliance/research/`）
  - 团队：Terry（Product Owner + Tech Lead）、Ahmad、Matt、Dave（Developer）；公司注册地悉尼 NSW
  - `docs/PRD.md`：产品方向、亮点、产品逻辑与工作流；合规检查有条件通过（`03-legal-compliance/checks/2026-10-10_prd.md`）
  - 根目录 `AGENTS.md` / `CLAUDE.md`、`.editorconfig`（Tab 缩进宽度 4）
- **原因与决策**：见 `company-os/02-operating-rhythm/decision-log.md`（DR-001 至 DR-005）
- **检查**：每次结构调整后检查全部相对链接（0 断链）
- **待确认**：Terry 是否兼任 CEO 与 Privacy Officer；三位 Developer 的雇佣类型与分工；8 项待律师确认问题（见 PRD 合规检查）
