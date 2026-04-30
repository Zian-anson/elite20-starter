# Zian-anson Elite20 — AI 视频生产工作流

## 一句话定位

基于 Hermes 多 Agent 架构的 AI 视频批量生产系统，支持从需求分析到文案生成到视频合成的完整链路验证。

## 核心产出

- **文案生成链路**：orchestrator → analyst + writer → reviewer → 用户决策（✅ 已跑通）
- **视频生成链路**：maker → video-reviewer → optimizer（⚠️ 调度链路已验证，实际生成待接入 API）
- **分发链路**：social-auto-upload → 7个平台（待实现）

## 项目结构

```
elite20-starter/
├── students/Zian-anson/
│   ├── reflections/        # D1 反思
│   ├── prompts/           # D4 三个 prompt-trace
│   ├── artifacts/         # D5 Skill调用、D9 产物+trace
│   ├── kstar/             # D7 K-S-T-A-R 工作表
│   └── coordinate-cards/   # D8 3D坐标卡
├── retros/                # D10 展示与回顾
├── ai_logs/               # AI 对话日志
├── experiment_logs/        # 实验日志
└── portfolio.md           # Portfolio 条目
```

## 快速验证（复现用）

```bash
# 复制仓库
git clone https://github.com/Zian-anson/elite20-starter.git
cd elite20-starter

# 查看工作流文件
cat students/Zian-anson/artifacts/D9-artifact-trace.md
cat students/Zian-anson/kstar/D7-kstar-worksheet.md
```

## 证据账本

- AI 日志：`ai_logs/chat_log.md`
- 拿来说明：`REUSE.md`
- 方案设计：见各 `students/Zian-anson/` 子目录

## Week 1-2 完成情况

| 检查项 | 状态 |
|--------|------|
| GitHub fork + ≥3 commits | ✅ 4+ commits |
| D2 环境截图 | ⚠️ 用链路验证截图替代 |
| reflections/D1.md | ✅ |
| prompts/D4-P{1,2,3}.md | ✅ |
| D5 Skill 调用 | ✅ writer profile |
| kstar/D7-kstar-worksheet.md | ✅ |
| coordinate-cards/D8.md | ✅ |
| D9 产物 + trace | ✅ 文案已出，视频待生成 |
| D10 展示 + retro | ✅ |

## 约束说明

视频生成环节（maker）**未实际调用外部 API**，仅完成了调度链路的正确性验证。原因：Hailuo/Kling API 额度不足。下一步接入实际 API 后完成全链路。

## 致谢

- Elite20 课程模板：liyan55/elite20-starter
- Hermes 多 Agent 架构参考：麦冬视频 / Hermes 官方文档
