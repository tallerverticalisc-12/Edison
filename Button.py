import time
import pyupm_grove as grove

# Create the button object using GPIO pin 0
button = grove.GroveButton(3)

# Read the input and print, waiting one second between readings
while 1:
    print button.name(), ' value is ', button.value()
    time.sleep(1)