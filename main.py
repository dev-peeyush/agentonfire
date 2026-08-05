import uvicorn
from app.core.config import settings
from fastapi import FastAPI, Request
from app.api.router import api_router
from contextlib import asynccontextmanager
from app.ai.agents.chat_agents import chat_agent
from app.db.engine import db_engine
from app.db.base import Base
from langgraph.checkpoint.postgres.aio import AsyncPostgresSaver
from app.core.config import settings
from app.ai.factory.agent_factory import init_chat_agent
from fastapi.templating import Jinja2Templates
from app.ai.voice.transcribe.whisper_service import WhisperService

@asynccontextmanager
async def lifespan(app: FastAPI):
    print('server is up')
    Base.metadata.create_all(bind=db_engine)
    
    async with init_chat_agent() as agent:
        app.state.chat_agent = agent
        
    app.state.whisper_service = WhisperService() 
    yield
 
    print('server shutting down')

app = FastAPI( lifespan= lifespan)
app.include_router(api_router, prefix="/api")

templates = Jinja2Templates(directory="templates")

@app.get('/')
async def home():
    return 'FastAPI is running!'

@app.get('/text_to_voice_web', description="This endpoint serves the text-to-voice conversion web page. Open the browser and navigate to http://localhost:8000/text_to_voice_web to access the page. You can enter text in the input field and click the 'Play' button to hear the AI's voice response. English is the only supported language for now.")
async def text_to_voice(request:Request):
    return templates.TemplateResponse(
        request=request,
        name="text_to_voice.html"
    )
    
@app.get('/voice_to_voice_web', description="This endpoint serves the voice-to-voice conversation web page. Open the browser and navigate to http://localhost:8000/voice_to_voice_web to access the page. You can upload an audio file (in .mp3 format) and click the 'Play' button to hear the AI's voice response based on the transcribed text from your audio input. English is the only supported language for now.")
async def voice_to_voice(request:Request):
    return templates.TemplateResponse(
        request=request,
        name="voice_to_voice.html"
    )

def main():
    uvicorn.run(
        'main:app',
        host=settings.HOST,
        port=settings.PORT,
        reload=True
    )


if __name__ == "__main__":
    main()
