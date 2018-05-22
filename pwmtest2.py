import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
p = GPIO.PWM(4, 340)
p.ChangeFrequency(340)
p.start(50)
counter = 0

while True:
    p.ChangeDutyCycle(75)
    time.sleep(2)
    p.ChangeDutyCycle(25)
    time.sleep(2)

    if(counter == 2):
        break
    else:
        counter+=1





p.ChangeDutyCycle(50)

p.cleanup()
