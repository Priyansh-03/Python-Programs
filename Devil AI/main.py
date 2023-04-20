from porcupine_detection import *
import speech_recognition as sr
import response_generator


# Define the Porcupine keywords
keywords = ["jarvis", "alexa"]

# Initialize the Porcupine hotword detection system
porcupine = PorcupineDetection(keywords)

# Initialize the speech recognition system
r = sr.Recognizer()

# Define the main program loop
while True:
    # Listen for the hotword
    porcupine.detect_hotword()
    
    # Once the hotword is detected, listen for the user's command
      
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
    
    # Generate a response based on the user's command
    response_generator.generate_response(command)
