from openwakeword.model import Model
import sounddevice as sd
import numpy as np

model = Model()

def wait_for_wake_word():
    print("👂 Waiting for wake word...")

    while True:
        audio = sd.rec(
            1280,
            samplerate=16000,
            channels=1,
            dtype="int16"
        )

        sd.wait()

        prediction = model.predict(audio.flatten())

        for name, score in prediction.items():

            if score > 0.5:
                print(f"Wake word detected: {name}")
                return