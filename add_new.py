#!/usr/bin/python3
from picamera import PiCamera
#from time import sleep

name = input("enter the name of the person: ")

def add(name):
    camera = PiCamera()
    #camera.start_preview()
    #sleep(50)
    camera.capture(f'/home/pi/third-eye/data/known/{name}.jpg')
    #camera.stop_preview()
    camera.close()

add(name)