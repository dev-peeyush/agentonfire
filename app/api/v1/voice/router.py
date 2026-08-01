from fastapi import APIRouter, UploadFile, Depends, HTTPException
from fastapi.responses import StreamingResponse

from app.api.v1.voice.schemas import TextToVoiceRequest
from app.core.deps import get_current_user
from app.api.v1.voice.service import VoiceService

router = APIRouter(tags=["Voice AI Agent"])
voice_service = VoiceService()

@router.post('/text_to_voice')
async def text_to_voice(request:TextToVoiceRequest, user = Depends(get_current_user)):
    # return {"message": "Text to voice conversion successful", "text": 'Peeyush is back.'}
    return StreamingResponse(
        voice_service.text_to_voice(request.text),
        media_type='application/octet-stream'
    )