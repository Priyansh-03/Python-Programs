import socket
from speak_module import *

def connect():
    try:
        # connect to the host -- tells us if the host is actually
        # reachable
        sock = socket.create_connection(("www.google.com", 80))
        if sock is not None:
            #print("Inernet connection is ON!!")
            sock.close
            print("Connecting to INTERNET!")
            speak("Connecting to INTERNET!")
            
           

    except OSError:
        pass
        print("Internet connection unavailable!! Please connect to a good internet :,(")
        speak("Internet connection unavailable!! Please connect to a good internet")
        exit(0)   

print("please wait!!...")
speak("please wait!!..Checking internet connection")