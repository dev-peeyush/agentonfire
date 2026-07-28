from app.api.v1.chat.schemas import ChatPayload
from app.core.deps import BasicUserData
from app.ai.agents.chat_agents import chat_agent
from fastapi import HTTPException


class ChatService:
    
    async def message(self, request: ChatPayload, user_data:BasicUserData):
        
        agent = chat_agent()
        config = {
            'configurable':{
                'thread_id':str(user_data.id)
            }
        }
        try:
            response = agent.invoke({
                'messages':[
                    {
                        'role':'user',
                        'content': request.message
                    }
                ]
            }, config=config)
            return response['messages'][-1].content
        except Exception as e:
            raise HTTPException(
                status_code=400,
                detail=str(e)
            )