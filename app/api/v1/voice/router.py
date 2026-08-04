from fastapi import APIRouter, UploadFile, Depends, HTTPException
from fastapi.responses import StreamingResponse

from app.api.v1.voice.schemas import TextToVoiceRequest
from app.core.deps import get_current_user, get_whisper_service
from app.api.v1.voice.service import VoiceService
import soundfile as sf
import numpy as np
from app.ai.voice.transcribe.whisper_service import WhisperService

router = APIRouter(tags=["Voice AI Agent"])
voice_service = VoiceService()

@router.post('/text_to_voice')
async def text_to_voice(request:TextToVoiceRequest, user = Depends(get_current_user)):
    # return {"message": "Text to voice conversion successful", "text": 'Peeyush is back.'}
    return StreamingResponse(
        voice_service.text_to_voice(request.text),
        media_type='application/octet-stream'
    )
    
    
@router.post('/voice_to_text')
async def voice_to_text(file: UploadFile, user = Depends(get_current_user), whisper_service: WhisperService = Depends(get_whisper_service)):
    if not file.filename.endswith(('.wav', '.mp3', '.m4a')):
        raise HTTPException(status_code=400, detail="Invalid file type. Only .wav, .mp3, and .m4a are supported.")
    
    
    audio, sr = sf.read(file.file)
    audio = audio.astype(np.float32)

    print(f"Audio shape: {audio.shape}, Sample rate: {sr}")
    transcribed_text = whisper_service.transcribe(audio)
    return {"transcribed_text": transcribed_text}