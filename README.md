# 🤖 Ragnar AI

Ragnar is a personal desktop AI assistant built with Python.

The goal of this project is to create a modern AI assistant that can communicate with the user through text and voice, answer questions using a local AI model, perform computer tasks, search the internet, and provide a modern desktop interface.

---

## ✨ Features

### 🧠 AI Conversations
- Ask questions through the desktop chat interface.
- AI-powered responses using Ollama.
- Local AI processing support.
- Multi-threaded response handling to keep the interface responsive.

### 🎤 Voice Assistant
- Voice input using speech recognition.
- Text-to-speech responses.
- Microphone support directly from the Ragnar desktop application.
- Wake word functionality for future hands-free interaction.

### 💻 Desktop Control
Ragnar can perform various computer tasks, including opening applications and websites.

Examples include:

- Open Google Chrome
- Open YouTube
- Open WhatsApp
- Open ChatGPT
- Open Canva
- Open Calculator
- Open Recycle Bin
- Open system tools
- Lock the computer

### 🌐 Internet Search
Ragnar can search the internet when information is not available locally.

### 💬 Modern Desktop Interface
The application includes:

- Modern dark-mode interface
- Sidebar navigation
- AI chat interface
- Microphone button
- Send message button
- Status indicators
- CPU and RAM usage display

### 🧠 Memory System
Ragnar includes a memory system for storing information and supporting future improvements in contextual conversations.

---

# 🏗️ Project Structure

```text
Ragnar/
│
├── main.py                     # Main application launcher
├── README.md                   # Project documentation
│
├── backend/
│   ├── ai/
│   │   ├── brain.py            # AI processing
│   │   ├── memory.py           # Memory system
│   │   └── intent.py           # Intent detection
│   │
│   ├── voice/
│   │   ├── listen.py           # Voice recognition
│   │   ├── speak.py            # Text-to-speech
│   │   └── wakeword.py         # Wake word detection
│   │
│   ├── skills/
│   │   ├── commands.py         # Computer commands
│   │   ├── launcher.py         # Application launching
│   │   ├── internet.py         # Internet search
│   │   └── system.py           # System utilities
│   │
│   └── utils/
│       └── router.py           # Request routing
│
├── gui/
│   ├── app.py                  # Main GUI
│   ├── chat.py                 # Chat interface
│   ├── sidebar.py              # Sidebar
│   ├── statusbar.py            # Status bar
│   └── theme.py                # Application theme
│
├── data/
│   ├── memory.json             # AI memory data
│   └── apps.json               # Application configuration
│
├── tests/                      # Testing files
│
└── assets/                     # Future icons, images and sounds
