# AGENTS.md — apps — 前端应用

> AI 助手在本目录工作前必读。全局规则：根目录 `AGENTS.md` 与 `company-os/11-rules/`。人类说明：同目录 `README.md`。完成任务后按 `changelog-rules.md` 写 `changelog/CHANGELOG.md`。

## 这个目录是什么
存放 git submodule 的目录。每个子目录是一个独立的公开仓库（见 `README.md`）。

## 在这里工作的规则
- 子仓库**只放代码、测试与配置**，外加一个链接回 meta repo 的简短 README；需求、设计、决策、CHANGELOG 等文档一律写在本 meta repo
- 改代码前先读对应模块说明：`company-os/06-app-development/src/<模块>/AGENTS.md`
- 代码改动在子仓库中提交与推送；meta repo 只更新 submodule 指针（`git add <路径>`）
- 子仓库是公开的：不得提交密钥、真实居民或个人数据、本地绝对路径
- 代码规范：`company-os/11-rules/code-rules.md`（Tab 缩进 4、单文件不超过 1000 行、禁用 `any`、只用合成测试数据）
