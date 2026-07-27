from langchain.agents.middleware import PIIMiddleware

creditcard_blocker = PIIMiddleware(
    'credit_card',
    strategy='block',
    apply_to_input=True,
    apply_to_output=True,
)