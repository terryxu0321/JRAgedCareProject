---
name: weekly-update
description: Compile CareKind AI's weekly update draft from OKRs, the decision log, recent file changes and feedback insights. Use for "写周报", "本周总结", "weekly update", "周五汇报".
---

# weekly-update

## 输入
- 周期（默认：本周一至今天）
- 可选：用户口述的本周进展

## 步骤
1. 读 `company-os/01-strategy/okrs.md` —— 当前季度 KR 与信心值
2. 读 `company-os/02-operating-rhythm/decision-log.md` —— 本周新增/变更的 DR
3. 列出本周在 `company-os/` 中修改过的文件（按修改时间），归纳进展
4. 读本周的 `07-marketing-operations/feedback-insights/`（若有）；如需原话，可**只读** `08-feedback/raw/` 并**逐字**引用一句，注明文件名
5. 按 `company-os/templates/weekly-update.md` 填写
6. 无法从文件得知的内容（指标数字、信心值变化）**标为"待填"**，不要编造

## 输出
`company-os/02-operating-rhythm/weekly/YYYY-Www.md`（例：`2026-W41.md`）

## 禁止
- 不编造指标、访谈数、客户名
- 不包含任何可识别居民信息
