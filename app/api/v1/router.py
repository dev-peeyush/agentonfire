from fastapi import APIRouter
from app.db.engine import get_db
from app.api.v1.auth.router import router as auth_router
from app.api.v1.chat.router import router as chat_router
from app.api.v1.rag.router import router as rag_router
from app.api.v1.voice.router import router as voice_router

router = APIRouter()
router.include_router(auth_router)
router.include_router(chat_router)
router.include_router(rag_router)
router.include_router(voice_router)