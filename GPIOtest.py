import RPi.GPIO as GPIO
import time

try:
   import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO! try running with superuser priveledges.")


GPIO.setmode(GPIO.BCM)
GPIO.setup(15,GPIO.OUT)

for num in range(0,10):
    pulse()
    


def pulse():
	GPIO.output(15,1)
	time.sleep(0.5)
	GPIO.output(15,0)


