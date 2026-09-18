# Python Developer Lab

本地优先的 Python 学习与软件工程训练平台。V1 实现课程/题目浏览、受限本地执行、自动判题、提交记录、进度统计和分级 Hint。

## 快速开始

需要 Python 3.13+。

复制 .env.example 为 .env，然后运行：

    python -m venv .venv
    pip install -e ".[dev]"
    python -m scripts.seed_content
    uvicorn app.main:app --host 127.0.0.1 --port 8000

打开 http://127.0.0.1:8000，API 文档位于 /docs。

## Docker 启动

本项目使用 SQLite，数据库文件持久化在 Compose volume `app-data` 中。确保本机已安装 Docker Desktop 后，在仓库根目录运行：

    docker compose up --build

打开 http://127.0.0.1:8000，停止服务：

    docker compose down

如需接入 OpenAI-compatible 服务，可在启动前设置 `AI_BASE_URL`、`AI_API_KEY`、`AI_MODEL` 和 `AI_TIMEOUT_SECONDS`。Compose 仅绑定到本机 `127.0.0.1`，符合 V1 的本地优先边界。

## 测试与质量

    pytest
    ruff check .
    pyright

## 安全边界

V1 执行器仅面向 localhost 开发，不是公网代码沙箱。它使用临时目录、参数数组、shell=False、超时、输出截断和基础 AST 检查。上线 LAN/NAS 前必须替换为 Docker Executor。
