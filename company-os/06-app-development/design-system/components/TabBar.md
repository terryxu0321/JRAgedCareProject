# TabBar

App 的底部主导航：3–5 个一级页面，图标加文字。

- 半透明表面（与 `top-bar-frosted` 相同），56px 高 + 底部安全区；每项至少 48×48。
- 选中项 `primary`（图标与文字），未选 `ink-muted`；文字 `caption`，始终显示文字，不只用图标。
- 只出现在一级页面；进入详情页后由 `action-bar` 取代。
- 读屏：当前项 `aria-current="page"`。
