import customtkinter as ctk
from theme import *

class ChatFrame(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(
            master,
            fg_color=CHAT
        )

        # Chat display
        self.chatbox = ctk.CTkTextbox(
            self,
            fg_color="#111827",
            text_color=TEXT,
            font=TEXT_FONT,
            corner_radius=15,
            wrap="word"
        )

        self.chatbox.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=(15,10)
        )

        # Bottom input area
        bottom = ctk.CTkFrame(
            self,
            fg_color=CHAT
        )

        bottom.pack(fill="x", padx=15, pady=10)

        # Text input
        self.entry = ctk.CTkEntry(
            bottom,
            height=45,
            placeholder_text="Ask Ragnar anything...",
            font=TEXT_FONT
        )

        self.entry.pack(
            side="left",
            fill="x",
            expand=True,
            padx=(0,10)
        )

        # Microphone button
        self.mic = ctk.CTkButton(
            bottom,
            text="🎤",
            width=50,
            height=45
        )

        self.mic.pack(side="left", padx=(0,10))

        # Send button
        self.send = ctk.CTkButton(
            bottom,
            text="➜",
            width=60,
            height=45,
            fg_color=BUTTON
        )

        self.send.pack(side="right")

    def add_message(self, sender, message):

        self.chatbox.insert(
            "end",
            f"\n{sender}\n"
        )

        self.chatbox.insert(
            "end",
            f"{message}\n\n"
        )

        self.chatbox.see("end")