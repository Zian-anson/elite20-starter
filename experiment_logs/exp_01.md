# 实验日志

## 实验 1：Hermes 多 Profile 环境验证

**日期：** 2026-04-28
**实验目标：** 验证 9 个 Hermes Profile 能否正常加载并互相调用

### 参数设置
- 环境：Mac Mini M4 16GB
- Hermes 版本：v0.11.0
- 模型：MiniMax-M2.7
- Profile 数量：9 个（default + 8 执行 Agent）

### 执行步骤
1. 配置 8 个执行 Agent 的 SOUL.md
2. 创建 hermes profile alias
3. 测试 orchestrator → writer 调用
4. 测试 orchestrator → analyst + writer 并行调用
5. 测试 writer → reviewer 串行调用

### 结果记录
- ✅ 9 个 Profile 全部加载成功
- ✅ orchestrator 正确调度各 Agent
- ✅ writer 生成文案耗时 14 秒
- ✅ 并行调度（analyst + writer）比串行节省约 40% 时间

### 问题与解决
- 问题：reviewer 的审核结果未自动触发 writer 迭代
- 解决：改为 orchestrator 汇总两个版本输出给用户决策

---

## 实验 2：视频生成链路验证（未实际生成）

**日期：** 2026-04-29
**实验目标：** 验证 maker → video-reviewer → optimizer 串行链路

### 参数设置
- 视频生成服务：Hailuo（免费主力）/ Kling（备用）
- 当前可用额度：Hailuo ~100 credits/天，Kling 66 credits/天
- API 状态：额度不足，未完成接入

### 执行步骤
1. orchestrator 解析任务，判断 maker 需调用外部视频 API
2. orchestrator 展示 maker 的输入参数（文案、时长、风格、输出格式）
3. orchestrator 展示 video-reviewer 的审核维度
4. orchestrator 展示 optimizer 的优化目标

### 结果记录
- ✅ 链路参数拆解正确
- ⚠️ 视频未实际生成（API 额度不足）
- 🔜 下一步：接入 Hailuo/Kling API 后完成实际生成

---

## 实验 3：Week 1-2 作业补交

**日期：** 2026-04-30
**实验目标：** 按 Elite20 规范补交 Week 1-2 作业到 GitHub

### 执行步骤
1. Fork liyan55/elite20-starter
2. 创建 students/Zian-anson/ 目录结构
3. 撰写 9 个交付文件（D1-D10）
4. 通过 GitHub API 上传所有文件

### 结果记录
- ✅ Fork 成功
- ✅ 9 个文件全部上传
- ✅ 截图作为 D9 证据上传

### 问题与解决
- 问题：macOS 拦截 git push（credential helper 不工作）
- 解决：改用 GitHub REST API 直接上传
