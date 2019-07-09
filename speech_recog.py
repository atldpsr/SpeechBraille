from Servo_control import setAngle
alphabets = {
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
servos = {
    1:7,
    2:8,
    3:9,
    4:10,
    5:11,
    6:12
    }

test="hello anish"
test_pins=[]
for i in test:
    test_pins.append(alphabets[i])
for j in test_pins:
    for k in j:
        setAngle()
print (test_pins)



    