import speech_recognition as sr
from speak_module import *

def takecommand():
    #it takes microphone input from the user and returns string output

    r = sr.Recognizer() 
    with sr.Microphone() as source:
        speak("Please give command...")
        print("please give command...\n")
        print("Listening...")
        r.pause_threshold = 1
        #open pause threshold to change settings!!
        audio=r.listen(source,timeout=10)
        #stopListening()
        
    

    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-IN')
        print(f"You said:{query}\n")   

    except Exception as e:
        # print(e)
        print("I'm sorry :(!! Can you say that again please?")
        speak("I'm sorry!! Can you say that again please?")
        return "None"
    return query 