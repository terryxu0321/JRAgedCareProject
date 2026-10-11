# ai-pipeline — AI 管线

编排 PRD C2 的 7 个步骤：① 转写 → ② 拆分 → ③ 归属 → ④ 分类 → ⑤ 抽取 → ⑥ 起草 → ⑦ 护栏。每步是独立子模块（单一职责），本目录只负责编排、重试与版本记录。

## 功能
- 片段处理与班末批处理（性能：单段 ≤ 60 s、40 段 ≤ 5 min 为不合格线）
- 模型/提示词版本记录 A-4
- 每句草稿可溯源到来源语句 A-5

| 子模块 | 步骤 |
|---|---|
| [transcription](transcription/README.md) | ① 转写 |
| [segmentation](segmentation/README.md) | ② 拆分 |
| [attribution](attribution/README.md) | ③ 归属引擎（核心） |
| [classification](classification/README.md) | ④ 分类 |
| [extraction](extraction/README.md) | ⑤ 字段抽取 |
| [drafting](drafting/README.md) | ⑥ 起草 |
| [guardrails](guardrails/README.md) | ⑦ 护栏 |

> 代码尚未开始。AI 助手说明见 [AGENTS.md](AGENTS.md)。
