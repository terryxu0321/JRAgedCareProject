# AI 上下文文件规范 AI Context File Rules

> Owner: Terry ｜ 适用：所有目录层级 ｜ 复审：每季度

## 为什么

AI 助手（Claude Code、Codex）在哪个目录工作，就需要那个目录的背景：它是什么、边界在哪里、有哪些禁止事项、需要哪些测试。每层都有简短、准确的说明，AI 才能少犯错、少猜测。

## 三件套

| 文件 | 读者 | 内容 |
|---|---|---|
| `README.md` | 人 | 这个目录是什么、有哪些文件、从哪里开始 |
| `AGENTS.md` | AI（Codex 只读这个文件名） | 职责、关键文件、规则与边界、相关 hazard、必须的测试 |
| `CLAUDE.md` | Claude Code | **只有一行 `@AGENTS.md`**，导入同目录的 AGENTS.md（同一份内容，DRY） |

## 规范

| # | 规范 |
|---|---|
| AC-1 | 以下每个目录**必须**有三件套：根目录、`docs/`、`changelog/`、`company-os/` 及其每个一级模块（部门）、`05-hr-teams/teams/*`（团队）、`06-app-development/src/`（代码仓库）及其每个模块和子模块（功能 / 主要模块）。`check_rules.py` 会检查（CONTEXT） |
| AC-2 | `CLAUDE.md` 只写 `@AGENTS.md`；需要只给 Claude 的说明时，写在 `@AGENTS.md` 下一行之后，并说明原因 |
| AC-3 | `AGENTS.md` 写**本目录特有**的内容；全局规则只引用（根目录 `AGENTS.md`、`11-rules/`），不复制 |
| AC-4 | 代码模块的 `AGENTS.md` 必须包含：职责、负责的功能（PRD 编号）、规则与边界、相关临床 hazard、必须覆盖的测试 |
| AC-5 | 新建目录、拆分模块（包括 `refactor-large-file` 拆出新模块）时，**同一个改动**中补齐三件套 |
| AC-6 | 目录的职责或边界变化时，同步更新其 `AGENTS.md`；过时的说明比没有说明更危险 |
| AC-7 | 说明保持简短（建议 ≤ 80 行），写事实与规则，不写营销语言；不写居民信息与密钥 |
| AC-8 | AI 进入一个目录工作前，先读该目录（及上级目录）的 `AGENTS.md`。Claude Code 读取目录中的文件时会自动加载该目录的 `CLAUDE.md`；Codex 需按根目录 `AGENTS.md` 的要求主动读取 |
