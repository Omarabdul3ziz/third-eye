from gtts import gTTS
import os

def speak(text):
    tts = gTTS(text=text,lang="en",tld="com")
    filename = '/home/pi/third-eye/temp/voice.mp3'
    tts.save(filename)
    os.system("omxplayer " + filename)
    
#   try:
#         tts = gTTS(text=text, lang='en')
#         filename = 'data/voice.mp3'
#         tts.save(filename)
#     except AssertionError:
#         tts = gTTS(text="Can't recognize", lang='en')
#         filename = 'data/voice.mp3'
#         tts.save(filename)
#     finally:
#         os.system("omxplayer " + filename)