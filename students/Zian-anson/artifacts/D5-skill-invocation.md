# D5 Skill Invocation — Zian Anson

**Date:** 2026-04-28

**Skill used:** `writer` (copywriter profile)
**Invoked via:** `copywriter chat -q "主题：AI写代码改变程序员未来..."`

---

## What the Skill does

The `writer` profile is a Hermes Skill/Profile that acts as a specialized copy generator for AI videos. It:
- Reads a requirement analysis JSON from the shared task directory
- Generates 2 versions of copy (hook → pain point → solution → CTA)
- Writes each version to `01-copy-draft-v{n}.json`
- Waits for reviewer feedback to iterate

## Real input I gave it

```
主题：AI写代码改变程序员未来
平台：抖音
时长：30秒
风格：口语化有钩子
```

## Artifact produced

Two copy drafts were generated (v1 and v2). Here's v1:

> **「AI帮我写代码这一天，我终于准点下班了」**
> 
> [0-3秒] 你有没有过这种经历？周一早上，堆成山的CRUD代码等着你。
> [3-10秒] 现在有了AI，你只要说清楚需求，重复代码它全包了。
> [10-20秒] 程序员老王实测：每天省下2小时做更有创造力的项目。
> [20-30秒] 想知道自己用AI提效的正确姿势？关注我，持续分享实操经验。

## One-paragraph explanation

这个 Skill 本质上是一个「文案生成专家 Agent」。调用时只需要给出任务描述（主题、平台、时长、风格），它就能自动生成符合要求的文案。它的优势在于：
1. 理解不同平台的文案差异（抖音要短平快，小红书要生活化）
2. 输出结构化 JSON，方便后续审核和视频制作流程衔接
3. 支持多版本迭代，审核不通过可以自动修改

**Key insight:** Skill 就像一个「.recipe book」——你不需要知道它怎么做，只要告诉它你要什么，它就会按配方输出结果。
