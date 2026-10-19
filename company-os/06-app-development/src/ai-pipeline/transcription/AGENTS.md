# AGENTS.md — ai-pipeline/transcription — ① 转写

> AI 助手在本目录工作前必读。全局规则：根目录 `AGENTS.md` 与 `company-os/11-rules/`。人类说明：同目录 `README.md`。完成任务后按 `changelog-rules.md` 写 `changelog/CHANGELOG.md`。

## 职责
把原音转为文字，输出词级时间戳与置信度。通过 `TranscriptionProvider` 接口接入 ASR 服务，换供应商不改调用方（SOLID L/D）。MVP 供应商为 **ElevenLabs**（Terry 2026-10-19），开启零保留；⚠️ 未列澳洲驻留区域 → 只用于合成数据，处理真实居民录音前须解决（PRD C1、G4 #10）。

## 负责的功能（PRD 编号）
- 名册姓名/常用名/房号热词、护理与药品术语表（T-01）
- 多语言识别与翻译 + 回译（T-02）
- 低置信词标"[请确认]"（T-03）

## 规则与边界
- 原音只在加密存储中处理，不写入临时明文文件
- 供应商需登记到子处理方清单与 AI 登记册

## 相关临床 hazard
- H-02 转写错误（药名、剂量、数字、姓名）
- H-07 翻译失真
- H-15 翻译审核失效

## 必须覆盖的测试
- 口音与噪音样本
- 药名/数字准确率
- 提供方实现可互换（接口契约测试）

## 参考
- `docs/PRD.md`
- `company-os/11-rules/code-rules.md`
- `company-os/06-app-development/clinical-safety-framework.md`
