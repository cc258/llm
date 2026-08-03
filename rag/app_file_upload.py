import time
import streamlit as st
from knowledage_base import KnowledgeBaseService


st.title("RAG 知识库更新")

uploaded_file = st.file_uploader("上传文件", type=["txt"], accept_multiple_files=False)

# st.session_state 状态管理

if "service" not in st.session_state:
    st.session_state["service"] = KnowledgeBaseService()

if uploaded_file is not None:
    filename = uploaded_file.name
    text = uploaded_file.read().decode('utf-8')


    st.write(f"文件名: {filename}")
    st.write(f"文件类型: {uploaded_file.type}")
    st.write(f"文件大小: {uploaded_file.size} 字节")
    st.write(f"文件内容: {text}")

    with st.spinner("上传知识库中。。。。。。"):
        time.sleep(1)
        res = st.session_state["service"].upload_by_str(text, filename)
        st.subheader(res)

