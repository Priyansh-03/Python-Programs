import pyttsx3

bot_unknown = "Sorry, I could not understand what you said."
engine=pyttsx3.init('sapi5')
engine.setProperty("rate",130)
voices=engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[0].id)

def generate_response(command):
    if command is None:
        speak(bot_unknown)
    elif "hello" in command:
        speak("Hello! How can I help you?")
    else:
        speak(bot_unknown)

def speak(audio):
   engine.say(audio)
   engine.runAndWait()
