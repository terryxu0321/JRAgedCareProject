# 路线图 Roadmap

> Owner: CEO + CTO ｜ 复审: 每月 ｜ 这是方向，不是承诺；对客户不要承诺具体日期

## 阶段 0：Foundation（2026 Q4）
- 公司设立、合规基础、合同包
- 用户研究：30 次访谈、2–3 次跟班观察（shadowing，需机构许可）
- MVP：progress note 语音 → 结构化草稿 → 护士编辑确认 → 复制/导出

## 阶段 1：Pilot（2027 Q1–Q2）
- 2 个付费试点机构，6–8 周
- 功能：progress notes、ADL、handover 摘要、多语言输入
- 度量：每份记录耗时、护士满意度、记录完整性（临床评审抽样）、编辑率
- 安全：试点期间每周临床安全复盘

## 阶段 2：Product-Market Fit（2027 H2）
- 与 1–2 个主流护理管理系统集成
- Incident 记录助手（辅助起草，**不**自动判定是否属于 SIRS 报告级别 —— 由人判断）
- Essential Eight Maturity Level 2；启动 ISO 27001
- Pre-seed / Seed 融资

## 阶段 3：Scale（2028+）
- 大型连锁提供者、Support at Home
- ISO 27001 认证
- 任何"分析/建议"类功能 → 先走 TGA 判定流程，必要时按医疗器械路径做（ARTG）

## 功能评估闸门（每个新功能都要过）

1. 是否改变 TGA 判定？（会生成诊断/治疗建议吗？）→ [TGA 自评](../03-legal-compliance/tga-samd-assessment.md)
2. 是否收集新类型的个人/健康信息？→ 更新 [隐私计划](../03-legal-compliance/privacy-program.md)
3. 是否引入新的子处理方/新 AI 模型？→ [供应商管理](../06-app-development/security/vendors-and-subprocessors.md)
4. 临床 hazard 是否已登记并缓解？→ [临床安全框架](../06-app-development/clinical-safety-framework.md)
