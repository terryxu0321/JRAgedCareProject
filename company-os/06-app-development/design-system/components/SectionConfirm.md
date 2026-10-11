# SectionConfirm

关键段落逐段确认，**没有**"全部确认"，防止不读就点（hazard H-08）。

- 每个关键段落（如事件、用药相关陈述、跌倒）一行：段落名 + 一个 `selection-chip` 形状的 "Confirm" 按钮；确认后变为 `selection-chip-selected` 样式 + "✓ Confirmed"。
- 段落里还有未核对的 `low-confidence-mark` 时，按钮禁用，并在行内说明 "Check 1 word first"。
- 底部 `action-bar` 显示进度（"2 of 3 sections confirmed"）。
- 确认动作写入审计（谁、何时）。
- 安全关键组件：规格由任务 T-0005 定稿，Clinical Lead 审阅前不得用于生产。
