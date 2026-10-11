# AI 治理 AI Governance

> Owner: CTO（问责人）｜ 复审: 每季度
> 对齐澳洲政府 **Guidance for AI Adoption**（National AI Centre / DISR，2025-10，取代 2024 年 Voluntary AI Safety Standard 的 10 条护栏）的 6 项基本实践。

## 6 项实践 × 我们的做法

| # | 实践 | 我们的做法 |
|---|---|---|
| 1 | **明确问责 Decide who is accountable** | CTO 为 AI 系统总问责人；Clinical Lead 对临床安全有否决权；AI 登记册中每个模型/用途有 Owner |
| 2 | **理解影响并规划 Understand impacts and plan accordingly** | 每个 AI 功能做影响评估（居民、护士、提供者）；关注 CALD、认知障碍居民、原住民及托雷斯海峡岛民的公平性 |
| 3 | **度量与管理风险 Measure and manage risks** | [临床安全 hazard log](clinical-safety-framework.md)；隐私 PIA；TGA 闸门 |
| 4 | **共享必要信息 Share essential information** | 对客户提供 AI 透明说明（模型用途、局限、数据流、已知错误类型）；界面标识 AI 内容；隐私政策说明 AI 使用 |
| 5 | **测试与监测 Test and monitor** | 发布前评测集回归；上线后编辑率/错误报告监测；模型/供应商变更视同重大发布 |
| 6 | **保持人类控制 Maintain human control** | HITL 强制；护士可随时弃用草稿手写；机构可关闭 AI 功能 |

## AI 登记册 AI Register

| ID | 用途 | 模型/供应商 | 处理区域 | 数据 | 是否训练 | Owner | 风险级别 |
|---|---|---|---|---|---|---|---|
| AI-01 | 语音转写 | `[待选]` | 澳洲 | 录音 | 否 | CTO | 高 |
| AI-02 | 记录结构化/起草 | `[待选，如通过澳洲区域云平台调用的 LLM]` | 澳洲 | 转写文本 | 否 | CTO | 高 |
| AI-03 | 翻译 | `[待选]` | 澳洲 | 转写文本 | 否 | CTO | 高 |

## 模型供应商选择硬性要求

- 推理在澳洲区域（核实数据是否可能经跨区域路由；需书面确认）
- 合同明确：**不保留、不用于训练**客户数据（或零数据保留）
- 有安全认证（ISO 27001 / SOC 2 / IRAP 评估为加分）
- 列入[子处理方清单](security/vendors-and-subprocessors.md)，并在 DPA 中向客户披露

## 禁止用途

- 诊断、治疗、用药建议；风险预测评分（除非走 TGA 器械路径）
- 评估/监控护士个人绩效（不作为卖点，不提供该功能）
- 自动对外提交记录或事件报告
