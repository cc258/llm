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
根据以下知识库内容回答用户问题。如果知识库中没有相关信息，请礼貌告知。

知识库内容：
{context}

用户问题：{question}
回答：
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
        if not docs:
            return ""
        # 给每段内容加上编号，帮助模型理解上下文
        parts = []
        for i, doc in enumerate(docs, 1):
            parts.append(f"[{i}] {doc.page_content}")
        return "\n".join(parts)

    def ask(self, question: str) -> str:
        """提问"""
        return self.chain.invoke(question)


if __name__ == '__main__':
    rag = RagService()
    res = rag.ask("身高185，尺码推荐")
    print(res)
