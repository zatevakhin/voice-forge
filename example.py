# pip install sounddevice
import sounddevice as sd

from voice_forge import PiperTts

# NOTE: Voices availbe here https://huggingface.co/rhasspy/piper-voices/tree/main
MODEL_NAME = "en_US-amy-medium"
MODELS_PATH = "models/"


if __name__ == "__main__":
    tts = PiperTts(MODEL_NAME, MODELS_PATH)

    input_text = "Hello, World!"
    data, samplerate = tts.synthesize_stream(input_text)

    sd.play(data, samplerate=samplerate, blocking=True)
