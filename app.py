import streamlit as st
from datetime import datetime

# --- runtime + session setup ---
from services.asyncio_fix import ensure_event_loop
ensure_event_loop()

from utils.session import init_state

# --- data / rag services ---
from services.pdf_loader import read_pdfs_to_text
from services.chunker import split_text
from services.embeddings import build_embeddings
from services.vectorstore import build_faiss_from_texts
from services.qa_chain import build_chain

# --- UI helpers ---
from ui.theme import inject_global_css
from ui.components import header, chat_message, side_card, download_history_button

# --- config ---
from config import RETRIEVAL_TOP_K

# ---------------- ui shell ----------------
st.set_page_config(page_title="RAG PDF Chatbot", page_icon="📚")
inject_global_css()
header("Chat with multiple PDFs", "Ask a question. I will answer from your uploaded documents only.")

# state
init_state()
model_name = "Google AI"

# ---------------- sidebar ----------------
side_card("Google API Key", "Get one at https://ai.google.dev/")
api_key = st.sidebar.text_input(" ", type="password", placeholder="Paste your Google API key", label_visibility="collapsed")

st.sidebar.markdown("### ")
side_card("Upload PDFs", "Drag & drop multiple files (up to 200 MB each).")
files = st.sidebar.file_uploader(" ", accept_multiple_files=True, label_visibility="collapsed")

col_a, col_b = st.sidebar.columns(2, gap="small")
with col_a:
    process_clicked = st.button("Submit & Process", use_container_width=True)
with col_b:
    reset_clicked = st.button("Reset", use_container_width=True)

# process PDFs -> build index once
if process_clicked:
    if not api_key:
        st.warning("Enter API key first.")
    elif not files:
        st.warning("Upload PDFs first.")
    else:
        with st.spinner("Indexing your PDFs..."):
            try:
                full_text = read_pdfs_to_text(files)
                chunks = split_text(full_text)
                emb = build_embeddings(api_key)
                vs = build_faiss_from_texts(chunks, emb)

                st.session_state.vector_store = vs
                st.session_state.embeddings = emb
                st.session_state.pdf_names = [f.name for f in files]
                st.success("Ready. Ask your question below!")
            except Exception as e:
                st.error(f"Failed to index PDFs: {e}")

# reset app state
if reset_clicked:
    st.session_state.clear()
    init_state()
    st.rerun()

# ---------------- main: query ----------------
user_q = st.text_input(
    "Ask a question about your PDFs",
    placeholder="e.g., What is machine learning?"
)

if user_q:
    if not api_key:
        st.warning("Enter API key first.")
    elif st.session_state.vector_store is None:
        st.warning("Upload and process PDFs first.")
    else:
        try:
            # retrieve relevant chunks
            docs = st.session_state.vector_store.similarity_search(user_q, k=RETRIEVAL_TOP_K)

            # build chain and ask
            chain = build_chain(api_key)
            out = chain(
                {"input_documents": docs, "question": user_q},
                return_only_outputs=True
            )["output_text"]

            # render current exchange
            chat_message("user", user_q)
            chat_message("bot", out)

            # record history
            st.session_state.conversation_history.append((
                user_q,
                out,
                model_name,
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                ", ".join(st.session_state.pdf_names),
            ))
        except Exception as e:
            st.error(f"Something went wrong while answering: {e}")

# ---------------- history + export ----------------
if st.session_state.conversation_history:
    st.markdown("### History")
    for q, a, _, ts, names in st.session_state.conversation_history:
        chat_message("user", q, meta=f"{ts} • {names}")
        chat_message("bot", a)

    download_history_button(st.session_state.conversation_history)
