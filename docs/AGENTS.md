# AGENTS.md — docs — 产品参考文档

> AI 助手在本目录工作前必读。全局规则：根目录 `AGENTS.md` 与 `company-os/11-rules/`。人类说明：同目录 `README.md`。完成任务后按 `changelog-rules.md` 写 `changelog/CHANGELOG.md`。

## 这个目录是什么
产品需求文档（PRD）所在地，是产品范围、逻辑与工作流的**唯一来源**，供运营、产品、开发共同参考。

## 关键文件
- `PRD.md` —— 总 PRD（Part A 战略 … Part G 路线图）
- `user-personas.md` —— 10 个用户画像（买 / 用 / 受益 / 审核）；画像变化不改变 PRD 产品边界，访谈后修订须引用 raw 原话

## 在这里工作的规则
- 修改 PRD 中的产品边界（TGA、录音模式、HITL、数据驻留、未同意老人处理）前先写 DR（`company-os/02-operating-rhythm/decision-log.md`）
- PRD 必须保留"法律依据"章节并链接本地法律文件（`company-os/11-rules/product-legal-rules.md`）；改完运行 `check_rules.py`
- 功能细节写在 `company-os/06-app-development/specs/`，链接回 PRD，不复制大段内容（DRY）
- 用户问题假设须引用 `company-os/08-feedback/raw/` 中的原话（只读，逐字引用）
