import streamlit as st

def init_state():
    st.session_state.setdefault("conversation_history", [])
    st.session_state.setdefault("vector_store", None)
    st.session_state.setdefault("pdf_names", [])
    st.session_state.setdefault("embeddings", None)
