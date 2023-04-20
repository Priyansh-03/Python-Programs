import pyttsx3
import speech_recognition as sr

bot_unknown = "Sorry, I could not understand what you said."
engine=pyttsx3.init('sapi5')
engine.setProperty("rate",130)
voices=engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
   engine.say(audio)
   engine.runAndWait()


def takecommand():
    #it takes microphone input from the user and returns string output

    r = sr.Recognizer() 
    with sr.Microphone() as source:
        print("Listening...")
        speak("I'm Listening ")
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1
        #open pause threshold to change settings!!
        audio=r.listen(source,timeout=10)
        #stopListening()

    try:
        print("Recognizing...")
        speak("I'm Recognizing,please wait")
        query=r.recognize_google(audio,language='en-IN')
        print(f"You said:{query}\n")   

    except Exception as e:
        print(e)
        print("I'm sorry :(!! Can you say that again please?")
        speak("I'm sorry!! Can you say that again please?")
        
        return ""

    return query