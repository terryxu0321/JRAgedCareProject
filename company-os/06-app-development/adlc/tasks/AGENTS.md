# AGENTS.md — adlc/tasks — 任务文件

> AI 助手在本目录工作前必读。全局规则：根目录 `AGENTS.md` 与 `company-os/11-rules/`。人类说明：同目录 `README.md`。完成任务后按 `changelog-rules.md` 写 `changelog/CHANGELOG.md`。

## 这个目录是什么
一任务一文件，格式见 ADLC spec §6.1；`work_items.py` 读取这里给每位成员提醒未完成工作。

## 关键文件
- `README.md` —— 字段与当前任务一览
- `T-*.md` —— 任务

## 在这里工作的规则
- 负责人与评审人必须是人；评审人 ≠ 执行者；safety 任务评审人 ≠ 负责人（AS-1 至 AS-3）
- AI 只执行 `executor` 为自己、状态 `ready` / `in-progress` 的任务；执行记录只追加
- `backlog → ready` 及更改执行者 / 评审人须 Terry 确认
- 不写居民信息、健康信息、密钥（AS-6）
