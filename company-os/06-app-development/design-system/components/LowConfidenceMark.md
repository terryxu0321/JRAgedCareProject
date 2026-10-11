# LowConfidenceMark

把转写中需要核对的词（药名、剂量、数字、姓名）标出来，逐个点开确认（hazard H-02）。

- `low-confidence-mark` —— `status-attention-bg` 底、`ink` 文字、2px 点状 `status-attention` 下划线，后接 "Check" 标签。
- 每个标记是一个按钮：点开后显示原始录音片段与可选写法，确认或改写后标记消失。
- 有未核对的标记时，所在段落不能确认（`section-confirm` 禁用并说明原因）。
- 读屏：标记读作 "<词>, needs checking"。
- 夜班主题下划线用 `status-attention-on-dark`。
- 安全关键组件：规格由任务 T-0005 定稿，Clinical Lead 审阅前不得用于生产。
