# 组织与角色 Org & Roles

> Owner: Terry ｜ 复审: 每季度或团队变化时 ｜ 最近更新: 2026-10-10

## 当前团队（4 人）—— 详见 [团队名册](team-roster.md)

| 姓名 | 职位 | 团队 |
|---|---|---|
| **Terry** | Product Owner + **Tech Lead** | Leadership / Engineering |
| **Ahmad** | Developer | Engineering |
| **Matt** | Developer | Engineering |
| **Dave** | Developer | Engineering |

## 当前组织（启动期）

```
          Terry — Product Owner + Tech Lead
          (兼 CEO 职责 / Privacy Officer，待确认)
                         │
     ┌───────────────────┼───────────────────┬────────────────────┐
  Engineering        Clinical Lead (RN)    Growth（Terry 兼）     顾问团
  Lead: Terry            （待招）                              (法律/隐私/R&D/行业)
  Ahmad · Matt · Dave
```

> ⚠️ **职责集中风险**：Terry 同时承担产品、技术、（暂定）CEO 与隐私官职责，RACI 中 CEO 与 CTO 两列都落在同一人身上。制衡措施：
> - 影响 AI 输出的发布仍须 **Clinical Lead 签字**（否决权不变）—— 尽快招募 Clinical Lead
> - 生产环境变更与安全相关 PR 至少由一位 Developer（Ahmad / Matt / Dave）评审，Terry 不自我批准
> - 涉及隐私的重大决定在 DR 中征询外部隐私顾问

## 角色与职责

| 角色 | 人员 | 核心职责 | 兼任的合规角色 |
|---|---|---|---|
| **Product Owner（兼 CEO 职责）** | Terry | 产品愿景与 backlog 优先级、需求与验收标准、战略、客户与销售、招聘、财务 | 隐私官（Privacy Officer，过渡期）、数据泄露事件负责人 —— 待 Terry 确认 |
| **Tech Lead（承担 CTO 职责）** | Terry | 技术架构决策、代码评审标准、发布把关、基础设施与供应商选择 | 安全负责人、AI 问责人 |
| **Developer** | Ahmad、Matt、Dave | App、后端、AI 管线、基础设施、测试、R&D 记录；评审 Terry 的生产/安全变更 | — |
| **Clinical Lead（RN）** | `[待招]` | 临床安全、模板、评测集、客户临床沟通 | 临床安全否决权 |
| 顾问：法律 | `[待找]` | 公司/融资、健康隐私、合同 | — |
| 顾问：行业 | `[待找]` | 前 DON / 养老机构高管 | — |

> 一旦团队超过 ~5 人，Privacy Officer 应由 CEO 以外的人担任或外聘。

## RACI（关键事项）

R = 执行，A = 最终负责，C = 咨询，I = 知会

> 当前映射：CEO 列 = Terry；CTO 列 = Terry（Tech Lead）。见上方「职责集中风险」的制衡措施。

| 事项 | CEO | CTO | Clinical Lead | 律师 |
|---|---|---|---|---|
| 产品发布（影响 AI 输出） | I | A/R | C（可否决） | — |
| 新子处理方 / 新模型 | C | A/R | I | C |
| 客户合同 / DPA | A/R | C | C | C |
| 数据泄露响应 | A/R | R | C | C |
| TGA 判定 | A | R | R | C |
| 招聘 | A/R | C | C | — |
| 临床模板 | I | C | A/R | — |

## 招聘计划（草稿）

| 顺序 | 角色 | 时间 | 类型 |
|---|---|---|---|
| 1 | Clinical Lead（RN，aged care 背景） | 2026 Q4 | 兼职/顾问 → 全职 |
| 2 | AI/ML 工程师（若 Ahmad / Matt / Dave 中无人专攻 AI） | 融资后 | 全职 |
| 3 | 客户成功/实施（有护理背景优先） | 首批客户后 | 全职 |

> 已到位：Terry（Product Owner）、Ahmad / Matt / Dave（Developer）—— 原计划中的「全栈/移动工程师」岗位已覆盖。
