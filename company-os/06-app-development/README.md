# App Development — CareKind AI

> Owner: CTO ｜ 本文件夹存放产品与工程的一切：原则、临床安全、AI 治理、安全、工程规范，以及代码。

## 目录结构

```
company-os/06-app-development/
├── README.md                     ← 你在这里
├── product-principles.md         产品原则（HITL、边界）
├── product-feature-map.md        MVP 功能与解决方案地图 + best practice 汇总（2026-10-19 调研）
├── clinical-safety-framework.md  临床安全框架 + hazard log
├── ai-governance.md              AI 治理（对齐澳洲 Guidance for AI Adoption 6 项实践）
├── engineering-standards.md      技术栈、开发流程、PR 检查清单
├── security/
│   ├── information-security-policy.md   信息安全政策（Essential Eight）
│   └── vendors-and-subprocessors.md     子处理方清单（含 LLM 供应商）
├── specs/                        功能需求文档（PRD），每个功能一份
├── rnd-log/                      R&D 实验记录（R&D Tax Incentive 证据）
└── src/                          代码仓库（模块说明已就位，代码尚未开始；正式代码将迁入独立 GitHub 私有仓库）
    ├── mobile-app/               护理人员 App
    ├── api/                      网关、认证授权、审计
    ├── ai-pipeline/              转写 → 拆分 → 归属 → 分类 → 抽取 → 起草 → 护栏（7 个子模块）
    ├── review-service/           审核状态机、事件快速通道
    ├── record-store/             签字记录、时间线、保留与删除
    ├── integrations/             导出与护理系统回写
    └── admin-web/                管理后台
```

每个目录都有 `README.md`（人）、`AGENTS.md`（AI）、`CLAUDE.md`（导入 AGENTS.md）。从 [src/README.md](src/README.md) 开始。

## 不可妥协的四条

1. **护士审核后才成为记录**（HITL）—— 代码层面强制，不是 UI 建议
2. **不生成诊断/治疗/用药建议** —— 保持在 TGA 医疗器械定义之外
3. **数据与 AI 推理全部在澳洲区域**，不用客户数据训练模型
4. **生产环境不使用真实居民数据做开发/测试** —— 使用合成数据或经批准的去标识化数据

## 相关公司文档

- [合规登记册](../03-legal-compliance/compliance-register.md)
- [TGA 判定自评](../03-legal-compliance/tga-samd-assessment.md)
- [隐私计划](../03-legal-compliance/privacy-program.md)
- [路线图](../01-strategy/roadmap.md)
