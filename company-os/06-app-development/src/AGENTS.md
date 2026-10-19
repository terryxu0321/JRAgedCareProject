# AGENTS.md — src — 代码仓库

> AI 助手在本目录工作前必读。全局规则：根目录 `AGENTS.md` 与 `company-os/11-rules/`。人类说明：同目录 `README.md`。完成任务后按 `changelog-rules.md` 写 `changelog/CHANGELOG.md`。

## 这个目录是什么
CareKind 产品代码。按 PRD C1 架构划分模块；每个模块目录有 README / AGENTS / CLAUDE 说明其职责与边界。正式代码将迁入独立 GitHub 私有仓库（届时本目录保留链接与这些说明）。

## 关键文件
- `mobile-app/` —— 护理人员 App
- `api/` —— 网关、认证授权、审计
- `ai-pipeline/` —— 转写 → 拆分 → 归属 → 分类 → 抽取 → 起草 → 护栏
- `review-service/` —— 审核状态机、事件快速通道
- `record-store/` —— 签字记录、时间线、保留与删除
- `integrations/` —— 导出与护理系统回写
- `admin-web/` —— 养老院管理端（公司 + 多家养老院；第一阶段合并进养老院 Web App）
- `super-admin/` —— Super Admin App（独立 React JS，CareKind 平台方管理客户公司）

## 在这里工作的规则
- 先读将要修改的模块的 `AGENTS.md`；跨模块只通过接口调用（SOLID D）
- 只用合成数据开发与测试（P-3）；日志不含健康信息（P-1）
- 关键逻辑先写测试（CORE-05）；改完运行 `python company-os/11-rules/check_rules.py`
- 影响 AI 输出的变更须跑临床评测集并由 Clinical Lead 签字（A-2）
