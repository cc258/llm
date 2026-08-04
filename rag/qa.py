import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
from rag.rag import RagService
from rag.knowledage_base import KnowledgeBaseService

# —— 页面配置 ——
st.set_page_config(page_title="AI", layout="wide")


# —— 初始化服务 ——
@st.cache_resource
def init_services():
    return RagService(), KnowledgeBaseService()

rag_service, kb_service = init_services()

if "messages" not in st.session_state:
    st.session_state.messages = []

# —— 左侧栏：知识库管理 ——
with st.sidebar:
    st.header("知识库管理")

    tab1, tab2 = st.tabs(["手动输入", "上传文件"])

    with tab1:
        manual_text = st.text_area("知识内容", height=120)
        manual_name = st.text_input("知识名称", value="手动输入")
        if st.button("上传文本", use_container_width=True, type="primary") and manual_text:
            with st.spinner("上传中..."):
                res = kb_service.upload_by_str(manual_text, manual_name)
            st.success(res)

    with tab2:
        uploaded = st.file_uploader("选择文件", type=["txt", "csv"])
        if uploaded:
            content = uploaded.read().decode("utf-8-sig")
            if st.button("上传文件", use_container_width=True, type="primary"):
                with st.spinner("上传中..."):
                    res = kb_service.upload_by_str(content, uploaded.name)
                st.success(res)

# —— 右侧主区域：聊天 ——
st.title("AI问答")

st.markdown("---")

# 欢迎语
if not st.session_state.messages:
    st.info("你好！请在左侧上传知识库，然后开始提问吧")

# 历史对话
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# 用户输入
prompt = st.chat_input("输入你的问题...")

if prompt:
    st.chat_message("user").write(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.spinner("正在思考..."):
        try:
            res = rag_service.ask(prompt)
        except Exception as e:
            res = f"出错了：{e}"

    st.chat_message("assistant").write(res)
    st.session_state.messages.append({"role": "assistant", "content": res})
