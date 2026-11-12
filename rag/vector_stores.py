try:
    from rag.secrets_loader import load_secrets
    from rag import config_data as config
except ImportError:
    from secrets_loader import load_secrets
    import config_data as config

import os
from langchain_chroma import Chroma
from langchain_community.embeddings import DashScopeEmbeddings

load_secrets()


def build_chroma(collection_name, embedding_function):
    """配置了 CHROMA_HOST 时连接独立的 Chroma 服务器（供 Chroma UI 连接），否则用本地持久化模式"""
    host = os.getenv('CHROMA_HOST')
    if host:
        import chromadb
        client = chromadb.HttpClient(host=host, port=int(os.getenv('CHROMA_PORT', '8000')))
        return Chroma(
            collection_name=collection_name,
            embedding_function=embedding_function,
            client=client,
        )
    return Chroma(
        collection_name=collection_name,
        embedding_function=embedding_function,
        persist_directory=config.KNOWLEDGE_PERSISTENT_DIR,
    )


class vectorStoreService(object):

    def __init__(self, embedding):
        self.vector_store = build_chroma(
            collection_name=config.KNOWLEDGE_BASE_COLLECTION_NAME,
            embedding_function=embedding,
        )

    def get_retriever(self):
        return self.vector_store.as_retriever(search_kwargs={"k": 3})


if __name__ == '__main__':
    retriever = vectorStoreService(DashScopeEmbeddings()).get_retriever()
    res = retriever.invoke("身高175， 尺码推荐")
    print(res)
