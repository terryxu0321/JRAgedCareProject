# 代码规范 Code Rules

> Owner: Terry（Tech Lead）｜ 适用：所有代码（App、后端、AI 管线、脚本、基础设施即代码）｜ 复审：每季度
> 技术栈、环境与开发流程见 [工程规范](../06-app-development/engineering-standards.md)；本文件是代码层面的**硬性规范**。

三条设计原则的优先级：**KISS > DRY > 过早的抽象**。先写简单、正确、可读的代码；重复出现第三次再抽象；SOLID 用来划分边界，不是用来堆层次。

---

## 0. 核心 15 条（所有代码必须遵守）

> 🤖 = `check_rules.py` 自动检查；其余在代码评审中检查。

| # | 规范 | 怎么做（CareKind） | 详见 |
|---|---|---|---|
| **CORE-01** | **单一职责 Single Responsibility** | 一个函数/模块只做一件事；改一个原因只影响一处。AI 管线每一步是独立模块 | §3 S、K-2 |
| **CORE-02** | **清晰命名 Clear Naming** | 变量/函数名说人话：`residentCandidates` 而不是 `a` / `tmp` / `data2` / `res`；布尔值用 `is/has/should` 开头；函数用动词开头 | K-5 |
| **CORE-03** | **不硬编码密钥 No Hard-Coded Secrets** 🤖 | API Key、密码、token 一律通过环境变量读取：本地开发放 `.env`（已在 `.gitignore` 中，**永不提交**），提交 `.env.example` 只列变量名不含值；测试/生产环境用云密钥管理服务注入。密钥一旦进过 git，视为泄露，立即轮换 | P-2 |
| **CORE-04** | **先写注释 Comments First** | 复杂逻辑**动手前**先写一句"为什么"（业务原因、法规依据、为什么不用更简单的办法），再写代码。注释解释"为什么"，不复述代码"做了什么"。法规相关逻辑注明出处，如 `// 只提示不判定：TGA 边界，PRD C5` | — |
| **CORE-05** | **测试驱动 Test-Driven** | 关键逻辑（归属、护栏、状态机、权限、事件快速通道、保留与删除）**先写测试**；其他逻辑至少写完立刻补测试，同一个 PR 内完成 | §8 |
| **CORE-06** | **显式错误处理 Explicit Error Handling** 🤖 | 错误要么处理（有明确的恢复动作），要么带上下文抛出；**禁止空 catch / `except: pass` 静默吞掉**。用户输入（录音、草稿）在任何错误路径上都不能丢（F-2）。错误信息不含健康信息明文（P-1） | F-2 |
| **CORE-07** | **在边界校验 Validate at Boundaries** | 只在系统边界做校验：用户输入、API 请求、外部服务响应（**ASR / LLM 的输出也是外部边界** → 护栏校验 F-3）、文件与集成数据。校验后用类型表达"已校验"，内部代码互相信任，**不层层判空** | F-3 |
| **CORE-08** | **默认安全 Secure by Default** | 默认最小权限、默认拒绝、默认最严设置（新角色无权限、新存储桶私有、新端点需认证、CORS 白名单、新功能对未同意老人默认关闭）。要放开必须在代码/配置中**显式声明并写明原因** | §6 |
| **CORE-09** | **不交付占位与假数据 No Placeholder / Fake Data** 🤖 | 合并的代码中禁止 `TODO` / `FIXME` / `XXX` / Lorem ipsum / 编造的数字。未完成的工作记入任务跟踪，不留在代码里。没有真实数据就**明确说明**（显示"暂无数据"），不编造。**允许**：测试中明确标注的合成数据（P-3），这是规定而非假数据 | — |
| **CORE-10** | **性能底线 Performance Boundaries** | 不合格线写死在下方 §11 性能底线表中，CI/监控按此告警；超过即为缺陷 | §11 |
| **CORE-11** | **最少依赖 Minimal Dependencies** | 标准库或已有依赖能解决就不装新包。装之前在 PR 中回答：真的需要吗？标准库为什么不够？维护状况、许可证、安全记录？ | K-4 |
| **CORE-12** | **YAGNI** | 不为"未来可能用到"写代码、参数、配置项或抽象层；只写现在要用的 | K-1 |
| **CORE-13** | **为读者写代码 Code for the Reader** | 代码首先给人看。可读性优先于炫技与微小的性能收益（除非触及 §11 性能底线） | K-6 |
| **CORE-14** | **导出必须写明类型 Explicit Types on Exports** | 每个导出的函数、变量、类成员写明参数与返回类型，不依赖隐式推断。TypeScript：ESLint `@typescript-eslint/explicit-module-boundary-types` 设为 error；Python：公开函数完整类型标注，Ruff `ANN` 规则 + mypy/pyright 严格模式 | §12 |
| **CORE-15** | **禁用 `any`，除非在白名单** 🤖 | TypeScript 禁用 `any`（ESLint `no-explicit-any` 设为 error），Python 禁用 `Any`。确实需要（如无类型的第三方库）时：先登记到 [any-whitelist.md](any-whitelist.md) 并获批，再在该行注释 `any-allowed: <白名单编号>`；优先用 `unknown` + 边界校验替代 | §12 |

---

## 1. KISS —— 保持简单

| # | 规范 |
|---|---|
| K-1 | 选**最简单的、能正确解决当前需求**的方案。不为假想的未来需求写代码（YAGNI） |
| K-2 | 函数只做一件事；一般 ≤ 40 行。超过时先考虑拆分，而不是加注释解释 |
| K-3 | 嵌套 ≤ 3 层；用提前返回（guard clause）代替深层 if/else |
| K-4 | 优先使用语言与框架自带的能力，而不是引入新依赖。新依赖须在 PR 中说明理由，并登记许可证 |
| K-5 | 命名说清意图：`attributeUtteranceToResident()` 好于 `process()`；不用缩写（`res` 可能是 resident 也可能是 response） |
| K-6 | 不写"聪明"的代码。一段代码需要讲解 5 分钟才能看懂，就是太复杂了 |

## 2. DRY —— 不重复知识

DRY 针对的是**知识**的重复，不是长得像的代码。

| # | 规范 |
|---|---|
| D-1 | 每条业务规则**只在一个地方定义**。例如：归属置信度阈值、记录类型清单、禁止内容规则、保留天数 → 集中在配置或一个模块中，其他地方引用 |
| D-2 | **三次法则**：同样的逻辑出现第三次时再抽取。两处相似但会各自演变的代码，宁可保留重复 |
| D-3 | 类型与校验只定义一次：API 契约（如 OpenAPI / 共享 schema）生成前后端类型，不手写两份 |
| D-4 | 常量不硬编码在多处；魔法数字（如 `0.85`、`7`）必须是有名字的常量，并注明来源（如"保留 7 天：PRD C7"） |
| D-5 | 文档同理：产品需求只写在 `docs/PRD.md`，代码注释链接到它，不复制大段需求 |

## 3. SOLID —— 划清边界

| 原则 | 规范 | 在 CareKind 中的例子 |
|---|---|---|
| **S** 单一职责 | 一个模块只有一个变化的理由 | 转写、拆分、归属、分类、起草、校验是 AI 管线中**各自独立的模块**（PRD C2）；归属逻辑变化不应修改起草代码 |
| **O** 开闭 | 增加新类型时扩展，而不是修改核心流程 | 新增记录类型（如限制性措施）= 新增一个模板与抽取器并注册，不改管线主流程 |
| **L** 里氏替换 | 实现同一接口的组件可以互换而不破坏调用方 | 任何 `TranscriptionProvider` 实现都必须返回相同结构（文本 + 词级时间戳 + 置信度）；换供应商不改调用方 |
| **I** 接口隔离 | 接口小而专一，调用方不依赖用不到的方法 | 审核服务只依赖 `DraftReader` / `DraftSigner`，而不是整个记录存储接口 |
| **D** 依赖倒置 | 业务逻辑依赖抽象，外部服务（ASR、LLM、存储、护理系统集成）通过接口注入 | 归属引擎依赖 `ResidentRoster` 接口，测试时注入合成名册，生产时注入真实实现 |

```ts
// ✅ 依赖抽象：归属引擎不知道名册来自哪里，也不知道用了哪个 ASR
interface ResidentRoster {
	findCandidates(mention: string, facilityId: string): ResidentCandidate[];
}

class AttributionEngine {
	constructor(private readonly roster: ResidentRoster, private readonly rules: AttributionRules) {}

	attribute(utterance: Utterance, shift: ShiftSession): Attribution {
		const candidates = this.roster.findCandidates(utterance.text, shift.facilityId);
		return this.rules.decide(candidates, shift.assignedResidentIds); // 阈值与硬规则只在 AttributionRules 中定义（DRY）
	}
}
```

**不要过度设计**：只有一个实现且没有替换需求的地方，不需要接口。为外部服务（ASR、LLM、存储、集成）和需要在测试中替换的依赖建接口即可。

## 4. 格式 Formatting

| # | 规范 |
|---|---|
| FMT-1 | **缩进一律使用 Tab，显示宽度 4**（所有语言：TypeScript/JavaScript、Python、Swift、Kotlin、SQL、Shell、JSON 等） |
| FMT-2 | **唯一例外：YAML**（`.yml` / `.yaml`，含 CI 配置、Docker Compose、Kubernetes）—— YAML 语法禁止用 Tab 缩进，使用 2 个空格 |
| FMT-3 | 根目录 [`.editorconfig`](../../.editorconfig) 是格式的唯一来源；编辑器须启用 EditorConfig 支持，不得用个人设置覆盖 |
| FMT-4 | 格式化工具与 `.editorconfig` 保持一致：Prettier `useTabs: true, tabWidth: 4`；Ruff `indent-style = "tab"`；其他语言同理。格式化在 CI 中检查，不通过不能合并 |
| FMT-5 | 对齐（如多行参数的竖直对齐）不靠空格凑；需要对齐时换行并多缩进一级 |
| FMT-6 | 行尾 LF；文件末尾保留一个换行；去除行尾空白；UTF-8 编码 |

## 5. 安全失败（Fail safe）—— 临床安全相关

| # | 规范 |
|---|---|
| F-1 | **不确定就不做**：归属、分类、抽取不确定时，返回"待人工处理"，**禁止**猜测或用默认值填充（PRD C3） |
| F-2 | 绝不静默丢失用户输入。任何失败都要保留原始输入并给出明确提示 |
| F-3 | AI 输出必须经过护栏校验（忠实性、禁止内容）才能显示为草稿；校验失败的句子不进入草稿 |
| F-4 | 签字记录只追加、不覆盖；更正是新版本 |
| F-5 | **禁止**任何"自动提交"代码路径；签字必须有人的操作 |
| F-6 | **禁止**实现诊断、治疗/用药建议、风险评分或临床预警（TGA 边界）。需求中出现这类功能时停下来，走 new-feature-gate |

## 6. 安全与隐私

| # | 规范 |
|---|---|
| P-1 | 日志、错误监控、分析事件中**禁止**出现健康信息明文与居民标识；用内部 ID |
| P-2 | 密钥、令牌、凭据**禁止**进入代码与提交历史：本地用 `.env`（不提交），云端用密钥管理服务（见 CORE-03） |
| P-3 | 开发与测试**只用合成数据**；禁止把生产数据复制到其他环境 |
| P-4 | 所有健康数据：传输 TLS 1.2+，静态加密；设备端缓存加密 |
| P-5 | 所有外部服务调用（ASR、LLM）**必须**使用澳洲区域端点，并在配置中显式声明区域 |
| P-6 | 访问控制在服务端执行，不依赖前端隐藏 |
| P-7 | 每个数据写入、签字、导出、查看敏感数据的操作写审计日志 |
| P-8 | 依赖扫描、SAST、密钥扫描在 CI 中必须通过 |

## 7. AI 管线

| # | 规范 |
|---|---|
| A-1 | 提示词（prompt）是代码：纳入版本控制、代码评审，变更视同发布 |
| A-2 | 影响 AI 输出的变更（模型、提示词、阈值、模板）**必须**跑临床评测集回归，结果附在 PR |
| A-3 | 模型与供应商通过配置切换，并登记到 AI 登记册与子处理方清单 |
| A-4 | 每段 AI 输出记录：模型版本、提示词版本、输入引用（不复制明文）、校验结果 |
| A-5 | 每句草稿保留到来源语句的链接（可溯源） |

## 8. 测试

| # | 规范 |
|---|---|
| T-1 | 新逻辑必须有单元测试；修复缺陷先写能重现缺陷的测试 |
| T-2 | 归属、护栏、状态机、权限：**必须**有覆盖边界情况的测试（同名、代词、未同意老人、离线、重复提交） |
| T-3 | 测试只用合成数据；测试命名描述行为（`should_send_to_unassigned_when_two_residents_share_name`） |
| T-4 | 测试保持简单（KISS 同样适用）；不为了覆盖率写无意义的测试 |

## 9. 代码评审

| # | 规范 |
|---|---|
| R-1 | 所有代码经 PR 合并，至少 1 人评审；生产与安全相关变更由 Terry 以外的人评审 |
| R-2 | PR 小而聚焦（建议 ≤ 400 行改动）；描述写清"改了什么、为什么、怎么验证" |
| R-3 | 评审按下面清单进行 |

```markdown
### PR 检查清单
- [ ] `python company-os/11-rules/check_rules.py` 通过
- [ ] 核心 15 条：单一职责 · 命名清晰 · 无硬编码密钥 · 复杂逻辑先写"为什么" · 关键逻辑先有测试 · 无空 catch · 只在边界校验 · 默认最严权限 · 无 TODO/假数据 · 不突破性能底线 · 无多余新依赖 · 无 YAGNI 代码 · 可读 · 导出写明类型 · 无未登记的 any
- [ ] 格式：Tab 缩进（宽度 4，YAML 除外），格式化检查通过
- [ ] 文件大小：每个代码文件 ≤ 1000 行（超过 800 行说明计划）
- [ ] KISS：有没有更简单的写法？有没有为假想需求写的代码？
- [ ] DRY：业务规则是否只定义在一处？是否引入了重复的知识？
- [ ] SOLID：模块职责是否单一？外部服务是否通过接口注入？是否过度抽象？
- [ ] 安全失败：不确定时是否交给人处理？是否可能静默丢失输入？
- [ ] 无健康信息明文进入日志；无密钥；只用合成数据
- [ ] 外部 AI 调用使用澳洲区域
- [ ] 若影响 AI 输出：评测集回归已通过，Clinical Lead 已签字
- [ ] TGA：不引入诊断/治疗/用药建议或风险评分
- [ ] 测试覆盖新逻辑与边界情况
```

## 10. 文件大小与自动重构

| # | 规范 |
|---|---|
| SIZE-1 | 单个代码文件**超过 1000 行必须重构**以降低行数。由 [refactor-large-file](../10-skills/refactor-large-file/SKILL.md) skill 执行；重构完成前不得合并 |
| SIZE-2 | 超过 800 行为预警：不再往里加新职责，并在 PR 中说明重构计划 |
| SIZE-3 | 降低行数的方式只能是**拆分职责（SOLID 的 S）、去除重复（DRY）、删除死代码、简化逻辑（KISS）**。**禁止**为凑行数压缩格式、多语句写一行、删除必要注释或缩短命名 |
| SIZE-4 | 豁免：生成的代码、第三方 vendored 代码、数据库迁移、测试快照与 fixtures、锁文件；JSON / YAML 等数据与配置文件不计入 |
| SIZE-5 | 重构必须保持行为不变：前后测试全部通过；重构单独成一个 PR，不夹带功能变更；涉及 AI 管线时跑临床评测集（A-2） |
| SIZE-6 | 阈值与豁免规则只在 [`rule_config.py`](rule_config.py) 中定义（DRY）；修改阈值须写 DR |

### 自动触发

| 环境 | 机制 |
|---|---|
| Claude Code | `.claude/settings.json` 的 PostToolUse hook 在每次编辑后运行 [`hook_file_size.py`](hook_file_size.py)：超过 1000 行 → 阻断提示并要求立即运行 `refactor-large-file`；超过 800 行 → 预警 |
| Codex | 根目录 `AGENTS.md` 要求改完代码运行 `check_rules.py`，出现 `SIZE` 即运行 `$refactor-large-file` |
| CI / 提交前 | `python company-os/11-rules/check_rules.py` —— 有超限文件返回非零退出码 |

## 11. 性能底线 Performance Boundaries（CORE-10）

超过下表"不合格线"即为缺陷，必须修复或写 DR 说明例外。指标按 p95 计算（95% 的请求要达到），在真实网络条件下测量。

| 场景 | 目标 | 不合格线 | 来源 |
|---|---|---|---|
| 按下录音键 → 开始录音（含视觉/触感反馈） | ≤ 100 ms | > 300 ms | 一线可用性（PRD R-01） |
| 交互式 API 请求（读取/保存/签字） | ≤ 500 ms | **> 2 s** | 用户要求 |
| App 冷启动到可录音 | ≤ 2 s | > 4 s | 一线可用性 |
| 单段语音 → 草稿可见（联网） | ≤ 30 s | > 60 s | PRD E7 |
| 班末 40 段批处理 | ≤ 3 min | > 5 min | PRD E7 |
| 待审核列表加载（≤ 50 条草稿） | ≤ 1 s | > 2 s | 用户要求 |
| 离线缓存的录音在恢复联网后开始上传 | ≤ 10 s | > 60 s | PRD R-02 |

- 新增接口或页面时，在 PR 中写明适用哪一行；没有对应行时先补充本表
- 性能优化不得以牺牲 §5 安全失败、§6 隐私为代价

## 12. 类型 Types（CORE-14、CORE-15）

| # | 规范 |
|---|---|
| TY-1 | TypeScript 开启 `strict: true`；导出的函数写明参数与返回类型；ESLint `explicit-module-boundary-types` 与 `no-explicit-any` 均为 error |
| TY-2 | Python 公开函数（模块级、不以 `_` 开头）完整类型标注；类型检查（mypy 或 pyright）严格模式在 CI 中必须通过 |
| TY-3 | 外部数据（API 响应、ASR/LLM 输出、文件）进入时先解析为明确类型（如 zod / pydantic schema），之后内部只使用该类型（与 CORE-07 配合） |
| TY-4 | `any` / `Any` 只能在 [any-whitelist.md](any-whitelist.md) 登记并获批后使用，且该行须有 `any-allowed: <编号>` 注释；`check_rules.py` 会拦截未登记的使用 |
