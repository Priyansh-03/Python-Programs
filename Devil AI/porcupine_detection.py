import struct 
import pvporcupine
import pyaudio

porcupine=None
paud=None
audio_stream=None

try:
    access_key="wuBirh3n1fv04/woOgW3ivkPxbOGhLxA47pIuQwXuG0Pkon+SveqSQ==" #to create access key signup to https://console.picovoice.ai/ 
    porcupine=pvporcupine.create(keywords=["jarvis","alexa"])
    paud=pyaudio.PyAudio()
    audio_stream=paud.open(rate=porcupine.sample_rate,channels=1,format=pyaudio.paInt16,input=True,frames_per_buffer=porcupine.frame_length)
    while True:
        keyword=audio_stream.read(porcupine.frame_length)
        keyword=struct.unpack_from("h"*porcupine.frame_length,keyword)
        keyword_index=porcupine.process(keyword)
        if keyword_index>=0:
            print("hotword detected")
            

finally:
    if porcupine is not None:
        porcupine.delete()
    if audio_stream is not None:
        audio_stream.close()
    if paud is not None:
        paud.terminate()