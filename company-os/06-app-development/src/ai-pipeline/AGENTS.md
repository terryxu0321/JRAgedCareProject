# AGENTS.md — ai-pipeline — AI 管线

> AI 助手在本目录工作前必读。全局规则：根目录 `AGENTS.md` 与 `company-os/11-rules/`。人类说明：同目录 `README.md`。完成任务后按 `changelog-rules.md` 写 `changelog/CHANGELOG.md`。

## 职责
编排 PRD C2 的 7 个步骤：① 转写 → ② 拆分 → ③ 归属 → ④ 分类 → ⑤ 抽取 → ⑥ 起草 → ⑦ 护栏。每步是独立子模块（单一职责），本目录只负责编排、重试与版本记录。

## 负责的功能（PRD 编号）
- 片段处理与班末批处理（性能：单段 ≤ 60 s、40 段 ≤ 5 min 为不合格线）
- 模型/提示词版本记录 A-4
- 每句草稿可溯源到来源语句 A-5

## 规则与边界
- 所有外部 AI 调用使用澳洲区域端点、零数据保留、不训练（P-5、DR-003）
- **禁止**生成诊断、治疗/用药建议、风险评分（F-6、TGA）
- 不确定就交给人：返回"待人工处理"，不猜测（F-1）
- 提示词即代码，变更视同发布（A-1）；影响输出的变更须跑临床评测集 + Clinical Lead 签字（A-2）
- ASR / LLM 的输出是外部边界，必须经护栏校验（CORE-07、F-3）

## 相关临床 hazard
- H-01 幻觉
- H-02 转写错误
- H-04 遗漏关键信息
- H-05 临床建议
- H-07 翻译失真

## 必须覆盖的测试
- 评测集回归（`company-os/06-app-development/clinical-safety-framework.md` §4）

## 参考
- `docs/PRD.md`
- `company-os/11-rules/code-rules.md`
- `company-os/06-app-development/clinical-safety-framework.md`
