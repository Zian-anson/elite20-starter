# 上传到 GitHub 指南

## 前置条件

1. 已安装 Git（可从 https://git-scm.com/downloads 下载）
2. 已注册 GitHub 账号（https://github.com/signup）
3. 在 GitHub 上创建了一个空仓库

## 操作步骤

### Step 1: 打开终端

- **Windows**: 打开 Git Bash 或 PowerShell
- **macOS/Linux**: 打开 Terminal

### Step 2: 进入项目目录

```bash
cd e:\HuaweiMoveData\Users\67512\Desktop\11\elite20-starter
```

### Step 3: 初始化 Git 仓库

```bash
git init
```

### Step 4: 配置 Git 用户信息

```bash
git config user.name "Your GitHub Username"
git config user.email "your-email@example.com"
```

### Step 5: 添加所有文件

```bash
git add .
```

### Step 6: 第一次 Commit（初始化项目结构）

```bash
git commit -m "feat: 初始化 Elite20 starter 项目结构"
```

### Step 7: 添加更多文件

```bash
git add ai_logs/chat_log.md
git commit -m "docs: 添加 AI 对话日志记录"
```

### Step 8: 添加实验日志和 Portfolio

```bash
git add experiment_logs/exp_01.md portfolio.md
git commit -m "docs: 添加实验日志和 Portfolio 条目"
```

### Step 9: 关联 GitHub 远程仓库

```bash
git remote add origin https://github.com/your-username/elite20-starter.git
```

**注意**: 替换 `your-username` 为你的 GitHub 用户名

### Step 10: 推送到 GitHub

```bash
git push -u origin main
```

### Step 11: 验证上传

打开浏览器访问你的 GitHub 仓库：
```
https://github.com/your-username/elite20-starter
```

## 确认清单

上传完成后，请确认以下内容：

- [ ] ✅ 项目结构完整
- [ ] ✅ 3 个 Commit 已推送
- [ ] ✅ README.md 可见
- [ ] ✅ REUSE.md 可见
- [ ] ✅ src/main.py 可见
- [ ] ✅ ai_logs/chat_log.md 可见
- [ ] ✅ experiment_logs/exp_01.md 可见
- [ ] ✅ portfolio.md 可见

## 常见问题

### Q1: 推送时提示权限错误
**解决**: 检查远程仓库 URL 是否正确，确保你有权限访问该仓库

### Q2: 提示 "fatal: remote origin already exists"
**解决**: 删除现有远程配置，重新添加
```bash
git remote remove origin
git remote add origin https://github.com/your-username/elite20-starter.git
```

### Q3: 提示需要登录
**解决**: 使用 GitHub Personal Access Token 作为密码
- 在 GitHub 上生成 Token（Settings → Developer settings → Personal access tokens）
- 推送时用户名填 GitHub 用户名，密码填 Token

## Commit 记录预览

| Commit Hash | 提交信息 | 修改内容 |
|-------------|----------|----------|
| (自动生成) | `feat: 初始化 Elite20 starter 项目结构` | README.md, REUSE.md, src/main.py, .gitignore |
| (自动生成) | `docs: 添加 AI 对话日志记录` | ai_logs/chat_log.md |
| (自动生成) | `docs: 添加实验日志和 Portfolio` | experiment_logs/exp_01.md, portfolio.md |

## 后续步骤

上传完成后，你可以：
1. 在 GitHub 上查看你的仓库
2. 继续添加更多功能
3. 创建 Pull Request
4. 邀请同伴进行代码审查