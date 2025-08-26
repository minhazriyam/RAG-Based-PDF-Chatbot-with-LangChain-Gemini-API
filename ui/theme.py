import streamlit as st

def inject_global_css():
    st.markdown("""
    <style>
      /* global resets */
      .block-container { 
        padding-top: 2rem; 
        padding-bottom: 2rem;
        max-width: 1050px; 
      }
      header[data-testid="stHeader"] { background: transparent; }
      /* top title area */
      .app-title {
        display:flex; align-items:center; gap:12px;
        padding: 10px 14px; border-radius: 14px;
        background: linear-gradient(135deg, rgba(124,92,255,.15), rgba(0,0,0,0));
        border: 1px solid rgba(124,92,255,.25);
        margin-bottom: 10px;
      }
      .app-title h1 { margin: 0; font-size: 1.5rem; }
      .subtle { color: #9aa1b3; font-size: .95rem; }

      /* card */
      .card {
        background: var(--secondary-background-color, #171a2a);
        border: 1px solid rgba(255,255,255,.06);
        border-radius: 16px;
        padding: 16px 18px;
      }

      /* chat */
      .chat {
        display:flex; gap:12px; margin: 10px 0 14px 0;
      }
      .chat .avatar {
        width: 42px; height: 42px; border-radius: 50%;
        display:flex; align-items:center; justify-content:center;
        background:#22263a; border:1px solid rgba(255,255,255,.08);
        font-weight:700;
      }
      .chat .bubble {
        flex:1; padding:14px 16px; border-radius: 14px;
        border: 1px solid rgba(255,255,255,.06);
      }
      .chat.user .bubble { background:#1a1f34; }
      .chat.bot  .bubble { background:#20263d; }
      .meta { color:#9aa1b3; font-size:.8rem; margin-top:6px; }

      /* pills */
      .pill {
        display:inline-flex; align-items:center; gap:8px;
        padding:6px 10px; border-radius:999px; font-size:.85rem;
        background:#1a1f34; border:1px solid rgba(255,255,255,.08);
        color:#cfd3e2;
      }

      /* sidebar polish */
      section[data-testid="stSidebar"] {
        border-right: 1px solid rgba(255,255,255,.08);
      }
      .side-card { padding:12px; border-radius:12px; border:1px solid rgba(255,255,255,.06); background:#14182a; }
      .side-title { font-weight:700; margin-bottom:.4rem; }
      .muted { color:#9aa1b3; }

      /* buttons (keep Streamlit behavior, just nicer) */
      div.stButton > button {
        width: 100%;
        border-radius: 12px;
        border:1px solid rgba(255,255,255,.12);
      }
      /* input */
      div[data-baseweb="input"] input {
        border-radius: 12px !important;
      }
    </style>
    """, unsafe_allow_html=True)
