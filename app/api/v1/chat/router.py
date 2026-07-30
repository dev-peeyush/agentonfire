from fastapi import APIRouter, Request, Depends
from app.api.v1.chat.service import ChatService
from app.api.v1.chat.schemas import ChatPayload
from app.core.deps import get_current_user,get_chat_agent


router = APIRouter(prefix='/chat', tags=['AI Chat Agent'])

chat_agent = Depends(get_chat_agent)
@router.post('/chat')
async def chat(request: ChatPayload, chat_agent = Depends(get_chat_agent), get_current_user = Depends(get_current_user), chat_service: ChatService = Depends()):
    return await chat_service.message(request = request, user_data = get_current_user, chat_agent= chat_agent)
