---
name: compliance-check
description: Check a CareKind AI feature, spec, marketing copy, contract term or decision against Australian compliance requirements (Privacy Act/APPs, NSW HRIP Act, TGA medical-device boundary, recording consent, Aged Care Act, Australian Consumer Law, Spam Act). Use for "合规检查", "compliance check", "这个功能/文案合规吗", "TGA 会不会算医疗器械", or before releasing a feature or publishing marketing.
---

# compliance-check

## 输入
- 要检查的对象：功能描述/spec 文件、营销文案、合同条款、DR 草稿（文件路径或粘贴文本）
- 对象类型：feature / marketing / contract / decision

## 参考资料（先读）
- `company-os/03-legal-compliance/compliance-register.md`
- `company-os/03-legal-compliance/tga-samd-assessment.md`（功能判定表）
- `company-os/03-legal-compliance/privacy-program.md`
- `company-os/03-legal-compliance/recording-consent.md`
- `company-os/07-marketing-operations/marketing-compliance.md`（营销类）
- `company-os/06-app-development/clinical-safety-framework.md`（功能类）
- 需要细节时：`company-os/03-legal-compliance/research/`

## 步骤
1. 判断对象涉及哪些领域：健康数据、录音、AI 输出、临床内容、对外宣称、员工监控、跨境数据
2. 逐项检查并给出 ✅ 通过 / ⚠️ 有风险 / ❌ 不通过：
   - **TGA**：是否生成护士未陈述的诊断、治疗、用药建议或风险评分？营销是否用了 detects/predicts/diagnoses 等措辞？
   - **隐私（APPs + NSW HRIP）**：新数据类型？用途变化？是否需要 PIA？数据是否留在澳洲？
   - **录音同意**：是否录到第三方对话？是否仍为按键口述默认？
   - **HITL**：AI 输出是否仍须护士审核才能成为正式记录？
   - **临床安全**：是否需要新增/更新 hazard？
   - **ACL / Spam Act**（营销）：数字宣称是否有证据？是否有退订？
   - **Aged Care**：是否可能妨碍客户的记录、SIRS、限制性措施义务？
3. 对每个 ⚠️/❌ 给出具体修改建议
4. 标出**必须由律师确认**的问题

## 输出
写入 `company-os/03-legal-compliance/checks/YYYY-MM-DD_<对象简称>.md`，结构：

```markdown
# 合规检查：<对象>
> 日期 · 检查对象路径 · ⚠️ 内部工作底稿，非法律意见

## 结论：通过 / 有条件通过 / 不通过
## 逐项结果（表格）
## 修改建议
## 需律师确认
## 需更新的文档（hazard log / PIA / 合规登记册）
```

## 禁止
- 不直接修改合规登记册或政策文件 —— 只在输出中**建议**修改
- 不给出"完全合规"的保证
