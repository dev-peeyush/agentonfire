from pathlib import Path
from app.ai.rag.embeddings import get_embedding_service
from langchain_community.vectorstores import FAISS
from app.core.config import settings

class VectorStoreService:
    def __init__(
        self, 
        user_id: str):
        self.db_path = Path(str(f'{settings.FAISS_INDEX_PATH}/{user_id}'))
        self.embedding = get_embedding_service().client
        
    def create(self, documents):
        vector_store = FAISS.from_documents(
            documents=documents, 
            embedding=self.embedding
        )
        self.save(vector_store)
        return vector_store
    
    def load(self):
        if not self.exists():
            return None
        
        return FAISS.load_local(
            str(self.db_path),
            self.embedding,
            allow_dangerous_deserialization=True
        )
    
    def save(self, vector_store: FAISS):
        self.db_path.mkdir(parents=True, exist_ok=True)
        vector_store.save_local(str(self.db_path))
        
    def exists(self):
        return (
            self.db_path / 'index.faiss'
        ).exists()
        
    def similarity_search(
        self, 
        query:str,
        k: int = 4
    ): 
        vector_store = self.load()
        
        if vector_store is None:
            raise ValueError('Vector Store not found')
        return vector_store.similarity_search(
            query=query,
            k=k
        )
        
    def add_documents(
        self, 
        documents
    ):
        vector_store = self.load()
        
        if vector_store is None:
            vector_store = self.create(documents=documents)
        
        else: 
            vector_store.add_documents(documents=documents) 
            self.save(vector_store=vector_store)
    
        return vector_store