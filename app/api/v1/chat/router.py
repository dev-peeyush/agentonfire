from fastapi import APIRouter, Request, Depends
from app.api.v1.chat.service import ChatService
from app.api.v1.chat.schemas import ChatInitRequest


router = APIRouter(prefix='/chat', tags=['Chat'])

@router.post('/init')
async def init_chat(request:ChatInitRequest, chat_service: ChatService = Depends()):
    return await chat_service.init_chat(request=request)
