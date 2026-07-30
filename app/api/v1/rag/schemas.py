from pydantic import BaseModel

class VectorQueryRequest(BaseModel):
    query:str