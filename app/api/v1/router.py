from fastapi import APIRouter, Depends
from app.db.engine import get_db
from app.api.v1.auth.router import router as auth_router
from app.api.v1.chat.router import router as chat_router


router = APIRouter()
router.include_router(auth_router)
router.include_router(chat_router)