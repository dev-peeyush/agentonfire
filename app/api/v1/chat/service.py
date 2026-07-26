from app.api.v1.chat.schemas import ChatInitRequest

class ChatService:
    
    async def init_chat(self, request:ChatInitRequest):
        return request.access_token