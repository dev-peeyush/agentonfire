from fastapi import APIRouter, UploadFile, Depends, HTTPException
from pathlib import Path
from app.ai.rag.loaders.pdf_loader import PDFLoaderService
from app.ai.rag.ingest import IngestionService
from app.ai.rag.retriever import RetrieverService
from app.api.v1.rag.schemas import VectorQueryRequest
from app.core.deps import get_current_user
import shutil

router = APIRouter(tags=["Data Ingestion"])
UPLOAD_DIR = Path("storage/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

@router.post('/ingest_pdf')
def ingest_pdf(upload_file: UploadFile, current_user = Depends(get_current_user)):
    
    if upload_file.content_type != 'application/pdf':
        raise HTTPException(
            status_code=400,
            detail='Only Pdf files are supported'
        )
    file_path = UPLOAD_DIR / upload_file.filename
    
    with open(file_path, 'wb') as buffer:
        shutil.copyfileobj(upload_file.file, buffer)
    
    # file_path = UPLOAD_DIR / 'test.pdf'
    pdf_service = PDFLoaderService()
    documents = pdf_service.load(file_path)
    ingest = IngestionService(user_id=current_user.id)
    print(f"total documents: {len(documents)}")
    return ingest.ingest(documents=documents)

@router.post('/search_pdf')
def search_pdf(request: VectorQueryRequest, current_user = Depends(get_current_user)):
    
    retriever_service = RetrieverService(user_id=current_user.id)
    return retriever_service.search(query=request.query)
