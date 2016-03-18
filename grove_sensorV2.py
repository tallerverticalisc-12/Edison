import time
import pyupm_servo as servo
import pyupm_grove as grove

# Create the servo object using D5
gServo = servo.ES08A(5)
light_sensor = grove.GroveLight(0)

while True:
	if(light_sensor.value() <= 2):
		gServo.setAngle(90)
		time.sleep(3)
	else:
		gServo.setAngle(0)
		
del gServo
del light_sensor