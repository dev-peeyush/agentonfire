from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from functools import lru_cache

class ChunkingService:

    def __init__(
        self, 
        chunk_size:int=1000,
        chunk_overlap:int = 200
    ):
        self._splitter = RecursiveCharacterTextSplitter(
            chunk_size = chunk_size,
            chunk_overlap = chunk_overlap,
            separators=[
                "\n\n",
                "\n",
                ". ",
                " ",
                ""
            ]
        )
    
    def split_documents(
        self, 
        documents: list[Document]
    ) -> list[Document]:
        return self._splitter.split_documents(documents=documents)
    
    
@lru_cache(maxsize=1)
def get_chunking_service() -> ChunkingService:
    return ChunkingService()
        