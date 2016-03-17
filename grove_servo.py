import pyupm_servo as Servo

servo = new Servo.ES08A(2)

servo.setAngle(90)
print "angle set at 90"