import customtkinter as ctk
from theme import *

class Sidebar(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(
            master,
            width=220,
            fg_color=SIDEBAR,
            corner_radius=0
        )

        self.pack_propagate(False)

        # Logo
        logo = ctk.CTkLabel(
            self,
            text="🤖 RAGNAR",
            font=TITLE_FONT,
            text_color=TEXT
        )
        logo.pack(pady=(30, 40))

        buttons = [
            "💬 Chat",
            "🧠 Memory",
            "🌐 Internet",
            "📂 Applications",
            "📄 Documents",
            "⚙ Settings"
        ]

        for name in buttons:

            btn = ctk.CTkButton(
                self,
                text=name,
                height=42,
                fg_color="transparent",
                hover_color="#1e293b",
                anchor="w",
                font=TEXT_FONT
            )

            btn.pack(fill="x", padx=15, pady=6)

        # Bottom Label
        version = ctk.CTkLabel(
            self,
            text="Ragnar v1.0",
            text_color=SUBTEXT,
            font=("Segoe UI", 11)
        )

        version.pack(side="bottom", pady=20)