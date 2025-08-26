from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains.question_answering import load_qa_chain
from config import GOOGLE_CHAT_MODEL

PROMPT = """
Answer the question using only the provided context.
If the answer is not in the context, say: "answer is not available in the context".

Context:
{context}

Question:
{question}

Answer:
"""

def build_chain(api_key: str):
    llm = ChatGoogleGenerativeAI(
        model=GOOGLE_CHAT_MODEL, temperature=0.3, google_api_key=api_key
    )
    prompt = PromptTemplate(template=PROMPT, input_variables=["context", "question"])
    return load_qa_chain(llm, chain_type="stuff", prompt=prompt)
