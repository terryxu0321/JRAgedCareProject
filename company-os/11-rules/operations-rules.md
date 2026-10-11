# 运营规范 Operations Rules

> Owner: Terry ｜ 适用：运营、销售、客户成功、市场、财务 ｜ 复审：每季度
> 详细做法见 [07-marketing-operations](../07-marketing-operations/README.md)、[04-finance](../04-finance/finance-ops.md)

## 1. 客户与合同

| # | 规范 |
|---|---|
| O-1.1 | 接触真实居民数据之前，**必须**签好 MSA + DPA（或试点协议 + DPA），并完成客户的安全/隐私审查 |
| O-1.2 | 合同条款**必须**经律师审阅；注意 ACL 不公平合同条款（对小企业客户的标准格式合同） |
| O-1.3 | DPA **必须**写明：数据位置（澳洲）、子处理方清单、泄露通知时限、删除与返还、记录转入机构系统的约定 |
| O-1.4 | 不承诺具体上线日期或未开发的功能；路线图对外只讲方向 |

## 2. 试点与上线

| # | 规范 |
|---|---|
| O-2.1 | 试点开始前**必须**书面约定成功标准与基线测量方法 —— 见 [试点手册](../07-marketing-operations/pilot-playbook.md) |
| O-2.2 | 上线前**必须**确认：同意状态已录入、员工书面通知已发出（NSW Workplace Surveillance 要求提前 14 天）、培训已完成 |
| O-2.3 | 进入养老院现场的人员**必须**持有有效 National Police Check，并遵守机构的感染控制与着装要求 |
| O-2.4 | 现场**禁止**拍照或录下任何居民；不在走廊或公共区域讨论居民 |
| O-2.5 | 试点结束后**必须**按 DPA 处理数据（删除或继续），并书面确认 |

## 3. 支持

| # | 规范 |
|---|---|
| O-3.1 | P1（服务不可用、疑似临床安全或数据问题）1 小时内首次响应；其他级别见 [客户成功](../07-marketing-operations/customer-success.md) |
| O-3.2 | **禁止**要求客户通过邮件或聊天发送居民信息；需要查看数据时走受控的生产访问流程 |
| O-3.3 | 任何可能影响居民安全的问题，当天报告 Clinical Lead（到岗前报告 Terry） |

## 4. 市场与宣传

| # | 规范 |
|---|---|
| O-4.1 | 所有对外材料发布前**必须**过 [市场宣传合规清单](../07-marketing-operations/marketing-compliance.md)，或运行 skill `compliance-check`（类型 marketing） |
| O-4.2 | **禁止**使用暗示医疗器械用途的词：detects、predicts、diagnoses、clinical decision support、early warning |
| O-4.3 | **禁止**宣称"提升 AN-ACC 资助"或类似诱导性表述 |
| O-4.4 | 对比竞争对手时只陈述可核实的事实，或只讲自己 |
| O-4.5 | 邮件营销遵守 Spam Act：有同意、标明身份、可退订（5 个工作日内处理）；不买名单 |
| O-4.6 | 客户案例与评价**必须**有书面授权；不使用虚构评价 |

## 5. 用户反馈

| # | 规范 |
|---|---|
| O-5.1 | 用户原话**必须**人工录入 `08-feedback/raw/`，逐字、不经 AI 改写 —— 见 [08-feedback](../08-feedback/README.md) |
| O-5.2 | 录入前人工去除居民可识别信息 |
| O-5.3 | 分析写在 `07-marketing-operations/feedback-insights/`，引用原始文件名 |

## 6. 供应商与支出

| # | 规范 |
|---|---|
| O-6.1 | 任何会接触客户数据的新供应商，**必须**先完成评估并登记到 [子处理方清单](../06-app-development/security/vendors-and-subprocessors.md)；变更须按 DPA 提前通知客户 |
| O-6.2 | 支出审批：单笔 `[待定，如 A$1,000]` 以上须 Terry 书面批准；年度合同须写 DR |
| O-6.3 | 所有支出保留票据（GST 抵扣与 R&D Tax Incentive 的证据） |
| O-6.4 | 研发相关工时按活动记录（R&D Tax Incentive） |

## 7. 运营节奏与事件

| # | 规范 |
|---|---|
| O-7.1 | 按 [运作节奏](../02-operating-rhythm/operating-cadence.md) 执行周会、月度复盘、合规月检；可用 workflow 自动生成草稿 |
| O-7.2 | 事件按 [incident-response](../09-workflows/incident-response.md)：先遏制、再评估（NDB 30 天内）、通知由人决定 |
| O-7.3 | 每个事件结束后 2 周内完成无责复盘 |
