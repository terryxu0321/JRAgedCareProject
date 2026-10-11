# BottomSheet

App 中从底部升起的面板：选项列表、筛选、次要操作，单手够得到。

- `canvas` 底，只有顶部两角 `rounded-lg`；顶部 36×5 拖动条（`border-input`，`rounded-pill`）；下方 `scrim`。
- 标题 `tagline`；选项用 `list-item`，每项至少 48px。
- 可下滑或点遮罩关闭；必须同时提供可见的关闭方式（"Done" 或关闭按钮）。
- 选项多时顶部放 `search-input`。
