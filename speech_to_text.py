import speech_recognition as sr

def recognize_speech_from_mic():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
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
