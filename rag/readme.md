# RAG


# 运行
```
uv run streamlit run qa.py
```

# 清除历史

```
rm -rf chroma_db md5.txt
```

# Dependencies

```
uv add streamlit dashscope langchain_community langchain_chroma chromadb openai
```


# 离线流程

- User > 
- WEB文件上传页面 > 
- app_file_upload【上传页面】 > 
- knowledge_base【知识库存储逻辑】 > 
- Chroma向量库


### 前后端一起运行

```
uv run streamlit run app_file_upload.py
```


### [因为启动的是Streamlit, 所以不需要再运行] knowledge

```
uv run python knowledage_base.py
```


# 在线流程

chain查询向量库，再问大模型


### 流程

向量库
vector_stores

执行链
rag

历史对话
file_history_store

三个糅合到一个chain中，执行，回答用户。

```
uv run python vector_stores.py
uv run python rag.py
uv run python file_history_store.py
```

都能看到对应的回答







