# Blog 写作规范 Blog Editorial Guide

> Owner：Terry ｜ v0.1 · 2026-10-20 ｜ 适用：`carekind-blog` 仓库（submodule：[carekind-blog/](carekind-blog/)）中的全部文章，包括每日自动起草的草稿
> 每篇文章发布前必须过 [市场合规清单](marketing-compliance.md)；语气按 [品牌与信息](brand-and-messaging.md)。

## 1. 每日自动草稿

| 项 | 规则 |
|---|---|
| 时间 | 每天悉尼时间 08:00，由 Claude 云端定时任务运行（Terry 2026-10-20）：routine "CareKind daily aged care blog draft"（[管理页面](https://claude.ai/code/routines/trig_014iJYD41XExw8fWTUMsZiby)），模型 Sonnet 5.5，只连 `carekind-blog` 仓库，不挂任何连接器（不能发邮件）。cron `0 21 * * *`（UTC）= 悉尼夏令时 08:00；**2027-04-04 夏令时结束后须改为 `0 22 * * *`**，否则会在 07:00 运行 |
| 内容 | 搜索**过去 24 小时**澳洲本地养老行业新闻（优先：ACQSC、Department of Health, Disability and Ageing、各州卫生部、OAIC、TGA、行业协会如 Ageing Australia、主流媒体），选 1 个对养老机构老板、DON 或护理团队最有用的主题，写 1 篇原创文章 |
| 语言 | 英文（澳洲拼写，如 organisation、colour） |
| 长度 | 600–900 词 |
| 位置 | `carekind-blog/drafts/YYYY-MM-DD-<slug>.md`；当天已有草稿就不再写第二篇 |
| 状态 | 草稿：front matter `status: draft-pending-review`。**仓库公开，草稿一提交即公开可见** —— 所以草稿也必须满足本规范 |
| 发布 | 🛑 Terry 按市场合规清单审核后，把文件移到 `posts/` 并改为 `status: published`；自动任务**从不**写入 `posts/` |
| 没有合适新闻 | 当天不写，不凑数；只在任务输出中说明 |

## 2. 文章格式

```markdown
---
title: "<标题>"
date: YYYY-MM-DD
status: draft-pending-review
author: CareKind AI (AI-assisted draft, pending human review)
sources:
  - title: "<原文标题>"
    publisher: "<机构或媒体>"
    url: "<链接>"
    published: YYYY-MM-DD
tags: [aged-care, ...]
---

<正文：开头一段说明发生了什么；接着说明对养老机构 / 护理团队的含义；最后列出读者可以做的事>

*This article summarises public information and is not legal or clinical advice.*
```

## 3. 内容规则

1. **原创写作，不复制新闻原文**：用自己的话总结，直接引用不超过一两句并加引号与出处；每个事实都能在 `sources` 中找到来源
2. **只写可核实的事实**；不确定的写明"reported"并给出处；不编造数字、机构、人物或引语
3. **不出现任何居民或患者可识别信息**；新闻涉及具体个人或个案时，只写机构层面的事实
4. **TGA 措辞**：不用 detects、predicts、diagnoses、monitors、clinical decision support、early warning；不暗示 CareKind 有医疗用途
5. **ACL**：不宣称 CareKind 能节省多少时间、提升多少质量（试点前没有证据）；不贬低或点名比较竞争对手
6. **少提产品**：文章以行业信息为主；结尾最多一句与 CareKind 相关的说明，按[品牌与信息](brand-and-messaging.md)措辞（"helps you write"，不说 "writes for you"）
7. **法律内容**：写明 "not legal advice"；引用法规给官方链接（legislation.gov.au、agedcarequality.gov.au 等）
8. **尊重长者**：用 "older people / residents"，不用 "the elderly"

## 4. 审核清单（Terry 发布前）

- [ ] 所有来源链接可打开，事实与来源一致
- [ ] 无复制粘贴的大段原文
- [ ] 无可识别个人信息
- [ ] [市场合规清单](marketing-compliance.md)逐项通过（ACL、TGA、隐私、AI 透明）
- [ ] 移到 `posts/`，`status: published`，`author` 改为审核人确认的署名
