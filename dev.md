# Development


# Quick Start

```
uv sync

<!-- 启动 langgraph 服务 -->
uv run langgraph dev

<!-- 测试本地模型 -->

# 第 1 步：Chroma 服务器（必须先启动，Streamlit 连它）
uv run chroma run chroma.yaml

# 第 2 步：RAG 问答（另开终端）
uv run streamlit run rag/qa.py --server.port 8501 --server.address 0.0.0.0

# 第 3 步：Agent 凯瑟琳（另开终端）
uv run streamlit run agent/app.py --server.port 8502 --server.address 0.0.0.0



<!-- 启动 jupyter notebook 服务 -->
uv run jupyter notebook

<!-- 激活虚拟环境 -->
source .venv/bin/activate

```



# Create a new project

### uv init
- 生成 main.py 入口文件, 
- 生成 pyproject.toml 项目配置

```shell
uv init -p 3.14
```

### Dependencies

```
uv add openai langchain langchain-openai numpy pandas matplotlib jupyter notebook
```


# Pandas 只有两个核心数据结构，记住就够了：

Series：一维数据（一列数据）
DataFrame：二维表格（行 + 列，像 Excel）


# jupyter

```shell
uv run jupyter notebook
```
