# AGENTS.md — 11-rules — 规范

> AI 助手在本目录工作前必读。全局规则：根目录 `AGENTS.md` 与 `company-os/11-rules/`。人类说明：同目录 `README.md`。完成任务后按 `changelog-rules.md` 写 `changelog/CHANGELOG.md`。

## 这个目录是什么
公司、运营、代码、产品法律参考、AI 上下文文件、变更日志规范，以及自动检查脚本与 hooks。

## 关键文件
- `code-rules.md` —— 核心 15 条等
- `product-legal-rules.md` + `legal-reference-index.md`
- `prd-assignment-rules.md` —— PRD 按难度与级别/方向分配
- `ai-context-rules.md`
- `changelog-rules.md`
- `work-log-rules.md` —— 成员工作记录、待办提醒、每日站会
- `check_rules.py`、`rule_config.py`、`hook_*.py`、`work_items.py`、`standup.py`
- `any-whitelist.md`

## 在这里工作的规则
- 阈值与文件分类只在 `rule_config.py` 定义（DRY）；修改阈值须写 DR
- 新增"必须/禁止"类条款须写 DR；改完运行 `check_rules.py`
- 本目录的 Python 脚本同样遵守代码规范（Tab、类型标注、无空 except）
