from langchain.chat_models import init_chat_model


def chat_model(model='gpt-4o-mini', model_provider='openai', temperature=0.1):
    return init_chat_model(
        model=model,
        model_provider=model_provider,
        temperature = temperature
    )
    