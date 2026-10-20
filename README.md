# CareKind AI

> *Less paperwork. More care.* —— 面向澳洲 aged care 护士的 AI 护理记录助手 ｜ 注册地：悉尼，NSW

📘 **产品需求文档（运营、产品、开发共同参考）：[docs/PRD.md](docs/PRD.md)**

公司运营资料都在 **[company-os/](company-os/README.md)** 下：

| # | 模块 | 入口 |
|---|---|---|
| 00 | 公司基础（使命价值观、公司档案、设立清单、术语表） | [00-company](company-os/00-company/) |
| 01 | 战略（定位、OKR、路线图） | [01-strategy](company-os/01-strategy/) |
| 02 | 运作节奏（会议、决策机制、决策日志） | [02-operating-rhythm](company-os/02-operating-rhythm/) |
| 03 | 法律与合规（合规登记册、隐私、TGA、录音同意、法规调研与模板） | [03-legal-compliance](company-os/03-legal-compliance/) |
| 04 | 财务 | [04-finance](company-os/04-finance/) |
| 05 | HR 与团队（Terry、Ahmad、Matt、Dave） | [05-hr-teams](company-os/05-hr-teams/README.md) |
| 06 | App 开发 | [06-app-development](company-os/06-app-development/README.md) |
| 07 | 市场与运营 | [07-marketing-operations](company-os/07-marketing-operations/README.md) |
| 08 | 用户反馈原始记录（不经 AI 编写） | [08-feedback](company-os/08-feedback/README.md) |
| 09 | 工作流（Claude / Codex 可自动执行） | [09-workflows](company-os/09-workflows/README.md) |
| 10 | 技能库 skills | [10-skills](company-os/10-skills/README.md) |
| 11 | **规范 Rules**（公司、运营、代码、产品法律参考） | [11-rules](company-os/11-rules/README.md) |

## 代码与内容仓库（git submodule）

本仓库是 **meta repo**：所有文档（PRD、spec、规范、决策、变更记录）都在这里；代码和 blog 文章放在独立的公开仓库，以 submodule 挂在下面。clone 后运行 `git submodule update --init --recursive` 拉取。

| 位置 | 仓库 | 内容 |
|---|---|---|
| `apps/carekind-nurse-web` | [carekind-nurse-web](https://github.com/terryxu0321/carekind-nurse-web) | 护士端 Web App（React + TS） |
| `apps/carekind-admin-web` | [carekind-admin-web](https://github.com/terryxu0321/carekind-admin-web) | 机构管理端 Web App（React + TS） |
| `apps/carekind-super-admin` | [carekind-super-admin](https://github.com/terryxu0321/carekind-super-admin) | Super Admin App（React + TS） |
| `apps/carekind-marketing-site` | [carekind-marketing-site](https://github.com/terryxu0321/carekind-marketing-site) | 营销网站（HTML + CSS，英文） |
| `services/carekind-api` | [carekind-api](https://github.com/terryxu0321/carekind-api) | 后端 API + AI 管线（NestJS） |
| `packages/carekind-shared` | [carekind-shared](https://github.com/terryxu0321/carekind-shared) | 共享代码：设计 token、zod 类型、API 客户端 |
| `company-os/07-marketing-operations/carekind-blog` | [carekind-blog](https://github.com/terryxu0321/carekind-blog) | Blog 文章（每日 8:00 自动起草，审核后发布；[写作规范](company-os/07-marketing-operations/blog-editorial-guide.md)） |

规则：代码在子仓库中提交；meta repo 只更新 submodule 指针。仓库清单与规则见 [工程规范](company-os/06-app-development/engineering-standards.md)。

**变更记录**：[changelog/CHANGELOG.md](changelog/CHANGELOG.md)（AI 每次修改的记录）

**AI 助手**：每层目录都有 `README.md`（人）+ `AGENTS.md`（AI）+ `CLAUDE.md`（导入 AGENTS.md）。Claude Code 读取 [CLAUDE.md](CLAUDE.md)，Codex 读取 [AGENTS.md](AGENTS.md)（同一份规则）。在本目录打开任一工具，说"运行 workflow weekly-operating-review"即可。

**从这里开始**：[公司设立清单](company-os/00-company/setup-checklist.md) → [合规登记册](company-os/03-legal-compliance/compliance-register.md) → [OKRs](company-os/01-strategy/okrs.md)

> ⚠️ 法律合规相关内容为内部工作底稿（基于 2026-10 公开信息），不构成法律意见，签约/上线前须由澳洲执业律师审阅。
