import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(4, GPIO.OUT)
p = GPIO.PWM(4, 333)
p.ChangeFrequency(333)
p.start(50)

high = 90
low = 35
neutral = 50

print("Hold calibration button on talon")
time.sleep(5)
print("Start calibration?")
input = raw_input("") 

p.ChangeDutyCycle(high)
time.sleep(2)
input = raw_input("Continue calibration?")
time.sleep(2)
p.ChangeDutyCycle(low)
time.sleep(2)
input = raw_input("Continue calibration?")
time.sleep(2)
p.ChangeDutyCycle(neutral)
time.sleep(4)
print("Release Calibration button")
input = raw_input("Button released?")
p.stop()
print("Calibration complete")
GPIO.cleanup()
