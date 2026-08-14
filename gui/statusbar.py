import customtkinter as ctk
import psutil

class StatusBar(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(master, height=40)

        self.label = ctk.CTkLabel(
            self,
            text=""
        )

        self.label.pack(pady=8)

        self.update_status()

    def update_status(self):

        cpu = psutil.cpu_percent()

        ram = psutil.virtual_memory().percent

        self.label.configure(
            text=f"🟢 Online    CPU {cpu}%    RAM {ram}%"
        )

        self.after(
            1000,
            self.update_status
        )