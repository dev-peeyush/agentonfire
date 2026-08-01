from pydantic import BaseModel

class TextToVoiceRequest(BaseModel):
    text: str