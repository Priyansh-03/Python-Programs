import pyttsx3
engine=pyttsx3.init('sapi5')
engine.setProperty("rate",178)
voices=engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)


def speak(audio):
   engine.say(audio)
   engine.runAndWait()