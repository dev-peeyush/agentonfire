from unittest import case

from kokoro import KPipeline
from app.core.config import settings
from app.ai.voice.kokoro import Kokoro as kokoro
from app.ai.voice.kokoro_mlx import KokoroMLX as kokoro_mlx

class VoiceService:
    def __init__(self):
        self.pipeline = KPipeline(lang_code='a', repo_id='hexgrad/Kokoro-82M')
        self.kokoro = kokoro()
        self.kokoro_mlx = kokoro_mlx()

    async def text_to_voice(self, response:str):
        
        print(f"Using voice model: {settings.VOICE_MODEL}")
        match settings.VOICE_MODEL:
            case 'kokoro':
                async for chunk in self.kokoro.text_to_voice(response):
                    yield chunk
            case 'kokoro_mlx':
                async for chunk in self.kokoro_mlx.text_to_voice(response):
                    yield chunk
            case _:
                raise ValueError(f"Unsupported voice model: {settings.VOICE_MODEL}")
        
        # generator = self.pipeline(response, voice='af_alloy')
        # for i, (gs, ps, audio) in enumerate(generator):
        #     print(i, gs, ps)
        #     pcm = (
        #             audio
        #             .clamp(-1, 1)
        #             .mul(32767)
        #             .round()
        #             .short()
        #             .cpu()
        #             .numpy()
        #             .tobytes()
        #         )
        
        #     yield pcm


