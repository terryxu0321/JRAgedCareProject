# 班次语音 → 按老人自动整理的护理记录

> 本功能的完整需求已并入总 PRD：**[docs/PRD.md](../../../docs/PRD.md)**（唯一来源）。
>
> - 录音模式决策：PRD Part B4
> - 归属引擎与 AI 管线：PRD Part C2–C3
> - 班次与事件工作流：PRD Part D2–D3
> - 功能需求与优先级：PRD Part E
> - TGA、hazard（建议 H-09 至 H-14）、评测计划：PRD Part F
>
> 后续如需更细的技术设计（接口、数据结构、模型选型），在本文件中补充，并链接回 PRD 对应章节。

## 法律依据 Legal References

本功能的法律依据与 PRD 相同，见 [docs/PRD.md](../../../docs/PRD.md) Part F0。核心文件：

- [recording-consent.md](../../03-legal-compliance/recording-consent.md) —— 按键口述，不做环境录音
- [tga-samd-assessment.md](../../03-legal-compliance/tga-samd-assessment.md) —— documentation-only
- [privacy-program.md](../../03-legal-compliance/privacy-program.md) —— 澳洲驻留、PIA、未同意老人处理
- 合规检查：[checks/2026-10-10_prd.md](../../03-legal-compliance/checks/2026-10-10_prd.md)

技术设计细化时，按 [法律参考索引](../../11-rules/legal-reference-index.md) 补充本节。
