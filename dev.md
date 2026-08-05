# Development


# Quick Start

```
uv sync

<!-- 启动 langgraph 服务 -->
uv run langgraph dev

<!-- 测试本地模型 -->
uv run ./app/agents/llm_local.py

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
