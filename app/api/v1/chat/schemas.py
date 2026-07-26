from pydantic import BaseModel

class ChatInitRequest(BaseModel):
    access_token:str