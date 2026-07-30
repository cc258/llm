## LangChain

B站
【黑马程序员2026最新版LangChain+LangGraph开发实战全套视频课程，从Agent开发，到LangSmith的监控、调试、评估一套搞定】https://www.bilibili.com/video/BV178w1z7EHQ?vd_source=44afd7b0dd2cd7ac6310831106137c4e


## 目录
app/agents
notebook


## Lession 0

2022年11月30日 ChatGPT横空出世，推开AI大门
交互，写诗，聊天
企业应用的刚需，
自动化的工作流重塑生产力，
AI数据分析正在协助企业做战略规划
24*7小时的智能客服也在替代人工客服
企业对于Agent开发的岗位需求正在井喷
薪资也是水涨船高，

掌握Agent开发，就是工程师向高级AI工程师跃迁的生死线
Agent开发技术比较复杂，拿OpenClaw为例，其中包括：
信息接入， 网关路由，深度推理，记忆管理，工具执行，会话管理等细节
有什么工具可以简化Agent的开发呢？

企业主流开发Agent的主流技术就是LangChain
LangChain提供了Agent的开发，调试，评估，部署的完整工具。
可以大大简化Agent的开发，玩转Agent， RAG的开发


## 三大重点 Deep Agents/LangChain/LangGraph


学习大纲：
Agent入门: AI通识，Langchain组件，Agent开发，Langsmith调试，私厨管家
Agent进阶：Runtime，Middleware，MCP，Muti-agent，Agent-Chat-UI,邮帮，嫁爱
RAG Agent： RAG原理，Milvus，查询优化，知识检索优化，系统评估，个人知识库
LangGraph：基本概念，流程控制，记忆管理，常见workflow，个人智能助手


## Lession 2

AI 需要经过训练才能具备智能
AI是怎样进行训练的，
又是怎样理解人类语言的呢？
AI的核心，也就是神经网络的原理。
神经网络的结构，
AI的核心是Transformer, 这是一种神经网络，本质是模拟人类的神经元，
将千千万万个神经元组成的网络，就是深度神经网络。


## Lession 3-4
深度神经网络的分层：
输入层，隐藏层，输出层。

神经网络的结构
基本流程如下：
前向传播
计算误差，误差的计算，有专门的损失函数
反向追责
调整权重， 梯度下降

词向量——把词转换为多维空间向量的一种技术
- 首先，将人类自然语言拆分成一个个片段，称为Token
- 每个Token都经过模型计算转为一个浮点数数组，作为向量坐标。
- 使词向量不同语义指向多维空间中的不同的方向。

GPT3中，一个词向量，包含12288个浮点数，代表了多维空间中的位置。
最终通过训练模型，不断的去调整 词 在空间中的位置。

2017年，Google发表的论文《Attention is all you need》中提出Transformer模型，
其中的自注意力机制（Self-attention）,使模型更高效处理Token.

词向量只是Transformer模型中的第一步，接下来还有很多步骤要去做。
Word Embedding > Attention > MLP >  Attention > MLP > … > softmax

Softmax根据模型计算出的向量结果，得出下一个Token的概率分布，然后基于概率的随机采样方式挑选一个作为结果，这个概率受模型的Temperature参数影响，值越大，越随机。


## Lession 5 大模型服务

#### 公共大模型
deepseek, chatGPT, kimi
优点：
全球访问，无需部署，无需维护
缺点：
定制受限，成本高，网络依赖，数据隐私

#### 私有大模型
Ollama 部署
高度定制，成本低，数据安全，不依赖外部网络，


## Lession 9 大模型API接口规范

大模型接口都遵循OpenAI规范，大同小异

URL， 
API Key, 
请求参数：temperature取值范围[0,2], model, message, stream，

## Lession 10 会话记忆

大模型提供的服务是无状态的
每一轮请求响应是一次会话。
不具备记忆功能。

需要记忆的话，
需要把前面的完整对话，加到后面的请求中。

注意如果是一次性的LLM应用，不需要记忆。

## Lession 11 开发环境
uv
notebook

```uv add notebook```


## Lession 25 实战

Langchain的Agent底层是基于LangGraph的。
LangGraph提供了完整的后端部署功能，自带非常完善的后端接口，【可以不使用FastAPI】意思是能跑起来。
同时Langchain也提供了基于LangSmith的GUI控制太实现Agent的调试，监控，一键部署。
利用LangGraph，可以实现Agent的部署，监控，评估。
通过LangSmith做测试。

QA：到底需不需要FastAPI？
答案：
- 只做独立智能体、快速部署、用官方 CLI 启动服务：**不需要 FastAPI**；
- 对接自研业务系统、自定义接口、统一网关、深度私有化：**必须写 FastAPI 封装**。


### 配置LangSmith

注册地址：https://www.langsmith.com/register

注册 》APIKEY

1. 配置apikey到环境变量中
   ```bash
   export LANGSMITH_API_KEY=sk-xxxx
   export LANGSMITH_TRACING=true
   ```

2. 安装LangSmith
   ```bash
   uv add "langgraph-cli[inmem]"
   ```
3. 手动实现配置文件
    langgraph.json

4. 使用命令
   ```bash
   uv run langgraph dev
   ```











