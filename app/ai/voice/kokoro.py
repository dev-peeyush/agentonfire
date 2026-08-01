from kokoro import KPipeline


class Kokoro:

    def __init__(self):
        self.pipeline = KPipeline(lang_code='a', repo_id='hexgrad/Kokoro-82M')

    async def text_to_voice(self, response:str):
        generator = self.pipeline(response, voice='af_alloy')
        for i, (gs, ps, audio) in enumerate(generator):
            print(i, gs, ps)
            pcm = (
                    audio
                    .clamp(-1, 1)
                    .mul(32767)
                    .round()
                    .short()
                    .cpu()
                    .numpy()
                    .tobytes()
                )
        
            yield pcm