import pyupm_servo as servo

servo = new servo.ES08A(2)

servo.setAngle(90)
print "angle set at 90"