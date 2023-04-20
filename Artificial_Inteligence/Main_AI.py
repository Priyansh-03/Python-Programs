from modules import *
# modules.modules_before()
import internet
# # from lsHotword import ls
# # ls.lsHotword_loop()
from ast import main
from logging.config import stopListening
import socket
import pyttsx3
import speech_recognition as sr
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
internet.connect()
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# modules.modules_after()
from speak_module import *
from password import *
from take_command import *
if __name__ == "__main__":
    speak("TURNING ON...!!")
    speak("I am DEVIL's Artificial inteligence.")
    passkey()    

    while True:
    # if 1:
        
        query = takecommand().lower()
        #logic..
        # if("None") in query:
        #     print("Maybe you didn't gave me command")
        #     speak("Maybe you didn't gave me command")

        if ('search') in query:
            query = query.replace("search", "")
            speak('Searching'+ query + "on wikipedia")
            try:
                results=wikipedia.summary(query, sentences=5,auto_suggest=False)
                speak("Here is what i found.")
                print(results)
                speak(results)
            except (wikipedia.exceptions.DisambiguationError or wikipedia.exceptions.PageError) as e:
                print(e.options)
                speak("Sorry, no valid link was found. please ask for another query!")

        
        
        elif ('what is my name')in query:
            print('I predict it is you!! Priyansh :D')
            speak('Well!! I was developed by Preeaansh, and for now, only he uses me often, so i know only one name.')
            
        elif'open youtube' in query:
            speak("opening youtube...")
            webbrowser.open("https://www.youtube.com/")
        
        elif'open google' in query:
            speak("opening google...")
            webbrowser.open("www.google.com")

        # elif'play music' in query:
        # speak("Here is your result...")
        #     music_dir.='D//...//...'#file location & use // in between.

        elif'youtube music' in query:
            speak("opening youtube music...")
            webbrowser.open("https://www.youtube.com/watch?v=fJJmG7CTqRE&list=RDMM&start_radio=1")
            
        elif'play' in query:
            video=query=query.replace("play","")
            speak('playing'+video)
            pywhatkit.playonyt(video)

        elif'open gmail' in query:
            speak("opening gmail...")
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")

        elif'shutdown pc' in query:
            speak("Okay sir...!!Shutting down.See you again")
            os.system("shutdown /s /t 1")
            
        elif'restart pc' in query:
            speak("Okay sir...!!restarting pc")
            os.system("restart /r /t 1")

        elif'''what's the time'''in query:
            time=strtime = datetime.datetime.now().strftime("%H:%M:%S")
            print(time)
            speak(f"Sir!!,the time is {strtime}")

        elif'open visual studio code' in query:
            path="C:\\Users\\priya\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)

        # elif 'send email'in query:
        #     try:
        #         speak("w")

        elif("let's talk") in query:
            # reply=random.choice('yes','no')
            # if(reply=="yes"):
            print(":D")
            speak('OKAY!! I love talking, like all other females, hahaha!!')
            speak( "by the way, how are you?")
            reply= takecommand().lower()
            if ('i am fine') in reply:
                print(":D")
                speak("great...!! glad to hear.")
                speak("i wish you remain healthy!!")
                speak("oh, oh!! I'M sorry my friend!! I'm running late of time!! we can talk later!! see you!!")
           
            else:
                speak("I'm sorry! but, i just got a call and now have a lot of work to do. We can talk later!")

        elif 'are you single' in query:
            reply= speak('NO! I am in a relationship with wifi. hahaha')
            print(reply)
            
        # elif'repeat after me' in query:
        #s

        elif'tell me a joke' in query:
            joke=pyjokes.get_joke()
            print(joke)
            speak(joke)

        # elif'start game'in query:
        #     print("which game you would like to play?")
        #     speak("which game you would like to play?")
        #     games=['tik tak toe']
        #     print(games)
        #     enter=takecommand().lower()
        #     if('tik tak toe')in enter:
        #         games()

        elif'close'in query:
            print("Ok sir!! See you again :)")
            speak("Ok sir!! See you again :)")
            exit(0)

        elif'what can you do' in query:
            speak("hii my friend. For now, i can do only few things like...")
            print('''If you want to talk, just say "let's talk"\nIf you want to play youtube music, just say"youtube music"\nIf you want to search in wikipedia, just say search (command)\n want to talk?, say"let's talk"\n For jokes,say "tell me a joke"\n Try to ask"am i single?"\nAsk time,say"what's the time"\nTo restart or Shutdown pc,say "restart pc" or "Shutdown pc" say "open google"\n say "open youtube"\nAsk,"What is my name?"\n To exit, say "Close AI"\n:D ''')

            speak('''If you want to talk, just say "let's talk"\nIf you want to play youtube music, just say"youtube music"\nIf you want to search in wikipedia, just say search (command)\n want to talk?, say"let's talk"\n For jokes,say "tell me a joke"\n Try to ask"am i single?"\nTo Ask time,say"what's the time"\nTo restart or Shutdown pc,say "restart pc" or, "Shutdown pc"\ntry say "open google"\n say "open youtube"\nAsk,"What is my name?"\n To exit, say "Close AI"\n ''')
        
        # elif("") in query:
        #     query = query.replace("", "")
        #     result=wikipedia.search(query)
        #     print(result)
        #     speak('u said,'+ query+f"here is what i found...{result}\n")