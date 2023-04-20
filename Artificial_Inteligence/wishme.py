import datetime
import speak

def wishMe():
    

    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Hi, Good morning!")

    elif hour >=12 and hour <18:
        speak("Hi, Good afternoon!")

    else:
        speak("Hi, Good Evening!")

    speak('Tell me what can i do for you?')