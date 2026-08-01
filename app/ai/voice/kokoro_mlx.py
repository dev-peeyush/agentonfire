import asyncio
import numpy as np
from kokoro_mlx import KokoroTTS


class KokoroMLX:
    def __init__(self):
        # Loads once, reused across all requests (same pattern as before)
        self.tts = KokoroTTS.from_pretrained("mlx-community/Kokoro-82M-bf16")

    async def text_to_voice(self, response: str):
        """
        Async generator yielding raw PCM16 bytes, chunk by chunk.
        Mirrors your original PyTorch-based generator's output format exactly.
        """
        loop = asyncio.get_event_loop()
        queue: asyncio.Queue = asyncio.Queue()
        SENTINEL = object()

        def _produce():
            # generate_stream is sync + CPU/GPU-bound (MLX), so it runs in a thread
            try:
                for chunk in self.tts.generate_stream(
                    response,
                    voice="af_alloy",
                    sample_rate=24000,
                ):
                    # chunk is a float32 numpy array in [-1, 1]
                    pcm = (
                        np.clip(chunk, -1.0, 1.0) * 32767.0
                    ).round().astype(np.int16).tobytes()
                    asyncio.run_coroutine_threadsafe(queue.put(pcm), loop)
            finally:
                asyncio.run_coroutine_threadsafe(queue.put(SENTINEL), loop)

        loop.run_in_executor(None, _produce)

        while True:
            item = await queue.get()
            if item is SENTINEL:
                break
            yield item