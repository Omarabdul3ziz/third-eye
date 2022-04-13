# import os
# import datetime

# def capture():
#     os.system("fswebcam -r 640x480 --no-banner /home/pi/third-eye/data/tmpimage.jpg")
    
  
  
from picamera import PiCamera
#from time import sleep


def capture():
    camera = PiCamera()
    #camera.start_preview()
    #sleep(50)
    camera.capture('/home/pi/third-eye/temp/image.jpg')
    #camera.stop_preview()
    camera.close()

capture()