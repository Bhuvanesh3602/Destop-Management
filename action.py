from sys import platform
import speech_to_text as stt
import text_to_speech as tts
import webbrowser
import datetime
import os
import subprocess
import random

def Action(data):
    user_data = data.lower()
    
    # Greetings
    if "what is your name" in user_data:
        response = "My name is Virtual Assistant."
        tts.text_to_speech(response)
    elif "hello" in user_data or "hye" in user_data or "hi" in user_data:
        response = "Hey sir, how can I help you?"
        tts.text_to_speech(response)
    elif "good morning" in user_data:
        response = "Good morning sir!"
        tts.text_to_speech(response)
    elif "good afternoon" in user_data:
        response = "Good afternoon sir!"
        tts.text_to_speech(response)
    elif "good evening" in user_data:
        response = "Good evening sir!"
        tts.text_to_speech(response)
    elif "good night" in user_data:
        response = "Good night sir! Sleep well."
        tts.text_to_speech(response)
    
    # Time and Date
    elif "time now" in user_data or "what time" in user_data or "current time" in user_data:
        current_time = datetime.datetime.now()
        Time = f"The time is {current_time.hour} hour and {current_time.minute} minutes."
        tts.text_to_speech(Time)
    elif "date" in user_data or "today" in user_data:
        today = datetime.datetime.now()
        date_str = f"Today is {today.strftime('%A, %B %d, %Y')}"
        tts.text_to_speech(date_str)
    
    # Web browsing
    elif "youtube" in user_data:
        tts.text_to_speech("Opening YouTube for you sir")
        webbrowser.open("https://www.youtube.com/")
    elif "google" in user_data:
        tts.text_to_speech("Opening Google for you sir")
        webbrowser.open("https://www.google.com/")
    elif "gmail" in user_data or "email" in user_data:
        tts.text_to_speech("Opening Gmail for you sir")
        webbrowser.open("https://mail.google.com/")
    elif "play music" in user_data or "music" in user_data:
        tts.text_to_speech("Opening music website for you sir.")
        webbrowser.open("https://gaana.com/")
    elif "facebook" in user_data:
        tts.text_to_speech("Opening Facebook for you sir")
        webbrowser.open("https://www.facebook.com/")
    elif "instagram" in user_data:
        tts.text_to_speech("Opening Instagram for you sir")
        webbrowser.open("https://www.instagram.com/")
    elif "twitter" in user_data:
        tts.text_to_speech("Opening Twitter for you sir")
        webbrowser.open("https://www.twitter.com/")
    elif "linkedin" in user_data:
        tts.text_to_speech("Opening LinkedIn for you sir")
        webbrowser.open("https://www.linkedin.com/")
    elif "github" in user_data:
        tts.text_to_speech("Opening GitHub for you sir")
        webbrowser.open("https://www.github.com/")
    
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
    elif "whatsapp" in user_data:
        tts.text_to_speech("Opening WhatsApp for you sir.")
        try:
            os.system("start whatsapp:")
        except Exception as e:
            tts.text_to_speech("Sorry sir, I could not open WhatsApp.")
            print("Error:", e)
    
    # System commands
    elif "shutdown" in user_data:
        tts.text_to_speech("Shutting down the system sir")
        if platform == "win32":
            os.system("shutdown /s /t 1")
    elif "restart" in user_data:
        tts.text_to_speech("Restarting the system sir")
        if platform == "win32":
            os.system("shutdown /r /t 1")
    elif "sleep" in user_data:
        tts.text_to_speech("Putting system to sleep sir")
        if platform == "win32":
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
    
    # Fun features
    elif "joke" in user_data:
        jokes = [
            "Why do programmers prefer dark mode? Because light attracts bugs!",
            "Why did the developer go broke? Because he used up all his cache!",
            "How many programmers does it take to change a light bulb? None, that's a hardware problem!"
        ]
        tts.text_to_speech(random.choice(jokes))
    elif "thank you" in user_data or "thanks" in user_data:
        response = "You're welcome sir! Happy to help."
        tts.text_to_speech(response)
    elif "how are you" in user_data:
        response = "I'm doing great sir! Thank you for asking. How can I assist you?"
        tts.text_to_speech(response)
    
    # Search
    elif "search" in user_data:
        query = user_data.replace("search", "").strip()
        if query:
            tts.text_to_speech(f"Searching for {query}")
            webbrowser.open(f"https://www.google.com/search?q={query}")
        else:
            tts.text_to_speech("What would you like me to search for?")
    
    else:
        response = "Sorry, I didn't understand that."
        tts.text_to_speech(response)