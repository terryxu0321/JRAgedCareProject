# CHANGELOG

> AI 与重要人工改动的任务级记录。**最新在最上面，只追加不修改。** 规范：[changelog-rules.md](../company-os/11-rules/changelog-rules.md)
> 逐次文件编辑的自动记录在 [ai-edits.jsonl](ai-edits.jsonl)（Claude Code hook 生成）。

---

## 2026-10-11 · Claude Code · DESIGN.md：设计规范唯一来源（Terry 选定的极简风格）

- **请求人**：Terry
- **请求**：把 Terry 选定的设计风格（参考 Apple 网站视觉语言的规范文本）保存为 CareKind 的 design system 与 design md，作为设计规范的唯一来源
- **改动**：
  - 新增 `company-os/06-app-development/design-system/DESIGN.md` —— YAML token（36 色、字体、间距、尺寸、圆角、层次、动效、27 个组件）+ 用法说明、Do / Don't、响应式、偏差表；新增同目录 README / AGENTS / CLAUDE
  - 修改 SPEC-003 §5.6（交付物指向 DESIGN.md）；T-0001 标记 `done`（Terry 直接选定方向）；T-0002 背景改为在 DESIGN.md 上校验与补全
  - 修改根目录 `AGENTS.md`（规则表：任何 UI 工作先读 DESIGN.md）、`06-app-development/AGENTS.md`、`07-marketing-operations/brand-and-messaging.md`（视觉一节指向 DESIGN.md）
- **原因与决策**：保留参考风格的核心（单一蓝色强调色、近黑文字、浅 / 近黑表面、胶囊按钮、无阴影无渐变），按 SPEC-003 与 WCAG 调整：次要灰字 #7a7a7a → #6e6e73（原 4.29:1 不达标）、控件边界改用 #86868b（原 1.32:1）、触控 44 → 48px、App 禁用 300 细体与 < 14px 文字、新增状态色层（草稿 / 已确认 / 错误 / 需核对 / 离线，全部 ≥ 4.5:1，浅色与夜班两套）并禁止用于临床风险；不打包 SF Pro（许可面向 Apple 平台，未经律师核实），用 system-ui + Inter 后备；不使用他人商标。token 只存在 DESIGN.md 一处（DRY），平台产物由 T-0007 生成
- **检查**：脚本计算 33 组颜色对比度；YAML 解析通过、全部 `{token}` 引用可解析（脚本放在会话临时目录，未入库）；`check_rules.py` 通过（exit 0，仅既有 ASSIGN 警告）
- **待确认**：SF Pro 许可结论待核实；图标集选型；Dave 在 T-0002 / T-0005 中按 DESIGN.md 继续

---

## 2026-10-11 · Claude Code · Design System spec（SPEC-003）、任务分配给 Dave，规则改为"整份 PRD 归一人"

- **请求人**：Terry
- **请求**：给 CareKind AI 做 design system，把任务分配好；追加：整份 PRD 与全部任务分配给一个人（Dave），并更新分配规则与 skill
- **改动**：
  - 新增 `company-os/06-app-development/specs/2026-10-design-system.md`（SPEC-003，L3）—— 原则、tokens、基础组件、安全关键组件（H-01/02/03/06/07/08/09）、文案、无障碍、法律依据、评测计划、任务表；`Assignee: Dave`（Terry 确认）
  - 新增 `company-os/03-legal-compliance/checks/2026-10-11_design-system.md` —— 有条件通过
  - 新增 `company-os/06-app-development/adlc/`、`adlc/tasks/`（各含 README / AGENTS / CLAUDE）与任务 T-0001 至 T-0009（ADLC §6.1 格式，状态 `ready`，Terry 确认）：负责人 / 执行者均为 Dave（T-0009 由 Claude Code 代执行），评审人 Terry
  - 修改 `company-os/11-rules/prd-assignment-rules.md` —— 新增 §3a"整份 PRD 归一人（含全部任务）"；§4、§7 去掉"协作者 / 按任务分人"
  - 修改 `company-os/10-skills/assign-prd/SKILL.md` —— 新增"同步任务"步骤；禁止把同一 PRD 的任务分给不同成员、禁止自审
  - 修改 ADLC spec §6.3 新增 AS-7；DR-007 补充说明；`specs/README.md`、`10-skills/README.md`
  - 通过脚本生成（hook 未捕获）：`sync_skills.py` → `.claude/skills/`、`.agents/skills/`
- **原因与决策**：SPEC-003 含 HITL 审核安全组件，按分配规范定为 L3 → Senior（Dave）。无障碍法律本地未覆盖，按 L-4 不凭记忆引用，建 T-0009 先补充本地文件。设计系统禁止临床严重程度 / 风险等级类组件（TGA）。只启用 ADLC 的任务文件部分，未实现阶段管理与 `adlc.py`。评审人 ≠ 执行者（AS-2），默认 Terry
- **检查**：`check_rules.py` 通过（exit 0；其余 3 份 PRD 未分配 WARN）；`work_items.py` 显示 9 个任务与 SPEC-003 均在 Dave 名下；skill 已同步
- **待确认**：Terry 审阅 SPEC-003 正文；H-17、H-18 待 Clinical Lead；设计工具选型；移动端技术栈 DR；Dave 一人承担 9 个任务，截止日是否需要放宽（WIP 上限 3）

---

## 2026-10-11 · Claude Code · 初始化 git 仓库

- **请求人**：Terry
- **请求**：把本项目建成 git 仓库
- **改动**：
  - `git init -b main`，首次提交 `87d312e` 包含全部 271 个现有文件（通过命令执行，hook 未捕获）
  - 新增 `.gitattributes` —— 统一 LF 换行（与 `.editorconfig` 一致，避免 Windows `core.autocrlf` 转成 CRLF）；PDF / 图片 / Office 文件按二进制处理
  - 修改 `.gitignore` —— 忽略 `.claude/worktrees/`（Claude Code 后台会话的隔离工作区）
  - 修改根目录 `AGENTS.md` 环境说明 —— 由"不是 git 仓库"改为本地 git 仓库说明
- **原因与决策**：沿用已有 `.gitignore`（排除密钥、缓存、本地 Claude 设置、`research/downloads/` 中约 80MB 的法律 PDF）；暂存前确认无 `.env`、密钥、`__pycache__`、PDF 被纳入。成为 git 仓库后，后台会话须在 worktree 中修改，因此以上三处改动在分支 `worktree-git-setup` 上提交，待合并。未添加远程仓库、未推送（对外发布须先确认）
- **检查**：`git status` / `git ls-files` 核对提交内容；`check_rules.py` 通过
- **待确认**：合并分支 `worktree-git-setup`；是否创建 GitHub 私有仓库并推送（ADLC spec 中 GitHub 为 Phase 2，需登记子处理方）；仓库位于 OneDrive，`.git` 被同步可能产生冲突 —— 建议对本文件夹选"始终保留在此设备上"，或日后迁出 OneDrive

---

## 2026-10-11 · Claude Code · 成员工作记录、待办提醒与 AI 每日站会（work-log-rules）

- **请求人**：Terry
- **请求**：成员用 AI 操作仓库时自动记录每个人的工作；记录每人分配的工作并可随时提醒未完成项，作为规则。追加：每位成员在 AI 中提交站会（写成 skill），提醒未完成 PRD、新分配 PRD、Blocker，并存档每人的站会报告。补充说明：这是学习项目，Ahmad / Matt / Dave 为假设成员
- **改动**：
  - 新增 `company-os/11-rules/work-log-rules.md`（WL-1 至 WL-8）与 `DR-008-member-work-log-and-standup.md`（提议中，附员工书面通知草稿）
  - 新增 `company-os/11-rules/work_items.py` —— 每人未完成工作（PRD Assignee + ADLC 任务）、单人工作记录（CHANGELOG 请求人 + ai-edits）、SessionStart 提醒（含"今天站会未交"）
  - 新增 `company-os/11-rules/standup.py` —— 提交前提醒（新分配 / 不再负责的 PRD、上次计划与 Blocker）、每日汇总
  - 新增 skill `company-os/10-skills/standup/`、`work-status/`；新增目录 `company-os/02-operating-rhythm/standups/`（README / AGENTS / CLAUDE）
  - 修改 `hook_log_change.py` —— 记录 `member`（来自 `CAREKIND_MEMBER`）；`.claude/settings.json` —— 新增 SessionStart hook
  - 修改 `operating-cadence.md`（站会改为在 AI 中提交）、`changelog-rules.md`（请求人 = 当前成员）、`02-operating-rhythm/AGENTS.md`、`10-skills/README.md`、`11-rules/README.md` 与 `AGENTS.md`、根目录 `AGENTS.md`（命令、规则表、学习项目说明）、`CLAUDE.md`（hook 说明）
  - 通过脚本生成（hook 未捕获）：`sync_skills.py` → `.claude/skills/`、`.agents/skills/`（12 个 skill）
- **原因与决策**：待办只读 PRD Assignee 与 ADLC 任务，不另建清单（DRY）；ADLC 任务目录尚未建立，届时自动生效。成员身份用环境变量，Terry 可扮演任一假设成员练习。为避免员工监控风险，不统计数量 / 耗时 / 提交率 / 排名，工作记录只能按单人查看；NSW Workplace Surveillance Act 通知义务在有真实员工后适用（setup-checklist §F）。提醒他人只出草稿，不对外发送
- **检查**：`check_rules.py` 通过（exit 0，仅既有 ASSIGN 警告）；`settings.json` JSON 有效；手工测试：全队待办、`--me` 未设置 / 已设置、`--log`、非名册成员报错、站会上下文（含用替身数据测试"新分配 PRD"）、站会汇总、hook 写入 `member` —— 均符合预期，测试用站会文件已删除；skill 已同步
- **待确认**：DR-008 是否确认；Terry 在自己机器上设置 `CAREKIND_MEMBER`；ADLC 任务目录何时建立；SessionStart hook 需新会话才生效

---

## 2026-10-11 · Claude Code · 更新团队成员级别与特点

- **请求人**：Terry
- **请求**：Dave 是 Senior，Ahmad 是 Junior，Matt 擅长 DevOps；Ahmad 有产品思维和审美能力 —— 更新到团队资料
- **改动**：
  - 修改 `company-os/05-hr-teams/team-roster.md` —— Ahmad 级别 Junior、Dave 级别 Senior、Matt 主方向"后端与基础设施（DevOps）"；更新日期
  - 修改 `team-members/ahmad.md`、`matt.md`、`dave.md` 的"技能"一节
  - 修改 `teams/engineering/README.md` —— 成员表改为 级别 + 特点，并指向名册为准
  - 修改 `company-os/11-rules/prd-assignment-rules.md` §3 第 2 步 —— 选人时参考个人档案"技能"
- **原因与决策**：DevOps 归入规范中的"后端与基础设施"方向；未给出的信息（Matt 级别；Ahmad、Dave 主方向；技术栈）保持 `[待填]`，不推断
- **检查**：`check_rules.py` 通过（exit 0）
- **待确认**：Matt 的级别；Ahmad 与 Dave 的主方向

---

## 2026-10-11 · Claude Code · PRD 分配规范：按难度与成员级别、方向分配

- **请求人**：Terry
- **请求**：设置 PRD 分配规则，按每个成员的特点（全栈 / 简单任务、Junior / Senior、方向）分配，并给出建议
- **改动**：
  - 新增 `company-os/11-rules/prd-assignment-rules.md` —— 成员级别（Junior/Mid/Senior/Lead）与主方向；PRD 难度 L1–L3（改变 AI 输出、HITL、签字记录、认证/数据驻留、回写、≥3 模块 → L3）；选人顺序 门槛 → 方向 → 负荷上限 → 轮换；Junior 成长任务；制衡；公平与反歧视；与 ADLC 任务级分配的分工
  - 新增 `company-os/02-operating-rhythm/decisions/DR-007-prd-assignment-by-level.md` —— 状态"提议中"，未登记到 decision-log
  - 修改 `company-os/05-hr-teams/team-roster.md` —— 新增"级别""主方向"两列（Terry = Lead，其余 `[待填]`）；待决定项改为填写级别与主方向
  - 修改 `team-members/ahmad.md`、`matt.md`、`dave.md` —— "主要方向"改为指向名册（唯一来源）
  - 修改 `company-os/10-skills/assign-prd/SKILL.md` 步骤 3 与输出 —— 按新规范判定难度、给建议、对不满足门槛的指定发出提示
  - 修改 `company-os/11-rules/README.md`、`AGENTS.md`，根目录 `AGENTS.md` 规则表 —— 登记新规范
  - 通过脚本生成（hook 未捕获）：`python company-os/10-skills/sync_skills.py` → `.claude/skills/`、`.agents/skills/`
- **原因与决策**：级别与方向只由 Terry 评定，AI 不推断、不编造（硬规则 7）；级别匹配不加自动检查，由 🛑 确认把关（KISS）；负荷上限只是规范中的数字，未写入 `rule_config.py`（无脚本使用）。与同日 ADLC spec 不冲突：ADLC §6 管任务级执行者/评审人，本规范管 PRD 级 Assignee
- **检查**：`check_rules.py` 通过（exit 0；3 条 WARN：现有 PRD 未分配）；skill 已同步，两份副本均包含新规范引用
- **待确认**：DR-007 是否确认；Ahmad / Matt / Dave 的级别与主方向；负荷上限（Junior 1、Mid 2、Senior 2、Lead 1）是否合适；反歧视条款未经律师核实

---

## 2026-10-11 · Claude Code · 新增 ADLC（AI 协作开发生命周期）spec：任务分配、PRD 阶段管理与状态记录

- **请求人**：Terry
- **请求**：为在项目中实施 ADLC 写一份 PRD —— 能分配任务、用 ADLC 管理所有 PRD、记录 PRD 状态
- **改动**：
  - 新增 `company-os/06-app-development/specs/2026-10-adlc-delivery-lifecycle.md` —— SPEC-002：S0–S8 阶段与闸门、PRD 元数据与只追加状态历史、生成式登记表 `docs/prd-registry.md`、任务文件与分配规则 AS-1 至 AS-6、AI 执行者权限、功能需求 AD-*、实施计划与验收、法律依据
  - 新增 `company-os/03-legal-compliance/checks/2026-10-11_adlc.md` —— 合规检查：有条件通过
  - 修改 `company-os/06-app-development/specs/README.md` —— "现有 specs"加入本 spec
- **原因与决策**：ADLC 是内部研发流程，放在 specs/ 按 spec-writer 走（含法律依据），不改动总 PRD；不改变产品边界，故无需 Type 1 DR。第一阶段只用仓库文件 + Python 标准库脚本（非 git 仓库、无新子处理方），GitHub 同步列为 Phase 2 并建议 Type 2 DR。复用同日新增的 `assign-prd`：Owner/Assignee 仍以 PRD 表头为唯一来源，ADLC 元数据不重复存储，S5 前必须已有 Assignee。为规避 NSW 员工监控风险，看板不做个人统计/排名/耗时。本次只写 spec，未实现脚本、未修改 `docs/PRD.md`、hazard log、隐私计划或合规登记册（只在检查中建议）
- **检查**：`check_rules.py` 通过（exit 0；仅 ASSIGN 警告：3 份 PRD 未分配 Assignee）；两个新文件相对链接 0 断链
- **待确认**：🛑 Terry 审阅 spec；本 spec 的 Assignee（`assign-prd`）；律师确认 ADLC 工作记录是否构成 NSW Workplace Surveillance Act 下的计算机监控；RDTI 记录保存要求需先用 `regulatory-watch` 补充本地文件；建议 hazard H-16 待 Clinical Lead；是否在 PRD D10 加 ADLC 链接

## 2026-10-11 · Claude Code · 新增 skill assign-prd：每个 PRD 有且仅有一个 Assignee

- **请求人**：Terry
- **请求**：新增一个 skill，把 PRD 分配给团队成员，每个 PRD 有且仅有一个负责人（Assignee）
- **改动**：
  - 新增 `company-os/10-skills/assign-prd/SKILL.md` —— 分配 / 改派 / 一览；🛑 Terry 确认后才写入；只写一行 `Assignee`
  - 修改 `company-os/11-rules/check_rules.py` —— 新增 ASSIGN 检查：多于一行、多个名字、占位或非名册成员 → 失败；未分配 → WARN
  - 新增 `company-os/02-operating-rhythm/decisions/DR-006-prd-single-assignee.md` —— 状态"提议中"，未登记到 decision-log
  - 修改 `company-os/10-skills/README.md`（技能清单）、`company-os/06-app-development/specs/README.md`（模板加 Assignee 行）、`company-os/11-rules/README.md` 与 `AGENTS.md`（检查列表加 ASSIGN）
  - 通过脚本生成（hook 未捕获）：`python company-os/10-skills/sync_skills.py` → `.claude/skills/assign-prd/`、`.agents/skills/assign-prd/`
- **原因与决策**：PRD 范围 = `docs/PRD.md` + `specs/*.md`（不含 README）。Assignee 写在 PRD 头部作为唯一来源，不另建登记表（DRY）；Assignee 与 Owner（产品决策人）区分。未分配暂为 WARN，避免在负责人确定前阻塞检查；没有替现有 PRD 选择负责人
- **检查**：`check_rules.py` 通过（2 条 WARN：两份现有 PRD 未分配）；临时文件测试 11 种 Assignee 写法，结果均符合预期；skill 已同步
- **待确认**：DR-006 是否确认并登记；`docs/PRD.md` 与 `specs/2026-10-shift-voice-to-resident-records.md` 分别由谁负责；确认后是否把"未分配"升级为失败

---

## 2026-10-10 · Claude Code · /init：改进根目录 CLAUDE.md 与 AGENTS.md

- **请求人**：Terry
- **请求**：运行 `/init`，为以后的 Claude Code 会话生成/改进 CLAUDE.md
- **改动**：
  - 修改 `CLAUDE.md` —— 加入 `/init` 标准开头；保留 `@AGENTS.md` 导入；新增"Claude Code only"一节（hooks 行为、嵌套 CLAUDE.md、skills 调用方式）
  - 修改 `AGENTS.md` —— 新增"Commands"（check_rules、sync_skills、手动测试 hook；如实说明尚无构建/测试命令）与"How the pieces fit"（PRD 架构 → src 模块、法律文件 → PRD → 检查、规则/skills/workflows/hooks 的关系）及 Windows/OneDrive 环境注意事项
- **原因与决策**：命令与架构对 Claude 和 Codex 都有用，写在共享的 AGENTS.md（DRY）；只有 Claude 有的 hook 行为写在 CLAUDE.md 导入行之后（AC-2）。未读取用户目录下的 Codex 配置，改为提示用户用 `/import`
- **检查**：`check_rules.py` 通过；hook 已自动记录本次编辑
- **待确认**：是否用 `/import` 导入 `~/.codex/config.toml` 中的设置；支出审批金额

## 2026-10-10 · Claude Code · 更正：hooks 已在当前会话生效

- **请求人**：Terry
- **请求**：（更正上一条记录）
- **改动**：无文件改动；修改 `company-os/06-app-development/README.md` 目录结构（列出 src 模块）
- **原因与决策**：上一条"待确认"写到 `.claude/settings.json` 需 `/hooks` 或重启才生效。实际 `changelog/ai-edits.jsonl` 已开始自动记录本会话的编辑，说明 hooks 已生效（同一 matcher 下的文件大小 hook 同时生效）
- **检查**：`ai-edits.jsonl` 已有自动记录；`check_rules.py` 通过；189 个 Markdown 文件 0 断链
- **待确认**：运营规范中的支出审批金额待 Terry 决定

## 2026-10-10 · Claude Code · 新增 changelog 规范、AI 上下文文件层级、核心 15 条代码规范与文件大小自动重构

- **请求人**：Terry
- **请求**：rules 增加核心 15 条代码要求；代码超过 1000 行自动触发重构；每个层级（根目录、仓库、功能、主要模块、部门）都有 CLAUDE.md 和 README；AI 每次修改记录到 changelog
- **改动**：
  - 新增 `changelog/`（CHANGELOG.md、ai-edits.jsonl、README.md、AGENTS.md、CLAUDE.md）
  - 新增 `company-os/11-rules/changelog-rules.md`、`ai-context-rules.md`、`any-whitelist.md`、`rule_config.py`、`hook_file_size.py`、`hook_log_change.py`
  - 新增 `company-os/10-skills/refactor-large-file/`
  - 新增 `.claude/settings.json`（PostToolUse：记录变更 + 检查文件大小）、`.gitignore`
  - 新增各层 `AGENTS.md` + `CLAUDE.md`（及缺失的 `README.md`），含 `company-os/06-app-development/src/` 下按 PRD 架构划分的模块骨架说明
  - 修改 `company-os/11-rules/code-rules.md`（§0 核心 15 条、§10 文件大小、§11 性能底线、§12 类型）、`check_rules.py`（新增 SIZE / SECRET / CATCH / PLACE / ANY / CONTEXT 检查）、`company-os/10-skills/sync_skills.py`（类型标注、修正空 except、命名）、根目录 `AGENTS.md`
- **原因与决策**：
  - 文件大小阈值、文件分类只在 `rule_config.py` 定义（DRY）
  - 每层目录：`AGENTS.md` 存内容（Codex 只读此文件名），`CLAUDE.md` 只写 `@AGENTS.md` 导入同一内容，避免两份维护
  - changelog 放根目录 `changelog/`（与 `docs/` 同为全仓库共用）；逐次编辑只记元数据，不记文件内容（隐私）
  - 约 80 MB 官方 PDF 下载目录排除在 git 之外，保留在 OneDrive
- **检查**：`check_rules.py` 通过；hook 用模拟输入测试（1200 行 → exit 2、900 行 → 预警、JSON 不计入；变更日志正确写入且坏输入不阻断）；内容检查的 6 个反例全部被拦截
- **待确认**：新建的 `.claude/settings.json` 需在 Claude Code 中打开一次 `/hooks` 或重启后生效；运营规范中的支出审批金额待 Terry 决定

## 2026-10-10 · Claude Code · 公司 OS 初始搭建（回溯记录）

- **请求人**：Terry
- **请求**：为 CareKind AI 搭建符合澳洲法律的 Company OS，并逐步完善
- **改动**（按时间顺序，摘要）：
  - 建立 `company-os/` 00–05（公司基础、战略、运作节奏、法律合规、财务、HR 与团队），之后按要求把 App 开发、市场运营、用户反馈并入 06–08，新增 09 工作流、10 技能库、11 规范
  - 两个调研子任务：竞争对手调研（`07-marketing-operations/competitor-research/`）、澳洲法律与各州对比 + 59 份官方模板（`03-legal-compliance/research/`）
  - 团队：Terry（Product Owner + Tech Lead）、Ahmad、Matt、Dave（Developer）；公司注册地悉尼 NSW
  - `docs/PRD.md`：产品方向、亮点、产品逻辑与工作流；合规检查有条件通过（`03-legal-compliance/checks/2026-10-10_prd.md`）
  - 根目录 `AGENTS.md` / `CLAUDE.md`、`.editorconfig`（Tab 缩进宽度 4）
- **原因与决策**：见 `company-os/02-operating-rhythm/decision-log.md`（DR-001 至 DR-005）
- **检查**：每次结构调整后检查全部相对链接（0 断链）
- **待确认**：Terry 是否兼任 CEO 与 Privacy Officer；三位 Developer 的雇佣类型与分工；8 项待律师确认问题（见 PRD 合规检查）
