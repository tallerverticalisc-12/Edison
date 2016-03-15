import time, sys, signal, atexit
import pyupm_at42qt1070 as upmAt42qt1070

# functions
def printButtons(touchObj):
	buttonPressed = False
	buttons = touchObj.getButtons()

	sys.stdout.write("Buttons Pressed: ")
	for i in range(7):
		if (buttons & (1 << i)):
			sys.stdout.write(str(i) + " ")
			buttonPressed = True

	if (not buttonPressed):
		sys.stdout.write("None")

	print " "

	if (touchObj.isCalibrating()):
		print "Calibration is occurring."

	if (touchObj.isOverflowed()):
		print "Overflow was detected."


# Global code that runs on startup

I2C_BUS = upmAt42qt1070.AT42QT1070_I2C_BUS
DEFAULT_I2C_ADDR = upmAt42qt1070.AT42QT1070_DEFAULT_I2C_ADDR

# Instantiate an AT42QT1070 on I2C bus 0
myTouchSensor = upmAt42qt1070.AT42QT1070(I2C_BUS,
                                         DEFAULT_I2C_ADDR)


# Exit handlers
def SIGINTHandler(signum, frame):
	raise SystemExit

def exitHandler():
	print "Exiting"
	sys.exit(0)


# This function lets you run code on exit, including functions from myTouchSensor
atexit.register(exitHandler)
# This function stops python from printing a stacktrace when you hit control-C
signal.signal(signal.SIGINT, SIGINTHandler)


# Print the button being touched every 0.1 seconds
while(1):
	myTouchSensor.updateState()
	printButtons(myTouchSensor)
	time.sleep(.1)