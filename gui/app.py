import sys
import os
import threading

# Allow app.py to import backend modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import customtkinter as ctk

from gui.theme import *
from gui.sidebar import Sidebar
from gui.chat import ChatFrame
from gui.statusbar import StatusBar

from backend.ai.brain import ask_ragnar
from backend.voice.listen import listen
from backend.voice.speak import speak

from backend.skills.commands import execute_command
from backend.skills.internet import search_web


ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


class RagnarApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("🤖 Ragnar AI")
        self.geometry("1300x800")

        # Sidebar
        self.sidebar = Sidebar(self)
        self.sidebar.pack(side="left", fill="y")

        # Right Panel
        self.right = ctk.CTkFrame(self)
        self.right.pack(side="right", fill="both", expand=True)

        # Chat
        self.chat = ChatFrame(self.right)
        self.chat.pack(fill="both", expand=True)

        # Status Bar
        self.status = StatusBar(self.right)
        self.status.pack(fill="x")

        # Events
        self.chat.send.configure(command=self.send_message)
        self.chat.mic.configure(command=self.voice_message)
        self.chat.entry.bind("<Return>", lambda e: self.send_message())

        # Welcome Message
        self.chat.add_message(
            "🤖 Ragnar",
            "Good evening, Sir. How may I assist you today?"
        )

        self.internet_keywords = [
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

    # -------------------------------------------------
    # COMMON RESPONSE LOGIC
    # -------------------------------------------------

    def get_response(self, text):

        # First execute desktop commands
        result = execute_command(text)

        if result:
            return result

        # Internet search
        if any(word in text.lower() for word in self.internet_keywords):
            return search_web(text)

        # AI Chat
        return ask_ragnar(text)

    # -------------------------------------------------
    # TEXT MESSAGE
    # -------------------------------------------------

    def send_message(self):

        text = self.chat.entry.get().strip()

        if not text:
            return

        self.chat.entry.delete(0, "end")

        self.chat.add_message("🧑 You", text)

        self.status.label.configure(text="🧠 Thinking...")

        threading.Thread(
            target=self.process_message,
            args=(text,),
            daemon=True
        ).start()

    def process_message(self, text):

        try:
            reply = self.get_response(text)

        except Exception as e:
            reply = f"Error: {e}"

        self.after(
            0,
            lambda: self.chat.add_message("🤖 Ragnar", reply)
        )

        self.after(
            0,
            lambda: self.status.label.configure(text="🔊 Speaking...")
        )

        speak(reply)

        self.after(
            0,
            lambda: self.status.label.configure(text="🟢 Ready")
        )

    # -------------------------------------------------
    # VOICE MESSAGE
    # -------------------------------------------------

    def voice_message(self):

        threading.Thread(
            target=self.process_voice,
            daemon=True
        ).start()

    def process_voice(self):

        self.after(
            0,
            lambda: self.status.label.configure(text="🎤 Listening...")
        )

        text = listen()

        if not text:
            self.after(
                0,
                lambda: self.status.label.configure(text="🟢 Ready")
            )
            return

        self.after(
            0,
            lambda: self.chat.add_message("🧑 You", text)
        )

        self.after(
            0,
            lambda: self.status.label.configure(text="🧠 Thinking...")
        )

        try:
            reply = self.get_response(text)

        except Exception as e:
            reply = f"Error: {e}"

        self.after(
            0,
            lambda: self.chat.add_message("🤖 Ragnar", reply)
        )

        self.after(
            0,
            lambda: self.status.label.configure(text="🔊 Speaking...")
        )

        speak(reply)

        self.after(
            0,
            lambda: self.status.label.configure(text="🟢 Ready")
        )


# -------------------------------------------------
# START APP
# -------------------------------------------------

if __name__ == "__main__":
    app = RagnarApp()
    app.mainloop()