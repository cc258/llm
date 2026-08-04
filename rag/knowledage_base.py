import os
import re
import hashlib
from datetime import datetime
from langchain_chroma import Chroma
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter


def clean_text(text: str) -> str:
    """清洗文本：去除多余空格、换行、特殊字符"""
    # 1. 去除 HTML 标签
    text = re.sub(r'<[^>]+>', '', text)
    # 2. 统一换行符
    text = text.replace('\r\n', '\n').replace('\r', '\n')
    # 3. 去除连续空行
    text = re.sub(r'\n\s*\n', '\n\n', text)
    # 4. 去除行首行尾空格
    lines = [line.strip() for line in text.split('\n')]
    text = '\n'.join(lines)
    # 5. 去除连续空格
    text = re.sub(r'[ \t]+', ' ', text)
    # 6. 去除首尾空白
    text = text.strip()
    return text

try:
    from rag.secrets_loader import load_secrets
    from rag import config_data as config
except ImportError:
    from secrets_loader import load_secrets
    import config_data as config

load_secrets()
os.makedirs(config.KNOWLEDGE_PERSISTENT_DIR, exist_ok=True)


def check_md5(md5_str: str):
    if not os.path.exists(config.KNOWLEDGE_BASE_TXT):
        open(config.KNOWLEDGE_BASE_TXT, 'w', encoding='utf-8').close()
        return False

    else:
        for line in open(config.KNOWLEDGE_BASE_TXT, 'r', encoding='utf-8').readlines():
            if line.strip() == md5_str:
                return True

        return False


def save_md5(input_str: str):

    with open(config.KNOWLEDGE_BASE_TXT, 'a', encoding='utf-8') as f:
        f.write(input_str + '\n')


def get_string_md5(input_str: str):
    return hashlib.md5(input_str.encode('utf-8')).hexdigest()


class KnowledgeBaseService(object):

    def __init__(self):
        self.chroma = Chroma(
            collection_name=config.KNOWLEDGE_BASE_COLLECTION_NAME,
            embedding_function=DashScopeEmbeddings(),
            persist_directory=config.KNOWLEDGE_PERSISTENT_DIR,
        )
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=config.chunk_size,
            chunk_overlap=config.chunk_overlap,
            separators=config.separators,
            length_function=len,
        )

    def upload_by_str(self, input_str: str, filename: str):
        # 先清洗文本
        input_str = clean_text(input_str)

        if not input_str:
            return f"{filename} 内容为空，添加失败。"

        md5_str = get_string_md5(input_str)
        if check_md5(md5_str):
            return f"{filename} 已经存在。"

        if len(input_str) > config.chunk_size:
            knowledge_chunks = self.splitter.split_text(input_str)
        else:
            knowledge_chunks = [input_str]

        metadata = {
            "source": filename,
            "create_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "operator": "cc",
        }

        self.chroma.add_texts(knowledge_chunks, metadatas=[metadata for _ in knowledge_chunks])

        save_md5(md5_str)

        return f"{filename} 添加成功（{len(knowledge_chunks)} 个分块）。"


if __name__ == '__main__':
    knowledge_base_service = KnowledgeBaseService()
    res = knowledge_base_service.upload_by_str("周杰伦", "zhoujielun")
    print(res)
