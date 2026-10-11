---
name: refactor-large-file
description: Refactor a CareKind code file that exceeds the 1000-line limit (code-rules.md SIZE-1) so it gets shorter and clearer without changing behaviour. Triggered automatically by the file-size hook or check_rules.py; also use for "重构", "refactor", "文件太长", "代码超过1000行", "拆分文件".
---

# refactor-large-file

降低代码行数的**正确方式**是拆分职责、去除重复和死代码，而不是把代码挤在更少的行里。

## 输入
- 超限的文件路径（来自 hook 提示或 `check_rules.py` 的 `SIZE` 输出）

## 先读
- `company-os/11-rules/code-rules.md`（KISS > DRY > 过早抽象；SOLID；§4 格式；§10 文件大小）
- 该文件的测试；没有测试时先补"特征测试"（characterization tests）锁定现有行为

## 步骤
1. **确认安全网**：运行现有测试，全部通过才开始；没有测试 → 先为该文件的公开行为补测试
2. **诊断**（先写计划，再动手）：
   - 文件承担了哪几种职责？（SOLID 的 S —— 每种职责是拆分候选）
   - 有哪些重复的知识？（DRY —— 第三次出现才抽取）
   - 有哪些死代码、未使用的导入、注释掉的代码、过时的兼容分支？
   - 有哪些可以用语言/框架自带能力替代的手写逻辑？（KISS）
3. **按优先级重构**，每一步后都跑测试：
   1. 删除死代码与未使用的内容
   2. 按职责拆分成新模块/文件（命名说清意图），原文件只保留其核心职责
   3. 抽取重复的知识到唯一位置
   4. 简化过度复杂的逻辑（提前返回、减少嵌套）
4. **保持行为不变**：不改公开接口签名（除非同时更新所有调用方）；不顺带加新功能或修无关的 bug —— 重构单独成一个 PR
5. **验证**：
   - 全部测试通过
   - 每个文件 ≤ 1000 行，目标 ≤ 500 行
   - `python company-os/11-rules/check_rules.py` 通过（包括 Tab 缩进格式）
6. **报告**：原文件行数 → 各新文件行数；拆分依据；删除了什么；测试结果

## 禁止
- ❌ 为凑行数把多条语句写在一行、删除必要的空行或注释、缩短变量名、压缩格式
- ❌ 为凑行数引入不必要的抽象层或接口（违反 KISS）
- ❌ 改变行为、删除测试、跳过失败的测试
- ❌ 在 AI 管线、归属、护栏、状态机代码中改变逻辑而不跑临床评测集（code-rules.md A-2）
- ❌ 改动生产与安全相关代码后自我批准（需 Terry 以外的人评审）
