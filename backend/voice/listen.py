import whisper
import sounddevice as sd
from scipy.io.wavfile import write

# Load Whisper model only once
model = whisper.load_model("base")

def listen():
    fs = 16000
    duration = 5  # seconds

    print("🎤 Listening...")

    recording = sd.rec(
        int(duration * fs),
        samplerate=fs,
        channels=1,
        dtype="int16"
    )

    sd.wait()

    write("voice.wav", fs, recording)

    result = model.transcribe("voice.wav")

    text = result["text"]

    print("You:", text)

    return text