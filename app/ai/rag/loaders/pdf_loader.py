from langchain_community.document_loaders import PyPDFLoader
from pathlib import Path
from langchain_core.documents import Document

class PDFLoaderService:
    
    def load(self, path:str) -> list[Document]:
        
        pdf_path = Path(path)
        
        if not pdf_path.exists():
            raise FileNotFoundError(pdf_path)
        
        loader = PyPDFLoader(pdf_path)
        return loader.load()
    