# 变更日志规范 Changelog Rules

> Owner: Terry ｜ 适用：所有 AI 助手（Claude Code、Codex）对本仓库的修改；人工的重要修改也建议记录 ｜ 复审：每季度

## 为什么

记录 AI 每次改了什么、为什么改，便于：追溯问题、审计（客户与监管问"这条规则什么时候、为什么改的"）、分析 AI 的工作模式与质量、为 R&D Tax Incentive 留存同期证据。

## 两层记录

| 层 | 文件 | 谁写 | 内容 |
|---|---|---|---|
| **逐次编辑**（自动） | [`changelog/ai-edits.jsonl`](../../changelog/ai-edits.jsonl) | Claude Code hook 自动追加 | 每次文件编辑一行 JSON：时间（UTC）、agent、会话 ID、工具、文件路径、操作系统用户 |
| **逐个任务**（AI 撰写） | [`changelog/CHANGELOG.md`](../../changelog/CHANGELOG.md) | 完成任务的 AI（Claude 或 Codex） | 请求、改动的文件、原因与决策、运行的检查、待确认事项 |

## 规范

| # | 规范 |
|---|---|
| CL-1 | Claude Code 的每次文件编辑由 PostToolUse hook（[`hook_log_change.py`](hook_log_change.py)）**自动**写入 `ai-edits.jsonl`，不需要也不允许手工修改该文件 |
| CL-2 | **每完成一个任务**（用户的一个请求），AI **必须**在 `CHANGELOG.md` 顶部追加一条记录，格式见下。Codex 没有 hook，这一条是它留下记录的唯一方式 |
| CL-3 | 只追加，不修改、不删除历史记录；写错了就追加一条更正 |
| CL-4 | **禁止**在任何 changelog 中写入居民可识别信息、健康信息、密钥或个人敏感信息；只写文件路径与改动性质 |
| CL-5 | 记录要可分析：使用固定字段与固定写法（agent 名：`Claude Code` / `Codex`；日期 `YYYY-MM-DD`） |
| CL-6 | 通过 Bash/脚本间接修改的文件不会被 hook 捕获 —— 必须在 CL-2 的任务记录中列出 |

## CHANGELOG.md 记录格式

```markdown
## YYYY-MM-DD · <Claude Code | Codex> · <一句话标题>

- **请求人**：<姓名>（= 当前成员 `CAREKIND_MEMBER`，见 work-log-rules WL-2）
- **请求**：<用户要求了什么，一两句>
- **改动**：
  - 新增 `path/to/file` —— <作用>
  - 修改 `path/to/file` —— <改了什么>
  - 删除 / 移动 `path` → `path`
- **原因与决策**：<为什么这样做；做了哪些假设；相关 DR>
- **检查**：<运行了什么、结果，如 `check_rules.py` 通过>
- **待确认**：<需要人决定的事项；无则写"无">
```

## 分析示例

```bash
# 每个文件被 AI 编辑的次数
python -c "import json,collections;c=collections.Counter(json.loads(l)['file'] for l in open('changelog/ai-edits.jsonl',encoding='utf-8'));print(c.most_common(20))"
```
