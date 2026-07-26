import uvicorn
from app.core.config import settings
from fastapi import FastAPI
from app.api.router import api_router
from contextlib import asynccontextmanager
from app.ai.agents.chat_agents import chat_agent
from app.db.engine import db_engine
from app.db.base import Base

@asynccontextmanager
async def lifespan(app: FastAPI):
    print('server is up')
    
    Base.metadata.create_all(bind=db_engine)
    chat_agent()
    yield
    print('server shutting down')

app = FastAPI( lifespan= lifespan)
app.include_router(api_router, prefix="/api")
@app.get('/')
async def home():
    return "Home"

def main():
    uvicorn.run(
        'main:app',
        host=settings.HOST,
        port=settings.PORT,
        reload=True
    )


if __name__ == "__main__":
    main()
