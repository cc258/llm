import os
from dotenv import load_dotenv


def load_secrets():
    """加载密钥：兼容本地 .env 和 Streamlit Cloud st.secrets"""
    # 1. 本地：加载 .env 文件
    env_path = os.path.join(os.path.dirname(__file__), '..', '.env')
    load_dotenv(env_path)

    # 2. Streamlit Cloud：从 st.secrets 读取并设置到环境变量
    try:
        import streamlit as st
        for key, value in st.secrets.items():
            os.environ.setdefault(key, str(value))
    except Exception:
        # 非 Streamlit 环境或没有 secrets
        pass
