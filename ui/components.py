import streamlit as st
import base64
import pandas as pd

def header(title: str, caption: str = ""):
    st.markdown(f"""
      <div class="app-title">
        <span class="pill">📚 RAG</span>
        <h1>{title}</h1>
      </div>
      <div class="subtle">{caption}</div>
    """, unsafe_allow_html=True)

def chat_message(role: str, text: str, meta: str | None = None):
    icon = "🧑" if role == "user" else "🤖"
    st.markdown(f"""
      <div class="chat {role}">
        <div class="avatar">{icon}</div>
        <div style="flex:1">
          <div class="bubble">{text}</div>
          {f'<div class="meta">{meta}</div>' if meta else ''}
        </div>
      </div>
    """, unsafe_allow_html=True)

def side_card(title: str, body_md: str):
    st.sidebar.markdown(f"""
      <div class="side-card">
        <div class="side-title">{title}</div>
        <div class="muted">{body_md}</div>
      </div>
    """, unsafe_allow_html=True)

def download_history_button(rows):
    if not rows: 
        return
    df = pd.DataFrame(rows, columns=["Question","Answer","Model","Timestamp","PDF Name"])
    csv = df.to_csv(index=False).encode()
    b64 = base64.b64encode(csv).decode()
    st.sidebar.markdown(
        f'<a href="data:file/csv;base64,{b64}" download="conversation_history.csv">'
        f'<button>Download conversation history</button></a>',
        unsafe_allow_html=True
    )
