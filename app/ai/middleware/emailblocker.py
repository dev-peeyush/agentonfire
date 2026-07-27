from langchain.agents.middleware import PIIMiddleware


email_blocker = PIIMiddleware(
    'email',
    strategy='block',
    apply_to_input=True,
    apply_to_output=True,
)