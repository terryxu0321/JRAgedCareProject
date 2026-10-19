# AGENTS.md — marketing-site — 营销网站

> AI 助手在本目录工作前必读。全局规则：根目录 `AGENTS.md` 与 `company-os/11-rules/`。人类说明：同目录 `README.md`。完成任务后按 `changelog-rules.md` 写 `changelog/CHANGELOG.md`。

## 职责
对外宣传网站：纯 HTML + CSS，少量脚本（导航、表单校验与提交）用 TypeScript 编写、`tsc` 编译；**不用 Next.js、React 或其他框架**（Terry 2026-10-19）。每页一个 `.html`，共用 `styles.css`（DESIGN.md token 写成 CSS 变量）。**只做英文。**不调用产品 API，不读写产品数据库；联系表单只提交到 CareKind 自己的线索接口。

## 负责的功能（SPEC-012 编号）
- 页面 MW-01 至 MW-07（P0）；MW-08 关于我们（P1）；MW-09、MW-10（P2）

## 规则与边界
- **文案就是预期用途（TGA）**：不得出现 detects、predicts、diagnoses、monitors、clinical decision support、early warning、"TGA approved"、"提升 AN-ACC 资助"
- 不写没有试点证据的数字；不点名比较竞争对手（ACL）
- 录音只描述为按键口述，不暗示环境录音
- 营销邮件同意单独勾选，不预勾选（Spam Act）；表单不收集居民或健康信息
- 截图只用合成数据；不用真实居民照片；考拉吉祥物不用于网站；logo 作为图片放置
- 只用 `design-system/DESIGN.md` 中 `scope: web` 的 token 与组件；WCAG 2.2 AA
- 每次发布前过 `07-marketing-operations/marketing-compliance.md` 清单，🛑 Terry 审核
- 不得编造团队成员、客户、评价

## 必须覆盖的测试
- 构建时扫描禁用词，命中即失败
- 未勾选营销同意时不进入邮件列表
- Lighthouse 移动端可访问性 ≥ 90

## 参考
- `company-os/06-app-development/specs/2026-10-marketing-website.md`
- `company-os/07-marketing-operations/brand-and-messaging.md`
- `company-os/07-marketing-operations/marketing-compliance.md`
