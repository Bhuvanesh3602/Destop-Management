# 🖥️ Desktop-Management

A **local AI assistant / desktop manager** that accepts **text or voice input** and performs everyday desktop actions such as opening websites, telling the time, launching applications, and more.

The application uses a **Tkinter GUI when available** and automatically **falls back to a Command-Line Interface (CLI)** if GUI dependencies are missing.

---

## ✨ Features

- 🪟 GUI-first design with CLI fallback
- 🎤 Voice input using `SpeechRecognition` and `PyAudio`
- 🔊 Text-to-speech responses using `pyttsx3`
- 🧩 Easy-to-extend command system
- 🪶 Lightweight and fully local (no cloud APIs for TTS)
- 🌐 Open websites (YouTube, Google, Gmail, Facebook, Instagram, etc.)
- 📅 Get current time and date
- 💻 Launch applications (Notepad, Calculator, Terminal, WhatsApp)
- 🔍 Google search functionality
- 😄 Tell jokes
- ⚡ System commands (shutdown, restart, sleep)

---

## 📋 Requirements

- Python 3.8+
- Packages:
  - SpeechRecognition
  - pyttsx3
  - Pillow
  - PyAudio (required for microphone input)

---

## 🚀 Quick Install (Windows)

### Step 1: Create Virtual Environment
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### Step 2: Install Dependencies
```powershell
pip install -r requirements.txt
```

**Note:** If PyAudio installation fails, download the wheel file for Python 3.11:
- Download: `PyAudio-0.2.11-cp311-cp311-win_amd64.whl` from https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio
- Install: `pip install PyAudio-0.2.11-cp311-cp311-win_amd64.whl`

---

## 🎯 Usage

Run the app:
```powershell
python app.py
```

- **GUI Mode**: If `tkinter` and `Pillow` are installed, a GUI window opens
- **CLI Mode**: If `tkinter` is unavailable, runs in command-line mode
  - Type messages directly
  - Type `mic` to use microphone
  - Type `quit` to exit

---

## 🗣️ Voice Commands

### Greetings
- "Hello" / "Hi" / "Hey"
- "Good morning" / "Good afternoon" / "Good evening"
- "What is your name?"
- "How are you?"

### Time & Date
- "What time is it?" / "Time now"
- "What is the date?" / "Today's date"

### Open Websites
- "Open YouTube"
- "Open Google"
- "Open Gmail" / "Open email"
- "Play music"
- "Open Facebook"
- "Open Instagram"
- "Open Twitter"
- "Open LinkedIn"
- "Open GitHub"

### Launch Applications
- "Open terminal" / "Open command prompt"
- "Open Notepad"
- "Open Calculator"
- "Open WhatsApp"

### Search
- "Search [your query]" - Opens Google search

### System Commands (Use with caution!)
- "Shutdown" - Shuts down the computer
- "Restart" - Restarts the computer
- "Sleep" - Puts computer to sleep

### Fun
- "Tell me a joke"
- "Thank you" / "Thanks"

---

## 📁 Files Overview

- `app.py` - Main application (GUI/CLI launcher)
- `speech_to_text.py` - Microphone input and speech recognition
- `text_to_speech.py` - Text-to-speech output
- `action.py` - Command processing and action execution
- `requirements.txt` - Python dependencies
- `image/` - GUI images (optional)

---

## 🔧 Troubleshooting

### Microphone Error (OSError -9999)
**Fixed!** The updated code includes:
- Ambient noise adjustment
- Proper timeout handling
- Better error handling

If you still have issues:
1. Check microphone permissions in Windows Settings
2. Ensure microphone is set as default recording device
3. Close other apps using the microphone

### PyAudio Installation Issues
- Use the wheel file method for Python 3.11
- Make sure you download the correct version for your Python

### tkinter Not Found
- Reinstall Python with the `tcl/tk` option enabled

### pyttsx3 Voice Issues
- Check Windows text-to-speech settings
- Ensure audio drivers are up to date

---

## 🎨 Extending the Assistant

Add more commands in `action.py`:

```python
elif "your command" in user_data:
    tts.text_to_speech("Your response")
    # Your action here
```

---

## 📝 License

This project does not include a license file. Add a LICENSE file (MIT/Apache2/etc.) if you want to open-source it.

---

## 🤝 Contributing

Contributions are welcome! Please open issues for bugs or feature requests.

---

**Enjoy your AI Desktop Assistant! 🎉**
