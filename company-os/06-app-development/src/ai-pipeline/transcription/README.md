# ai-pipeline/transcription — ① 转写

把原音转为文字，输出词级时间戳与置信度。通过 `TranscriptionProvider` 接口接入澳洲区域 ASR 服务，换供应商不改调用方（SOLID L/D）。

## 功能
- 名册姓名/常用名/房号热词、护理与药品术语表（T-01）
- 多语言识别与翻译 + 回译（T-02）
- 低置信词标"[请确认]"（T-03）

> 代码尚未开始。AI 助手说明见 [AGENTS.md](AGENTS.md)。
