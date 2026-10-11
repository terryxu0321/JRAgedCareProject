# 产品设计与 PRD 法律参考规范 Product & PRD Legal Reference Rules

> Owner: Terry ｜ 适用：所有产品设计、PRD（`docs/PRD.md`）、功能 spec（`company-os/06-app-development/specs/`）、营销中涉及产品能力的表述 ｜ 复审：每季度

## 为什么

CareKind 的产品边界由法律决定：TGA 医疗器械定义、隐私法、各州录音法、Aged Care Act 的记录义务。凭记忆或临时搜索做产品决定，容易出错且无法追溯。所以：**产品设计必须基于本地已整理的法律文件，并在文档中写明依据。**

本地法律文件 = `company-os/03-legal-compliance/` 下的全部内容（合规工作文件、`research/` 调研总结、`research/downloads/` 官方原件）。查找入口：[法律参考索引](legal-reference-index.md)。

## 规范

| # | 规范 |
|---|---|
| L-1 | 产品设计、PRD、spec 开始前，**必须**按[法律参考索引](legal-reference-index.md)查阅与本功能相关的本地法律文件 |
| L-2 | 每份 PRD 与 spec **必须**包含 **"法律依据 Legal References"** 章节：列出查阅过的本地文件（相对链接 + 相关章节），以及每份文件对设计的具体影响 |
| L-3 | 法律依据**必须**链接到 `company-os/03-legal-compliance/` 下的文件；网络来源只能作为补充，不能替代本地文件 |
| L-4 | 本地文件没有覆盖的问题：先运行 skill `regulatory-watch` 或补充调研，把结论写入 `03-legal-compliance/`，**再**引用 —— 让本地文件始终是唯一来源 |
| L-5 | 本地文件"最近核实"日期超过 90 天，或与新信息冲突时：先运行 workflow `monthly-compliance-review` 更新，再做决定 |
| L-6 | 设计中的法律不确定点**必须**列入"需律师确认"，并在确认前标记为风险；不得在不确定的情况下按"可能没问题"推进 |
| L-7 | 每份 PRD/spec 定稿前**必须**运行 skill `compliance-check`，并链接检查结果 |
| L-8 | 改变产品边界（TGA 判定、录音模式、HITL、数据驻留、未同意老人的处理）**必须**先写 DR |
| L-9 | `research/downloads/` 中部分官方文件有许可限制（如 CC BY-NC-ND）：只能作为结构参考，**禁止**把其内容直接复制进产品或对外材料 |
| L-10 | 法律相关结论一律标注"内部工作底稿，非法律意见" |

## "法律依据"章节模板

```markdown
## 法律依据 Legal References

> 查阅日期：YYYY-MM-DD ｜ 依据 [法律参考索引](<相对路径>/company-os/11-rules/legal-reference-index.md)

| 话题 | 本地文件（章节） | 对设计的影响 |
|---|---|---|
| 录音同意 | [recording-consent.md](...)；[state-by-state-comparison.md](...) §2 | 默认按键口述；不做环境录音 |
| … | … | … |

**需律师确认**：…
**合规检查**：[checks/YYYY-MM-DD_xxx.md](...)
```

## 自动检查

```bash
python company-os/11-rules/check_rules.py
```

检查 `docs/PRD.md` 和 `company-os/06-app-development/specs/*.md`（不含 README）：
- 是否有"法律依据"章节
- 章节中是否至少有一个链接指向 `company-os/03-legal-compliance/`
- 这些链接是否都能打开

不通过时返回非零退出码，可放进 CI 或提交前检查。
