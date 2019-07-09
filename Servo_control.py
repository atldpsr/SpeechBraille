import RPi.GPIO as GPIO
from time import sleep



def setAngle(servo, angle):
	pwm = GPIO.PWM(servo, 50)
	pwm.start(0)
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(servo,GPIO.OUT)
	duty = angle/18 + 2
	GPIO.output(servo, True)
	pwm.ChangeDutyCycle(duty)
	sleep(1)
	GPIO.output(servo, False)
	pwm.ChangeDutyCycle(0)
	pwm.stop()
	


