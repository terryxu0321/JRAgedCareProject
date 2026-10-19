# packages — 共享代码

本文件夹只放 git submodule（每个都是独立的公开仓库）。**文档全部在本 meta repo**，子仓库只放代码、测试与配置。

| 子仓库 | 内容 | 模块说明（需求与边界） |
|---|---|---|
| [carekind-shared](carekind-shared) | 设计 token（CSS 变量）、zod schema 与 TS 类型、API 客户端 | [design-system/](../company-os/06-app-development/design-system/DESIGN.md) |

拉取子仓库：`git submodule update --init --recursive`。仓库清单与规则见 [工程规范](../company-os/06-app-development/engineering-standards.md)"仓库清单"。
