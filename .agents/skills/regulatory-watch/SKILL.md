---
name: regulatory-watch
description: Scan Australian regulator sources (OAIC, TGA, ACQSC, Department of Health, AHPRA/NMBA, NAIC, ACSC, Fair Work, NSW IPC) for changes affecting CareKind AI and propose compliance-register updates. Use for "法规监测", "合规月检", "regulatory watch", "有没有新法规", "check for regulation changes".
---

# regulatory-watch

## 输入
- 时间范围（默认：上一次 regulatory-watch 报告至今；若无则过去 30 天）

## 步骤
1. 读 `company-os/03-legal-compliance/compliance-register.md`，尤其"法规变化监测源"和所有 👀（监测中）条目
2. 读上一份 `company-os/03-legal-compliance/regulatory-watch/` 报告（如有）
3. 用网络搜索逐一检查监测源，**优先官方 .gov.au 页面**。重点：
   - TGA digital scribe 审查结果 / 新开发者指引
   - 隐私法 Tranche 2 立法进展；2026-12-10 自动化决策透明义务
   - Aged Care Rules 修订编号与内容
   - NSW 相关（公司注册在 NSW）：HRIP Act、Surveillance Devices、Workplace Surveillance
   - AHPRA/ACSQHC 关于 AI scribe 的指引更新
4. 每条变化：是什么、何时生效、来源 URL、对 CareKind 的影响、建议动作
5. 起草对合规登记册的**修改建议**（diff 形式），不要直接改登记册
6. 🛑 人工确认：Terry 审阅后决定是否更新登记册

## 输出
`company-os/03-legal-compliance/regulatory-watch/YYYY-MM.md`
顶部注明：⚠️ 内部工作底稿，非法律意见；每条结论附来源链接；无法核实的标"未核实"

## 禁止
- 不直接修改合规登记册或政策
- 不引用无来源的结论
