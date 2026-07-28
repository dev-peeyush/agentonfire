from contextlib import asynccontextmanager
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.checkpoint.postgres.aio import AsyncPostgresSaver
from langgraph.checkpoint.redis import RedisSaver
from app.core.config import settings  # Adjust to your project path
from app.ai.agents.chat_agents import chat_agent

@asynccontextmanager
async def init_chat_agent():
    """
    Dynamically initializes LangGraph with Postgres, Redis, or In-Memory savers.
    Yields the fully compiled LangGraph agent instance to the caller.
    """
    # --- STRATEGY A: POSTGRESQL ---
    if settings.CHECKPOINTER_TYPE == "postgres" and settings.DATABASE_URI:
        async with AsyncPostgresSaver.from_conn_string(
            settings.DATABASE_URI
        ) as checkpointer:
            await checkpointer.setup()
            yield chat_agent(checkpointer=checkpointer)

    # --- STRATEGY B: REDIS ---
    elif settings.CHECKPOINTER_TYPE == "redis":
        # Pull your Redis Connection String (e.g., "redis://localhost:6379")
        
        # RedisSaver supports standard 'with' block syntax 
        # Note: An asynchronous wrapper context manager can map this perfectly
        with RedisSaver.from_conn_string(settings.REDIS_URI) as checkpointer:
            # Important: Initializes RediSearch & RedisJSON indices on first run
            checkpointer.setup()
            yield chat_agent(checkpointer=checkpointer)
    # --- STRATEGY C: IN-MEMORY FALLBACK ---
    else:
        print("💡 LangGraph: Initializing Clean In-Memory Saver (Testing Mode)")
        checkpointer = InMemorySaver()
        yield chat_agent(checkpointer=checkpointer)
