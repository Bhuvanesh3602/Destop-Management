from sys import platform
import speech_to_text as stt
import text_to_speech as tts
import webbrowser
import datetime
from sys import platform
import platform

import os
def Action(data):
    user_data=data.lower()
    if "what is your name" in user_data:
        response = "My name is Virtual Assistant."
        tts.text_to_speech(response)
    elif "hello" in user_data or "hye" in user_data:
        response = "Hey sir, how can I help you?"
        tts.text_to_speech(response)
    elif "good morning" in user_data:
        response = "Good morning sir!"
        tts.text_to_speech(response)
        tts.text_to_speech(response)
    elif "time now" in user_data:
        current_time = datetime.datetime.now()
        Time = f"The time is {current_time.hour} hour and {current_time.minute} minutes."
        tts.text_to_speech(Time)
    elif "play music" in user_data:
        tts.text_to_speech("Opening music website for you sir.")
        webbrowser.open("https://gaana.com/")
        
    elif "youtube" in user_data:
        tts.text_to_speech("Opening youtube website for you sir")
        webbrowser.open("https://www.youtube.com/")
        
    elif "terminal" in user_data or "command prompt" in user_data:
            tts.text_to_speech("Opening terminal for you sir.")
            if platform.system() == "Windows":
                os.system("start cmd")
            elif platform.system() == "Linux":
                os.system("gnome-terminal")
            elif platform.system() == "Darwin":  # macOS
                os.system("open -a Terminal")

    elif "whatsapp" in user_data:
       tts.text_to_speech("Opening WhatsApp for you sir.")
       try:
          os.system("start whatsapp:")  # Works for Microsoft Store version
       except Exception as e:
           tts.text_to_speech("Sorry sir, I could not open WhatsApp.")
           print("Error:", e)

        
        
    else:
        response = "Sorry, I didn't understand that."
        tts.text_to_speech(response)