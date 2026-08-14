import os
import json

APP_PATHS = [
    r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs",
    os.path.expandvars(r"%APPDATA%\Microsoft\Windows\Start Menu\Programs")
]

apps = {}


def scan_apps():
    global apps
    apps = {}

    for folder in APP_PATHS:
        if not os.path.exists(folder):
            continue

        for root, dirs, files in os.walk(folder):
            for file in files:
                if file.endswith(".lnk") or file.endswith(".exe"):
                    name = os.path.splitext(file)[0].lower()
                    apps[name] = os.path.join(root, file)

    with open("apps.json", "w") as f:
        json.dump(apps, f, indent=4)

    print(f"Found {len(apps)} applications.")


def load_apps():
    global apps

    if os.path.exists("apps.json"):
        with open("apps.json", "r") as f:
            apps = json.load(f)
    else:
        scan_apps()