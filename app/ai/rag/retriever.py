from langchain_core.documents import Document
from app.ai.rag.vector_store import VectorStoreService
class RetrieverService:
    
    def __init__(self, user_id:str):
        self.vector_store = VectorStoreService(user_id=user_id)

    def search(self, query: str)->list[Document]:
        return self.vector_store.similarity_search(query=query)