import speech_recognition as sr
import pyaudio

def recognize_speech_from_mic():
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Adjusting for ambient noise... Please wait")
            r.adjust_for_ambient_noise(source, duration=1)
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source, timeout=5, phrase_time_limit=10)
            
            try:
                voice_data = r.recognize_google(audio)
                print("You said:", voice_data)
                return voice_data
            except sr.UnknownValueError:
                print("Sorry, I did not get that")
                return "Sorry, I did not get that"
            except sr.RequestError:
                print("Sorry, my speech service is down")
                return "Sorry, my speech service is down"
    except OSError as e:
        print(f"Microphone error: {e}")
        return "Microphone error occurred"
    except Exception as e:
        print(f"Error: {e}")
        return "An error occurred"
