---
name: feedback-synthesis
description: Analyse CareKind AI's raw user feedback (read-only) and write themes, pain points and product implications to a separate insights file. Use for "分析用户反馈", "反馈总结", "feedback synthesis", "用户之声", "Voice of Nurse".
---

# feedback-synthesis

## ⚠️ 最重要的规则
`company-os/08-feedback/raw/` 是**人工录入的原始数据**：
- ✅ 可以读取
- ❌ **不得创建、修改、重命名、删除、总结进原文件、翻译或"清理"其中任何文件**
- 分析结果**只写在** `company-os/07-marketing-operations/feedback-insights/`

## 输入
- 范围：日期区间或文件列表（默认：自上次 insights 文件以来的新反馈）

## 步骤
1. 列出 `08-feedback/raw/` 中范围内的文件（只读）
2. 按反馈人角色（RN/EN/PCW/DON…）、来源、机构代号整理
3. 归纳主题：痛点、需求、对现有功能的评价、安全/隐私担忧
4. 每个主题：频次、代表性原话（**逐字引用 + 文件名**，不改写、不翻译；如需翻译，另起一行标注"[译文，AI 生成]"）
5. 产品启示：建议进入 backlog 的事项；涉及临床安全的反馈**单独置顶**
6. 若发现 raw 文件中含可识别居民信息：**不要修改原文件**，在输出顶部提醒人工去标识化，并且不在输出中复制该信息

## 输出
`company-os/07-marketing-operations/feedback-insights/YYYY-MM-DD_synthesis.md`
