# 黑马程序员大模型RAG与Agent智能体项目实战教程


【黑马程序员大模型RAG与Agent智能体项目实战教程，基于主流的LangChain技术从大模型提示词到实战项目】https://www.bilibili.com/video/BV1yjz5BLEoY?p=8&vd_source=44afd7b0dd2cd7ac6310831106137c4e


# Dep

uv add dashscope langchain_community langchain_chroma chromadb


# OpenAI库基础使用

### 获取客户端对象

```
from openai import OpenAI

client: OpenAI = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_BASE_URL"),
)

```

api_key 模型服务商提供的APIKEY密钥
base_url 模型服务商API接入地址


```

from openai.types.chat.chat_completion import ChatCompletion

response: ChatCompletion = client.chat.completions.create(
    model="deepseek-v4-pro",
    messages=[
        {"role": "system", "content": "你是一个Python开发人员"},
        {"role": "assistant", "content": "我是Python开发人员，有什么课可以帮助您的吗？"},
        {"role": "user", "content": "For循环输出 1 到 5 的数字。"},
    ],
)

```

### 处理结果
```
print(response.choices[0].message.content)
```


以上就完成了AI模型的调用了。

实际例子：
notebook/class2/openAI.ipynb


### 小结
OpenAI库是一个基于Python的库，用于调用OpenAI的API。

主要使用就 3 个流程：
1. 获取客户端对象（OpenAI类对象）
2. 调用模型（client.chat.completions.create类对象）
3. 处理结果（response对象）

实际例子：
notebook/class2/openAI.ipynb


# LangChain中链的使用

LangChain 链是顺序执行的多个串联组件。
通过 “｜” 符号让各个组件形成链
链的组件，需要是Runnable对象。
前一个组件的输出，是后一个组件的输入。
可通过链调用invoke或者stream方法，来执行链。



