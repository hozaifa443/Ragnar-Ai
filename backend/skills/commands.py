import os
import webbrowser
import subprocess


def open_program(paths):
    """Try multiple executable paths."""
    for path in paths:
        if os.path.exists(path):
            subprocess.Popen(path)
            return True
    return False


def execute_command(command):
    print(">>> execute_command() called")
    print(">>>", repr(command))
    command = command.lower().strip()

    print(f"[COMMAND] Received: {command}")

    # ---------------- Websites ---------------- #

    if "chrome" in command:
        print("[DEBUG] Opening Chrome...")

        chrome_paths = [
            r"C:\Program Files\Google\Chrome\Application\chrome.exe",
            r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
            os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe"),
        ]

        if open_program(chrome_paths):
            return "Opening Chrome, Sir."

        webbrowser.open("https://google.com")
        return "Chrome not found. Opening Google in your default browser."

    elif "youtube" in command:
        webbrowser.open("https://youtube.com")
        return "Opening YouTube, Sir."

    elif "gmail" in command:
        webbrowser.open("https://mail.google.com")
        return "Opening Gmail, Sir."

    elif "chatgpt" in command:
        webbrowser.open("https://chat.openai.com")
        return "Opening ChatGPT, Sir."

    elif "canva" in command:
        webbrowser.open("https://www.canva.com")
        return "Opening Canva, Sir."

    elif "whatsapp" in command:
        webbrowser.open("https://web.whatsapp.com")
        return "Opening WhatsApp, Sir."

    # ---------------- Windows Apps ---------------- #

    elif "calculator" in command or "calc" in command:
        subprocess.Popen("calc.exe")
        return "Opening Calculator."

    elif "notepad" in command:
        subprocess.Popen("notepad.exe")
        return "Opening Notepad."

    elif "paint" in command:
        subprocess.Popen("mspaint.exe")
        return "Opening Paint."

    elif "command prompt" in command or "cmd" in command:
        subprocess.Popen("cmd.exe")
        return "Opening Command Prompt."

    elif "file explorer" in command or "explorer" in command:
        subprocess.Popen("explorer.exe")
        return "Opening File Explorer."

    elif "task manager" in command:
        subprocess.Popen("taskmgr.exe")
        return "Opening Task Manager."

    elif "settings" in command:
        os.system("start ms-settings:")
        return "Opening Settings."

    elif "recycle bin" in command:
        subprocess.Popen("explorer.exe shell:RecycleBinFolder", shell=True)
        return "Opening Recycle Bin."

    # ---------------- Core Temp ---------------- #

    elif "core temp" in command:

        core_temp_paths = [
            r"C:\Program Files\Core Temp\Core Temp.exe",
            r"C:\Program Files (x86)\Core Temp\Core Temp.exe",
        ]

        if open_program(core_temp_paths):
            return "Opening Core Temp."

        return "Core Temp is not installed."

    # ---------------- Windows ---------------- #

    elif "start menu" in command:
        os.system(
            'powershell -command "(New-Object -ComObject WScript.Shell).SendKeys(\'^{ESC}\')"'
        )
        return "Opening Start Menu."

    elif "lock screen" in command:
        os.system("rundll32.exe user32.dll,LockWorkStation")
        return "Locking your computer, Sir."

    return None