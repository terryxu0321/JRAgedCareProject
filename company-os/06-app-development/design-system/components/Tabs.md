# Tabs

分段控件：在同一页面的 2–4 个视图之间切换（如 "To review / Confirmed"）。

- `canvas-parchment` 胶囊轨道、2px 内边距；选中段 `canvas` 底 + `elevation-hairline` + `caption-strong`；未选段 `caption` + `ink`。
- 每段至少 44px 高，整个控件高 48px。
- 段名短（一两个词），可带数量："To review (2)"。
- 读屏：`role="tablist"` / `role="tab"` + `aria-selected`。
- 切换页面层级用 `tab-bar`，不用 tabs。
