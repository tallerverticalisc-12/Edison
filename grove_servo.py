import time
import pyupm_servo as servo
 
# Create the servo object using D5
gServo = servo.ES08A(5)
gServo.haltPwm()
for i in range(0,5):
    # Set the servo arm to 0 degrees
    gServo.setAngle(0)
    print 'Set angle to 0'
    time.sleep(1)
    # Set the servo arm to 90 degrees
    gServo.setAngle(90)
    print 'Set angle to 90'
    time.sleep(1)
# Delete the servo object
del gServo