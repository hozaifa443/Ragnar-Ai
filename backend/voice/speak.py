import pyttsx3

def speak(text):
    engine = pyttsx3.init()

    engine.setProperty("rate", 170)

    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[0].id)

    engine.say(text)
    engine.runAndWait()

    engine.stop()