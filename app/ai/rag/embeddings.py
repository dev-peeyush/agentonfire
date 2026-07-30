from langchain_openai.embeddings import OpenAIEmbeddings
from app.core.config import settings
from functools import lru_cache


class EmbeddingService:
    def __init__(self):
        self.embedding = OpenAIEmbeddings(
            model= settings.EMBEDDING_MODEL
        )
    
    @property
    def client(self):
        return self.embedding
    
    def embed_query(self, text: str):
        return self.embedding.embed_query(text)
    
    def embed_document(self, doucments: list[str]):
        return self.embedding.embed_documents(doucments)
    
@lru_cache(maxsize=1)
def get_embedding_service()->EmbeddingService:
    return EmbeddingService()