import streamlit as st
from rag.rag import RagService
from rag.knowledage_base import KnowledgeBaseService

st.title("智能客服")
st.divider()

# 初始化服务
if "RagService" not in st.session_state:
    st.session_state.RagService = RagService()
if "KnowledgeBaseService" not in st.session_state:
    st.session_state.KnowledgeBaseService = KnowledgeBaseService()
if "messages" not in st.session_state:
    st.session_state.messages = []

# —— 上传知识区域 ——
with st.expander("上传知识", expanded=False):
    tab1, tab2 = st.tabs(["上传文件", "手动输入"])

    with tab1:
        uploaded = st.file_uploader("选择 txt/csv 文件", type=["txt", "csv"])
        if uploaded and st.button("上传文件"):
            content = uploaded.read().decode("utf-8-sig")
            res = st.session_state.KnowledgeBaseService.upload_by_str(content, uploaded.name)
            st.success(res)

    with tab2:
        manual_text = st.text_area("输入知识: (如：我是大帅)")
        if st.button("上传文本") and manual_text:
            res = st.session_state.KnowledgeBaseService.upload_by_str(manual_text, "手动输入")
            st.success(res)

st.divider()

# 显示历史对话
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# 用户输入
prompt = st.chat_input()

if prompt:
    st.chat_message("user").write(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.spinner("AI is thinking..."):
        res = st.session_state.RagService.ask(prompt)

    st.chat_message("assistant").write(res)
    st.session_state.messages.append({"role": "assistant", "content": res})
