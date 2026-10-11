# 10 · Skills 技能库

> Owner: Terry（Tech Lead）｜ 格式：开放的 Agent Skills 标准（`SKILL.md`），**Claude Code 与 Codex 通用**

Skill = 一个可复用的单项能力（如"检查合规""写决策记录"）。Workflow（见 [09-workflows](../09-workflows/README.md)）把多个 skill 串成完整流程。

## 这里是唯一来源（source of truth）

```
company-os/10-skills/<skill-name>/SKILL.md     ← 只在这里编辑
        │  python company-os/10-skills/sync_skills.py
        ├──► .claude/skills/<skill-name>/       Claude Code 自动发现
        └──► .agents/skills/<skill-name>/       Codex 自动发现
```

**修改或新增 skill 后必须运行同步脚本**（在项目根目录）：

```bash
python company-os/10-skills/sync_skills.py
```

脚本只会覆盖/删除它自己生成的副本（带 `.synced-from-company-os` 标记），不会动你手动放进 `.claude/skills` 或 `.agents/skills` 的其他 skill。

## 技能清单

| Skill | 作用 | 会写入 |
|---|---|---|
| [run-workflow](run-workflow/SKILL.md) | 读取并逐步执行 `09-workflows/` 中的某个 workflow | 取决于 workflow |
| [compliance-check](compliance-check/SKILL.md) | 按合规登记册、TGA 边界、隐私、市场合规检查功能/文案/决策 | `03-legal-compliance/checks/` |
| [decision-record](decision-record/SKILL.md) | 按模板起草 DR 并登记到决策日志 | `02-operating-rhythm/decisions/`、`decision-log.md` |
| [spec-writer](spec-writer/SKILL.md) | 起草功能需求（含 TGA/隐私/临床检查项） | `06-app-development/specs/` |
| [weekly-update](weekly-update/SKILL.md) | 汇总本周 OKR、决策、反馈信号，生成周报草稿 | `02-operating-rhythm/weekly/` |
| [feedback-synthesis](feedback-synthesis/SKILL.md) | **只读** `08-feedback/raw/`，在别处写分析 | `07-marketing-operations/feedback-insights/` |
| [regulatory-watch](regulatory-watch/SKILL.md) | 扫描监管来源，报告法规变化，提出登记册更新建议 | `03-legal-compliance/regulatory-watch/` |
| [refactor-large-file](refactor-large-file/SKILL.md) | 代码文件超过 1000 行时重构降行数（hook / check_rules 自动触发） | 被重构的代码 |
| [onboard-team-member](onboard-team-member/SKILL.md) | 新成员档案 + 名册 + 入职清单 | `05-hr-teams/` |
| [assign-prd](assign-prd/SKILL.md) | 把 PRD / spec **整份**分配给唯一一个 Assignee（含它的全部任务）、改派、查看负责人一览 | PRD 头部的 `Assignee` 行；`adlc/tasks/` 中该 PRD 任务的负责人 / 执行者 |
| [standup](standup/SKILL.md) | 在 AI 中提交每日站会：先提醒未完成 PRD、新分配 PRD、上次 Blocker；查看全队站会汇总 | `02-operating-rhythm/standups/` |
| [work-status](work-status/SKILL.md) | 查看某位成员 / 全队的未完成工作、个人工作记录，起草提醒文字 | 不写入（只读） |

## 编写新 skill

1. 新建 `company-os/10-skills/<kebab-case-name>/SKILL.md`
2. 头部必须有：
   ```yaml
   ---
   name: <与文件夹同名>
   description: <做什么 + 什么时候用；中英文关键词都写，便于自动匹配>
   ---
   ```
3. 正文写清：输入、步骤、输出位置、**禁止事项**、何时停下来问人
4. 运行同步脚本

## 所有 skill 的共同红线

所有 skill 都必须遵守 `company-os/11-rules/` 中的规范（产品与 PRD 类 skill 尤其要遵守 `product-legal-rules.md`）。此外：

- ❌ 不创建、修改、总结或翻译 `08-feedback/raw/` 中的文件（原始反馈只能人工录入）
- ❌ 不把任何可识别居民的信息写进文档
- ❌ 不对外发送（邮件、提交表单、发布）—— 只生成草稿，人来发送
- ❌ 法律合规输出一律标注"内部工作底稿，非法律意见"
- ✅ 不确定时停下来问人，而不是猜
