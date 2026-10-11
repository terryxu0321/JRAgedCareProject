# Design System 设计系统

> Owner: Terry（风格决定）｜ 维护：Dave（SPEC-003 Assignee）｜ 需求：[SPEC-003](../specs/2026-10-design-system.md)

**[DESIGN.md](DESIGN.md) 是 CareKind 设计规范的唯一来源（SoT）**：文件头部 YAML 定义全部 token（颜色、字体、间距、尺寸、圆角、层次、动效、组件），正文说明用法、Do / Don't、响应式与对参考风格的调整。

风格：Terry 于 2026-10-11 选定的极简风格 —— 界面隐身、单一蓝色强调色、浅色 / 近黑表面交替、胶囊按钮；并为护理场景加强了无障碍（48px 触控、17px 正文、WCAG 2.2 AA 对比度）与安全状态（AI 草稿 / 已确认 / 需核对）。

## 怎么用

- 设计稿、代码、AI 生成的界面：只引用 `{colors.primary}` 这类 token，不写十六进制颜色或像素字号
- 新增或修改 token：先改 DESIGN.md 的 YAML，再改正文；新颜色先算对比度
- 平台产物（CSS 变量、iOS、Android）由 DESIGN.md 生成（任务 T-0007），不手写第二份

## 相关任务

T-0002 tokens 校验与夜班主题 · T-0003 无障碍清单 · T-0004 基础组件 · T-0005 安全关键组件 · T-0007 构建与 CI —— 见 [adlc/tasks/](../adlc/tasks/README.md)
