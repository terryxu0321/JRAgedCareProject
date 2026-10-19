# apps — 前端应用

本文件夹只放 git submodule（每个都是独立的公开仓库）。**文档全部在本 meta repo**，子仓库只放代码、测试与配置。

| 子仓库 | 内容 | 模块说明（需求与边界） |
|---|---|---|
| [carekind-nurse-web](carekind-nurse-web) | 护士端 Web App（React + TS） | [src/mobile-app/](../company-os/06-app-development/src/mobile-app/AGENTS.md) |
| [carekind-admin-web](carekind-admin-web) | 机构管理端 Web App（React + TS） | [src/admin-web/](../company-os/06-app-development/src/admin-web/AGENTS.md) |
| [carekind-super-admin](carekind-super-admin) | Super Admin App（React + TS） | [src/super-admin/](../company-os/06-app-development/src/super-admin/AGENTS.md) |
| [carekind-marketing-site](carekind-marketing-site) | 营销网站（HTML + CSS，英文） | [src/marketing-site/](../company-os/06-app-development/src/marketing-site/AGENTS.md) |

拉取子仓库：`git submodule update --init --recursive`。仓库清单与规则见 [工程规范](../company-os/06-app-development/engineering-standards.md)"仓库清单"。
