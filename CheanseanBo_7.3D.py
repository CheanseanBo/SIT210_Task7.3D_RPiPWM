import RPi.GPIO as GPIO
import time

#Declare pin number
ledPin = 7
trigPin = 11
echoPin = 12

#Setup all pin of sensors and LED
GPIO.setmode(GPIO.BOARD)
GPIO.setup(ledPin, GPIO.OUT)

GPIO.setup(trigPin, GPIO.OUT)

GPIO.setup(echoPin, GPIO.IN)


#Setup led frequency to 500hz
led = GPIO.PWM(ledPin, 500)
led.start(0)


while(1):
	
	#When the sensor trigger, we then go check on the echo Pin
	GPIO.output(trigPin, GPIO.HIGH)
	time.sleep(0.1)
	GPIO.output(trigPin, GPIO.LOW)
	
	#When the sensor sends a signal we set the data in start
	while GPIO.input(echoPin) == 0:
		#time.time() expresses time in seconds
		start = time.time()
	#When the sensor receive the signal back, we set the data in stop
	while GPIO.input(echoPin) == 1:
		stop = time.time()
	
	#We then calculate the distance by taking the duration multiply by 170, (add 2 zeros to convert to cm)
	distance = (stop - start) * 17000
	
	#If sensor distance is within 1m
	if 0 <= distance <= 100:
		#It sets the DutyCycle percentage, or set the LED brightness in that percentage
		led.ChangeDutyCycle(100 - distance)
	else:
		#Else it would just set the LED off
		led.ChangeDutyCycle(0)

