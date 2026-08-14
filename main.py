from backend.voice.listen import listen
from backend.voice.speak import speak

from backend.ai.brain import ask_ragnar

from backend.skills.commands import execute_command
from backend.skills.internet import search_web

print("🤖 Ragnar Online")
speak("Hello, Sir. Ragnar is online.")

internet_keywords = [
    "today",
    "latest",
    "news",
    "weather",
    "ipl",
    "score",
    "price",
    "bitcoin",
    "stock",
    "who won"
]

while True:

    user = listen()

    if not user:
        continue

    user = user.strip()

    print(f"\n🧑 You: {user}")

    # Exit
    if user.lower() in ["exit", "quit", "goodbye"]:
        reply = "Goodbye, Sir. Have a great day."
        print(f"🤖 Ragnar: {reply}")
        speak(reply)
        break

    # Check built-in commands
    result = execute_command(user)

    if result:
        print(f"🤖 Ragnar: {result}")
        speak(result)
        continue

    # Internet search
    if any(word in user.lower() for word in internet_keywords):

        print("🌐 Searching Internet...")

        speak("Searching the internet, Sir.")

        try:
            reply = search_web(user)
        except Exception as e:
            print("Internet Error:", e)
            reply = "Sorry Sir, I couldn't search the internet."

    else:
        # Local AI
        reply = ask_ragnar(user)

    print(f"\n🤖 Ragnar: {reply}")
    speak(reply)