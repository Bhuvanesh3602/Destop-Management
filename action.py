from sys import platform
import speech_to_text as stt
import text_to_speech as tts
import webbrowser
import datetime
import os
import subprocess
import random
import psutil
import socket

def Action(data):
    user_data = data.lower()
    
    # Greetings
    if "what is your name" in user_data or "your name" in user_data:
        response = "My name is AI Assistant Pro. I'm here to help you with your desktop tasks."
        tts.text_to_speech(response)
    elif "hello" in user_data or "hye" in user_data or "hi" in user_data:
        responses = [
            "Hey sir, how can I help you?",
            "Hello! What can I do for you today?",
            "Hi there! Ready to assist you!"
        ]
        tts.text_to_speech(random.choice(responses))
    elif "good morning" in user_data:
        response = "Good morning sir! Have a wonderful day ahead!"
        tts.text_to_speech(response)
    elif "good afternoon" in user_data:
        response = "Good afternoon sir! How may I assist you?"
        tts.text_to_speech(response)
    elif "good evening" in user_data:
        response = "Good evening sir! How can I help you tonight?"
        tts.text_to_speech(response)
    elif "good night" in user_data:
        response = "Good night sir! Sleep well and sweet dreams."
        tts.text_to_speech(response)
    
    # Time and Date
    elif "time now" in user_data or "what time" in user_data or "current time" in user_data:
        current_time = datetime.datetime.now()
        Time = f"The time is {current_time.strftime('%I:%M %p')}."
        tts.text_to_speech(Time)
    elif "date" in user_data or "today" in user_data and "what" in user_data:
        today = datetime.datetime.now()
        date_str = f"Today is {today.strftime('%A, %B %d, %Y')}"
        tts.text_to_speech(date_str)
    elif "day" in user_data and "what" in user_data:
        day = datetime.datetime.now().strftime('%A')
        tts.text_to_speech(f"Today is {day}")
    
    # System Information
    elif "battery" in user_data or "battery status" in user_data:
        try:
            battery = psutil.sensors_battery()
            if battery:
                percent = battery.percent
                plugged = "plugged in" if battery.power_plugged else "not plugged in"
                tts.text_to_speech(f"Battery is at {percent} percent and {plugged}")
            else:
                tts.text_to_speech("Battery information not available")
        except:
            tts.text_to_speech("Unable to get battery status")
    elif "cpu" in user_data or "processor" in user_data:
        cpu_percent = psutil.cpu_percent(interval=1)
        tts.text_to_speech(f"CPU usage is at {cpu_percent} percent")
    elif "memory" in user_data or "ram" in user_data:
        memory = psutil.virtual_memory()
        tts.text_to_speech(f"Memory usage is at {memory.percent} percent")
    elif "ip address" in user_data or "my ip" in user_data:
        try:
            hostname = socket.gethostname()
            ip = socket.gethostbyname(hostname)
            tts.text_to_speech(f"Your IP address is {ip}")
        except:
            tts.text_to_speech("Unable to get IP address")
    
    # Web browsing
    elif "youtube" in user_data:
        tts.text_to_speech("Opening YouTube for you sir")
        webbrowser.open("https://www.youtube.com/")
    elif "google" in user_data and "open" in user_data:
        tts.text_to_speech("Opening Google for you sir")
        webbrowser.open("https://www.google.com/")
    elif "gmail" in user_data or "email" in user_data:
        tts.text_to_speech("Opening Gmail for you sir")
        webbrowser.open("https://mail.google.com/")
    elif "play music" in user_data or "music" in user_data:
        tts.text_to_speech("Opening music website for you sir.")
        webbrowser.open("https://www.spotify.com/")
    elif "facebook" in user_data:
        tts.text_to_speech("Opening Facebook for you sir")
        webbrowser.open("https://www.facebook.com/")
    elif "instagram" in user_data:
        tts.text_to_speech("Opening Instagram for you sir")
        webbrowser.open("https://www.instagram.com/")
    elif "twitter" in user_data or "x.com" in user_data:
        tts.text_to_speech("Opening Twitter for you sir")
        webbrowser.open("https://www.twitter.com/")
    elif "linkedin" in user_data:
        tts.text_to_speech("Opening LinkedIn for you sir")
        webbrowser.open("https://www.linkedin.com/")
    elif "github" in user_data:
        tts.text_to_speech("Opening GitHub for you sir")
        webbrowser.open("https://www.github.com/")
    elif "amazon" in user_data:
        tts.text_to_speech("Opening Amazon for you sir")
        webbrowser.open("https://www.amazon.com/")
    elif "netflix" in user_data:
        tts.text_to_speech("Opening Netflix for you sir")
        webbrowser.open("https://www.netflix.com/")
    elif "reddit" in user_data:
        tts.text_to_speech("Opening Reddit for you sir")
        webbrowser.open("https://www.reddit.com/")
    elif "stack overflow" in user_data:
        tts.text_to_speech("Opening Stack Overflow for you sir")
        webbrowser.open("https://stackoverflow.com/")
    
    # Applications
    elif "terminal" in user_data or "command prompt" in user_data:
        tts.text_to_speech("Opening terminal for you sir.")
        if platform == "win32":
            os.system("start cmd")
        elif platform == "linux":
            os.system("gnome-terminal")
        elif platform == "darwin":
            os.system("open -a Terminal")
    elif "notepad" in user_data:
        tts.text_to_speech("Opening Notepad for you sir")
        if platform == "win32":
            os.system("notepad")
    elif "calculator" in user_data:
        tts.text_to_speech("Opening Calculator for you sir")
        if platform == "win32":
            os.system("calc")
    elif "paint" in user_data:
        tts.text_to_speech("Opening Paint for you sir")
        if platform == "win32":
            os.system("mspaint")
    elif "file explorer" in user_data or "explorer" in user_data:
        tts.text_to_speech("Opening File Explorer for you sir")
        if platform == "win32":
            os.system("explorer")
    elif "task manager" in user_data:
        tts.text_to_speech("Opening Task Manager for you sir")
        if platform == "win32":
            os.system("taskmgr")
    elif "control panel" in user_data:
        tts.text_to_speech("Opening Control Panel for you sir")
        if platform == "win32":
            os.system("control")
    elif "settings" in user_data:
        tts.text_to_speech("Opening Settings for you sir")
        if platform == "win32":
            os.system("start ms-settings:")
    elif "whatsapp" in user_data:
        tts.text_to_speech("Opening WhatsApp for you sir.")
        try:
            os.system("start whatsapp:")
        except Exception as e:
            tts.text_to_speech("Sorry sir, I could not open WhatsApp.")
            print("Error:", e)
    elif "vs code" in user_data or "visual studio code" in user_data:
        tts.text_to_speech("Opening Visual Studio Code for you sir")
        if platform == "win32":
            os.system("code")
    
    # System commands
    elif "shutdown" in user_data and "system" in user_data:
        tts.text_to_speech("Shutting down the system sir")
        if platform == "win32":
            os.system("shutdown /s /t 1")
    elif "restart" in user_data and "system" in user_data:
        tts.text_to_speech("Restarting the system sir")
        if platform == "win32":
            os.system("shutdown /r /t 1")
    elif "sleep" in user_data and "system" in user_data:
        tts.text_to_speech("Putting system to sleep sir")
        if platform == "win32":
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
    elif "lock" in user_data:
        tts.text_to_speech("Locking the system sir")
        if platform == "win32":
            os.system("rundll32.exe user32.dll,LockWorkStation")
    elif "volume up" in user_data:
        tts.text_to_speech("Increasing volume")
        if platform == "win32":
            os.system("nircmd.exe changesysvolume 2000")
    elif "volume down" in user_data:
        tts.text_to_speech("Decreasing volume")
        if platform == "win32":
            os.system("nircmd.exe changesysvolume -2000")
    elif "mute" in user_data:
        tts.text_to_speech("Muting volume")
        if platform == "win32":
            os.system("nircmd.exe mutesysvolume 1")
    
    # Fun features
    elif "joke" in user_data:
        jokes = [
            "Why do programmers prefer dark mode? Because light attracts bugs!",
            "Why did the developer go broke? Because he used up all his cache!",
            "How many programmers does it take to change a light bulb? None, that's a hardware problem!",
            "Why do Java developers wear glasses? Because they don't C sharp!",
            "What's a programmer's favorite hangout place? The Foo Bar!",
            "Why did the programmer quit his job? Because he didn't get arrays!"
        ]
        tts.text_to_speech(random.choice(jokes))
    elif "flip a coin" in user_data or "coin flip" in user_data:
        result = random.choice(["Heads", "Tails"])
        tts.text_to_speech(f"The coin landed on {result}")
    elif "roll a dice" in user_data or "dice roll" in user_data:
        result = random.randint(1, 6)
        tts.text_to_speech(f"You rolled a {result}")
    elif "random number" in user_data:
        result = random.randint(1, 100)
        tts.text_to_speech(f"Your random number is {result}")
    elif "thank you" in user_data or "thanks" in user_data:
        responses = [
            "You're welcome sir! Happy to help.",
            "My pleasure sir!",
            "Anytime sir! That's what I'm here for."
        ]
        tts.text_to_speech(random.choice(responses))
    elif "how are you" in user_data:
        responses = [
            "I'm doing great sir! Thank you for asking. How can I assist you?",
            "I'm functioning perfectly sir! Ready to help you.",
            "All systems operational sir! What can I do for you?"
        ]
        tts.text_to_speech(random.choice(responses))
    elif "who created you" in user_data or "who made you" in user_data:
        response = "I was created using Python programming language. I'm an AI assistant designed to help with desktop tasks."
        tts.text_to_speech(response)
    elif "what can you do" in user_data or "your features" in user_data:
        response = "I can open websites, launch applications, tell you the time and date, check system information, tell jokes, and much more. Just ask me!"
        tts.text_to_speech(response)
    
    # Search
    elif "search" in user_data:
        query = user_data.replace("search", "").replace("for", "").strip()
        if query:
            tts.text_to_speech(f"Searching for {query}")
            webbrowser.open(f"https://www.google.com/search?q={query}")
        else:
            tts.text_to_speech("What would you like me to search for?")
    elif "wikipedia" in user_data:
        query = user_data.replace("wikipedia", "").replace("search", "").strip()
        if query:
            tts.text_to_speech(f"Searching Wikipedia for {query}")
            webbrowser.open(f"https://en.wikipedia.org/wiki/{query}")
        else:
            tts.text_to_speech("What would you like me to search on Wikipedia?")
    
    # Weather (opens weather website)
    elif "weather" in user_data:
        tts.text_to_speech("Opening weather information for you sir")
        webbrowser.open("https://www.weather.com/")
    
    # News
    elif "news" in user_data:
        tts.text_to_speech("Opening news for you sir")
        webbrowser.open("https://news.google.com/")
    
    # Exit commands
    elif "exit" in user_data or "quit" in user_data or "bye" in user_data:
        tts.text_to_speech("Goodbye sir! Have a great day!")
    
    else:
        responses = [
            "Sorry, I didn't understand that. Can you please rephrase?",
            "I'm not sure what you mean. Could you try asking differently?",
            "I didn't catch that. Please try again."
        ]
        tts.text_to_speech(random.choice(responses))