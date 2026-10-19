# Facility Go-Live Checklist — 模板

> **内部模板，非法律意见。** 复制到试点文件夹后逐项勾选，不改本模板；不写真实居民信息。

| 项目 | 说明 |
|---|---|
| 用途 | 一家机构从签约到上线的一次性清单，对应 PRD D1；全部 🛑 项完成前不得上线 |
| 何时使用 | 签约后至上线日；每个新院区重复一次 |
| 谁填写 | CareKind 上线负责人 + 机构管理员 / DON（各自签名确认） |
| 保存年限 | 随客户合同档案保存（期限按合同【需律师确认】） |
| 法规依据 | PRD D1、D8、C7（[docs/PRD.md](../../../docs/PRD.md)）；APP 8、APP 11；NSW HRIP Act；NSW Workplace Surveillance Act 2005；见 [privacy-program.md](../../03-legal-compliance/privacy-program.md)、[recording-consent.md](../../03-legal-compliance/recording-consent.md)、[compliance-register.md](../../03-legal-compliance/compliance-register.md)、[tga-samd-assessment.md](../../03-legal-compliance/tga-samd-assessment.md) |

| Field | Entry |
|---|---|
| Facility | 【机构代号】 【州】 |
| CareKind go-live lead | 【姓名】 |
| Facility admin / DON | 【职位】 |
| Planned go-live date | 【日期】 |

## 1. Contract & privacy

- [ ] 🛑 MSA signed（【日期】）
- [ ] 🛑 DPA signed：数据与 AI 推理在澳洲、不用客户数据训练、保留期、泄露通知、分包商清单
- [ ] 🛑 Trust pack provided：安全概述、PIA 摘要、TGA intended purpose 声明、hazard 摘要
- [ ] 机构安全 / 隐私审查问卷已答复（【日期】）
- [ ] 机构隐私联系人与 CareKind 泄露联系人已互换（[data-breach-response-plan.md](../../03-legal-compliance/data-breach-response-plan.md)）

## 2. Admin configuration

- [ ] SSO / users and roles（PCW、EN、RN、DON、Admin）按 PRD C6 配置
- [ ] Resident roster imported（姓名、常用名、房号、可选照片）——只在 CareKind 系统内，不进本清单
- [ ] Templates and review rules confirmed by DON（如 PCW 记录是否需 RN 复核）
- [ ] Retention settings：原音签字后 ≤ 【___】 天删除；草稿弃用后删除
- [ ] 🛑 Record transfer agreement：签字后【___】天内转入机构系统；负责人【职位】；"已转入"确认流程已演示

## 3. Consent & notices

- [ ] 🛑 Resident notices given and consent collected（[resident-ai-consent-notice.md](resident-ai-consent-notice.md)，律师确认版本：【版本号】）
- [ ] 🛑 Consent status entered for every resident；未同意居民的手动记录流程已告知员工
- [ ] Withdrawal process tested（撤回立即生效）
- [ ] 🛑 Staff written notice issued（[staff-workplace-surveillance-notice.md](staff-workplace-surveillance-notice.md)）；NSW：发出日【日期】，最早上线日 = 发出日 + 14 天 → 【日期】
- [ ] 其他州监控 / 监听法要求已由律师确认（【州】：【结论】）

## 4. Training

- [ ] 🛑 Role-based training completed（PCW / EN / RN / DON；出席名单在机构系统）
- [ ] 培训内容含：审核签字责任、AI 局限（可能遗漏或出错）、离开房间后口述、事件快速通道、"报告 AI 错误"
- [ ] Champion nominated：【职位】
- [ ] Baseline documentation time measured（方法：【】；不做个人排名）

## 5. Go-live decision

| Check | Owner | Done |
|---|---|---|
| 所有 🛑 项完成 | CareKind go-live lead | ☐ |
| 机构同意上线 | DON | ☐ |
| 首周支持安排（联系人、响应时间） | CareKind | ☐ |
| 首周复盘会日期 | 双方 | 【日期】 |

Sign-off：CareKind 【姓名】 【日期】　Facility 【职位】 【日期】
