# services — 后端服务

本文件夹只放 git submodule（每个都是独立的公开仓库）。**文档全部在本 meta repo**，子仓库只放代码、测试与配置。

| 子仓库 | 内容 | 模块说明（需求与边界） |
|---|---|---|
| [carekind-api](carekind-api) | NestJS API + AI 管线 worker（Node.js + TS） | [src/api/](../company-os/06-app-development/src/api/AGENTS.md) 及其他后端模块 |

拉取子仓库：`git submodule update --init --recursive`。仓库清单与规则见 [工程规范](../company-os/06-app-development/engineering-standards.md)"仓库清单"。
