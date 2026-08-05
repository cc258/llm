try:
    from rag.secrets_loader import load_secrets
    from rag import config_data as config
except ImportError:
    from secrets_loader import load_secrets
    import config_data as config

from langchain_chroma import Chroma
from langchain_community.embeddings import DashScopeEmbeddings

load_secrets()

class vectorStoreService(object):

    def __init__(self, embedding):

        self.embedding = embedding
        self.vector_store = Chroma(
            collection_name=config.KNOWLEDGE_BASE_COLLECTION_NAME,
            embedding_function=embedding,
            persist_directory=config.KNOWLEDGE_PERSISTENT_DIR,
        )

    def get_retriever(self):
        return self.vector_store.as_retriever(search_kwargs={"k": 3})



if __name__ == '__main__':
    retriever = vectorStoreService(DashScopeEmbeddings()).get_retriever()
    res = retriever.invoke("身高175， 尺码推荐")
    print(res)