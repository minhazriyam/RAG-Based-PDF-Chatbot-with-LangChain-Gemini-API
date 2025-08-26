from langchain_google_genai import GoogleGenerativeAIEmbeddings
from config import GOOGLE_EMBED_MODEL

def build_embeddings(api_key: str):
    return GoogleGenerativeAIEmbeddings(
        model=GOOGLE_EMBED_MODEL, google_api_key=api_key
    )
