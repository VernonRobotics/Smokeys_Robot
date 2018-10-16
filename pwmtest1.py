import RPi.GPIO as IO
import time
IO.setwarnings(False)
IO.setmode(IO.BCM)
IO.setup(12,IO.OUT)
p = IO.PWM(12,100)
p.start(25)
time.sleep(4)
IO.cleanup()
