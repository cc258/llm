# 使用官方 Python 基础镜像
FROM python:3.12-slim

# 安装系统依赖
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# 安装 uv（更快的包管理器）
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /usr/local/bin/

# 设置工作目录
WORKDIR /app

# 复制依赖文件（利用缓存）
COPY pyproject.toml uv.lock ./

# 创建虚拟环境并安装依赖
ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --no-dev --frozen

# 复制项目代码
COPY . .

# 创建数据目录
RUN mkdir -p /app/rag/chroma_db

# 设置环境变量
ENV PYTHONUNBUFFERED=1
ENV STREAMLIT_BROWSER_GATHER_USAGE_STATS=false

# 暴露端口
EXPOSE 8501

# 启动 Streamlit
CMD ["uv", "run", "streamlit", "run", "rag/qa.py", \
     "--server.port", "8501", \
     "--server.address", "0.0.0.0", \
     "--server.headless", "true"]
