# AGENTS.md — ai-pipeline/attribution — ③ 归属引擎（核心）

> AI 助手在本目录工作前必读。全局规则：根目录 `AGENTS.md` 与 `company-os/11-rules/`。人类说明：同目录 `README.md`。完成任务后按 `changelog-rules.md` 写 `changelog/CHANGELOG.md`。

## 职责
把每个语句归属到某位老人，或送入"待归属"。这是产品最核心、风险最高的模块（PRD C3）。

## 负责的功能（PRD 编号）
- 候选生成：全名、常用名、姓、房号、读音近似；优先本班负责名单（A-01）
- 证据打分与置信度分级（A-03）
- 多老人按句归属（A-02）
- 依据与第二标识输出给审核界面（A-04）
- 上下文延续只作为中置信建议（A-05）

## 规则与边界
- **硬规则（PRD C3）**：高置信须唯一候选且两个标识一致；代词最多中置信；存在同名时仅凭姓名永远不是高置信
- **不使用**声纹、人脸等生物特征（A-06）
- 未同意 AI 处理的老人：立即丢弃该语句的转写与原音片段，只返回"请手动记录"提示
- 阈值与硬规则只在 `AttributionRules` 中定义（DRY）；依赖 `ResidentRoster` 接口（SOLID D）
- **先写测试再写代码**（CORE-05）

## 相关临床 hazard
- H-03 / H-09 错误老人（极高）
- H-10 串写

## 必须覆盖的测试
- 同名老人
- 只有代词
- 房号口误
- 无候选 / 多候选
- 未同意老人
- 跨班次负责名单
- 高置信误归属目标为 0

## 参考
- `docs/PRD.md`
- `company-os/11-rules/code-rules.md`
- `company-os/06-app-development/clinical-safety-framework.md`
