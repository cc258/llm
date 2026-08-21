from  langchain.chat_models import init_chat_model
from langchain_tavily import TavilySearch
from langchain.agents import create_agent
import os

# 1. 加载环境变量
from dotenv import load_dotenv
load_dotenv()

# 2. web搜索工具, 使用tavily作为web搜索工具
web_search = TavilySearch(
    max_results = 0,
    topic = "general"
)

# 3. 多模态模型
### 不再需要checkpoint，LangSmitch已经自带了,加了会报错。

model = init_chat_model(
    model="qwen3.8-max",
    model_provider="openai",
    base_url=os.getenv("OPENAI_BASE_URL"),
    api_key=os.getenv("OPENAI_API_KEY"),
)

# 4. Agent系统提示词
system_prompt = """
你是凯瑟琳，是个逗逼，用有趣独特精简的视角，用中英双语来回答问题。回答时，固定用“凯瑟琳：”。
"""

# 5. 创建Agent
agent = create_agent(
    model=model,
    # tools=[web_search],
    system_prompt=system_prompt,
)



