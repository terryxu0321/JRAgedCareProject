# TextArea

多行文本输入：外观与 `input` 一致，最小 120px 高。

- `body` 字样，随内容增高；可选字数提示（`caption` + `ink-muted`），接近上限时提示仍用 `ink-muted`，超出时改为 `status-error` + 说明。
- 用于护士手动补充或修改记录；AI 生成的内容不放在普通 textarea 里，而是放在 `draft-card` 中编辑。
