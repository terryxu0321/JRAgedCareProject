---
name: decision-record
description: Draft a CareKind AI Decision Record (DR) from the company template and register it in the decision log. Use for "写一个决策记录", "记录这个决定", "create a DR", "decision record", or when a Type 1 (hard-to-reverse) decision is being made.
---

# decision-record

## 输入
- 决策主题、背景、可选方案（如用户没给出，先问）
- 决策人（默认 Terry）

## 步骤
1. 读 `company-os/02-operating-rhythm/decision-making.md`，判断 Type 1（单向门）还是 Type 2（双向门）
2. 读 `company-os/02-operating-rhythm/decision-log.md`，取下一个编号 `DR-NNN`
3. 复制 `company-os/templates/decision-record.md`，填写：背景、选项对比表、推荐与理由、影响检查
4. 影响检查中涉及隐私/TGA/临床时，使用 skill `compliance-check` 并在 DR 中引用其结果
5. 状态设为 **"提议中"**（不要替人做决定）
6. 🛑 人工确认：展示草稿，等用户确认后再登记

## 输出
- 新文件：`company-os/02-operating-rhythm/decisions/DR-NNN-<kebab-标题>.md`
- 在 `decision-log.md` 表格末尾追加一行（只追加，不修改已有行）

## 禁止
- 不把状态写成"已决定"，除非用户明确说已决定
- 不删除或改写历史 DR
