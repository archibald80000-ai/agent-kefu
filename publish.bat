@echo off
chcp 65001 >nul
echo =========================================
echo     agent-kefu-learning GitHub 发布助手
echo =========================================

if not exist ".git" (
    echo 初始化 Git 仓库...
    git init
)

git add .
git commit -m "chore: prepare public learning release"
git branch -M main

set /p RepoUrl="请输入 GitHub 仓库地址 (例如 https://github.com/Username/agent-kefu-learning.git): "
if "%RepoUrl%"=="" (
    echo [错误] 仓库地址不能为空
    pause
    exit /b 1
)

git remote add origin %RepoUrl% 2>nul
if %errorlevel% neq 0 (
    git remote set-url origin %RepoUrl%
)

git push -u origin main
echo 发布完成
pause
