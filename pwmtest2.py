import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(4, GPIO.OUT)
p = GPIO.PWM(4, 340)
p.ChangeFrequency(340)
p.start(50)
counter = 0

while True:
    p.ChangeDutyCycle(75)
    time.sleep(5)
    p.ChangeDutyCycle(25)
    time.sleep(5)

    if(counter == 2):
        break
    else:
        counter+=1





p.ChangeDutyCycle(50)

GPIO.cleanup()
