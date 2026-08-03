try:
    # 作为包导入时（项目根目录运行）
    from rag.vector_stores import vectorStoreService
    from rag.secrets_loader import load_secrets
except ImportError:
    # 直接运行时
    from vector_stores import vectorStoreService
    from secrets_loader import load_secrets

from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.chat_models import ChatTongyi
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

load_secrets()


class RagService(object):

    def __init__(self):
        # 1. 向量检索服务
        self.vector_service = vectorStoreService(embedding=DashScopeEmbeddings())
        self.retriever = self.vector_service.get_retriever()

        # 2. Prompt 模板
        self.prompt = PromptTemplate.from_template("""
        你是客服，从知识库中提取最相关的答案，如果没有相关信息，请回答“不知道”。
        {context}
        问题：{question}
        答案：
        """)

        # 3. 大模型
        self.chat_model = ChatTongyi()

        # 4. 构建 RAG 链：检索 -> 拼接上下文 -> 填充prompt -> 调用模型 -> 解析输出
        self.chain = (
            {"context": self._retrieve_context, "question": RunnablePassthrough()}
            | self.prompt
            | self.chat_model
            | StrOutputParser()
        )

    def _retrieve_context(self, question: str) -> str:
        """从向量库检索相关文档并拼接成上下文"""
        docs = self.retriever.invoke(question)
        return "\n".join(doc.page_content for doc in docs)

    def ask(self, question: str) -> str:
        """提问"""
        return self.chain.invoke(question)


if __name__ == '__main__':
    rag = RagService()
    res = rag.ask("身高185，尺码推荐")
    print(res)
