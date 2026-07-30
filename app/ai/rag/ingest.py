from langchain_community.document_loaders import PyPDFLoader
from app.ai.rag.chunking import get_chunking_service
from app.ai.rag.vector_store import VectorStoreService
from pathlib import Path
from langchain_core.documents import Document

class IngestionService:
    def __init__(self, user_id:str):
        self.chunk_service = get_chunking_service()
        self.vector_store = VectorStoreService(user_id=user_id)
        
        
    def ingest(self, documents:list[Document]):
        
        chunks = self.chunk_service.split_documents(documents=documents)
        print(f"total chunks: {len(chunks)}")
        self.vector_store.add_documents(chunks)
        
        return {
            "pages": len(documents),
            "chunks": len(chunks),
            "status": "success"
        }
        
    