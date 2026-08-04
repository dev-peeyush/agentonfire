import whisper
from app.core.config import settings

class WhisperService:

    def __init__(self):
        self.model = whisper.load_model(settings.WHISPER_MODEL)

    def transcribe(
        self,
        audio: any
    ) -> str:

        result = self.model.transcribe(audio)

        print(f"Transcription result: {result}")
        return result["text"].strip()