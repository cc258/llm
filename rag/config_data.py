import os

# 当前文件所在目录的绝对路径
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

EMBEDDING_MODEL_NAME = 'qwen3.8-max'
KNOWLEDGE_BASE_TXT = os.path.join(BASE_DIR, 'md5.txt')
KNOWLEDGE_BASE_COLLECTION_NAME = 'rag'
KNOWLEDGE_PERSISTENT_DIR = os.path.join(BASE_DIR, 'chroma_db')
os.makedirs(KNOWLEDGE_PERSISTENT_DIR, exist_ok=True)

chunk_size = 150
chunk_overlap = 30
separators = ['\n\n', '\n', '。', '！', '？', '!', '?', '.', ' ', '']
