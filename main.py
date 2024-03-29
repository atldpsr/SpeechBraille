# from Servo_control import setAngle
from ibm_recognize import recognize
from voice_recorder import record
import requests
from time import sleep
angle = 90              #angle to which to change the servo to
space_interval = 1      #amount of time to wait when getting a space
letter_interval = 0.5   #amount of time to wait when getting a new letter




alphabets = {           # alphabets mapped to servo numbers
    "a": [1],
    "b": [1,2],
    "c": [1,6],
    "d": [1,6,5],
    "e": [1,5],
    "f": [1,2,6],
    "g": [1,2,5,6],
    "h": [1,2,5],
    "i": [2,6],
    "j": [2,5,6],
    "k": [1,3],
    "l": [1,2,3],
    "m": [1,3,6],
    "n": [1,3,5,6],
    "o": [1,3,5],
    "p": [1,2,3,6],
    "q": [1,2,3,5,6],
    "r": [1,2,3,5],
    "s": [1,2,6],
    "t": [2,3,5,6],
    "u": [1,3,4],
    "v": [1,2,3,4],
    "w": [2,4,5,6],
    "x": [1,3,4,6],
    "y": [1,3,4,5,6],
    "z": [1,3,4,5],
    " ": []    
    }
servos = { # pin mappings
    1:7,
    2:8,
    3:9,
    4:10,
    5:11,
    6:12
    } 
# for servo in servos:
#     setAngle(servo, 0) # Initialise all the servos from zero
prompt = input("Do you wanna recognize from an exisiting file?[y/n]").lower()
if prompt == "y":
    filename = input("Enter file name (without any extension)") + '.wav'
else:
    filename = input("Enter the filename you want to save to without any extension") + '.wav'
    record(filename)

test = recognize(filename).replace("'", "")

print('recognized: {}'.format(test))
test_pins=[alphabets[i.lower()] for i in test] # a list of all the sservo mappings for the sentence



for letter, character  in zip(test_pins, test): # iterate over all letters in the string
    if letter == []:                            #space
        print('waiting {} second, got a space'.format(space_interval))
        sleep(space_interval)
    else:
        print('got letter: {}'.format(character))
        
        for pin in letter:                      # iterate over all the pins for the letter

            print("setting pin:{}, angle:{}".format(pin, angle))
    print('letter completed, now waiting for 0.5 seconds')
    sleep(letter_interval)                      # wait for new letter


# GPIO.cleanup()

    