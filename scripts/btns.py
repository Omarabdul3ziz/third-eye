
from gpiozero import Button
from signal import pause


def getid(button):
    if(button.pin.number == 13):
        print("Pressed 1")
    if(button.pin.number == 6):
        print("Pressed 2")
    if(button.pin.number == 26):
        print("Pressed 3")
    if(button.pin.number == 19):
        print("Pressed 4")
    
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
which()

# ================================================ #
# import RPi.GPIO as GPIO
# GPIO.setmode(GPIO.BCM)

# ----------------------------------------- 4 buttons

""" this works
# define buttons
buttonpins = [6, 13, 19, 26] 
GPIO.setup(buttonpins, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# 1. loop
while True:
    if (GPIO.input(6) == 0):
        print(1)
    if (GPIO.input(13) == 0):
        print(2)
    if (GPIO.input(19) == 0):
        print(3)
    if (GPIO.input(26) == 0):
        print(4)
"""

""" this not
# 2. instead of the loop you can add event listener
# event will interrupt the progeram and call the btnpressed function

def buttonPressed(code):
    ## run function with the code
    print(code)
while True:
    sleep(1)
GPIO.add_event_detect(6, GPIO.RISING, callback=lambda x: buttonPressed(1), bouncetime=150)
GPIO.add_event_detect(13, GPIO.RISING, callback=lambda x: buttonPressed(2), bouncetime=150)
GPIO.add_event_detect(19, GPIO.RISING, callback=lambda x: buttonPressed(3), bouncetime=150)
GPIO.add_event_detect(26, GPIO.RISING, callback=lambda x: buttonPressed(4), bouncetime=150)

"""



#  this works fine

"""

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

buttonpins = [6, 13, 19, 26] 
GPIO.setup(buttonpins, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# 1. loop
while True:
    if (GPIO.input(6) == 0):
        print(2)
    if (GPIO.input(13) == 0):
        print(1)
    if (GPIO.input(19) == 0):
        print(4)
    if (GPIO.input(26) == 0):
        print(3)
        
        """