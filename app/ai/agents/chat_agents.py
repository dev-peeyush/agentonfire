from langchain.agents import create_agent
from app.ai.models.chat_model import chat_model
from langgraph.checkpoint.memory import InMemorySaver, BaseCheckpointSaver
from app.ai.middleware.middlewares import middlewares
import dotenv
dotenv.load_dotenv()
def chat_agent(model = chat_model(), checkpointer: BaseCheckpointSaver = InMemorySaver() ):
    return create_agent(
        model=model,
        checkpointer=checkpointer,
        middleware=middlewares
    )
