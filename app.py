from face_recognition import faceapp
from object_recognition import classify
from text_recognition import textapp

from scripts import say, cam

def read():
    cam.capture()
    try:
        results = textapp.read()
        
        print(results)
        say.speak(results)
    except AssertionError:
        say.speak('No text found')
        print("cant")
    except PiCameraMMALError:
        say.speak("Need to restart")
        print("error")

def what():
    cam.capture()
    try:
        results = classify.what()
        
        print(results)
        say.speak(results)
    except AssertionError:
        say.speak('Can not recognize object')
        print("cant")
   # except PiCameraMMALError:
    #    say.speak("Need to restart")
     #   print("error")

def who():
    cam.capture()
    try:
        results = faceapp.who()
        
        print(results)
        say.speak(results)
    except AssertionError:
        say.speak('Can not recognize face')
        print("cant")
    except PiCameraMMALError:
        say.speak("Need to restart")
        print("error")

def dotasknum(num, *argv):
    if num == 1:
        return read(*argv)
    elif num == 2:
        return what(*argv)
    elif num == 3:
        return who(*argv)


from gpiozero import Button
from signal import pause


def getid(button):
    if(button.pin.number == 13):
        print("Pressed 1")
    if(button.pin.number == 6):
        print("Pressed 2")
        return what()
    if(button.pin.number == 26):
        print("Pressed 3")
        return who()
    if(button.pin.number == 19):
        print("Pressed 4")
        return read()
    
def which():
    b1 = Button(13)
    b2 = Button(6)
    b3 = Button(26)
    b4 = Button(19)

    b1.when_pressed = getid
    b2.when_pressed = getid
    b3.when_pressed = getid
    b4.when_pressed = getid

    pause()

# print(dotasknum(1, 'text_recognition/data/test.jpeg'))
# print(dotasknum(3, 'face_recognition/dumpdata/known', 'face_recognition/dumpdata/unknown/harry.jpeg'))
# print(dotasknum(2, 'object_recognition/download.jpeg'))
# 
# print(classify.what("/home/pi/third-eye/tmp/test/object/apple.jpeg"))
# print(faceapp.who("/home/pi/third-eye/tmp/test/face/known", "/home/pi/third-eye/tmp/test/face/isharry.jpeg"))
# print(textapp.read("/home/pi/third-eye/tmp/test/text/download.png"))

which()

