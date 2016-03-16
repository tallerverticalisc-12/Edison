import requests
import time
import pyupm_grove as grove
import pyupm_i2clcd as lcd
import pyupm_ttp223 as ttp223

touchSensor = ttp223.TTP223(2)

button = grove.GroveButton(3)

lcdDisplay = lcd.Jhd1313m1(0, 0x3E, 0x62)
lcdDisplay.setCursor(0,0)

touchCounter = 0
buttonCounter = 0

dispPlaces = 20


def updateInfo(info):
    global dispPlaces
    s = requests.post('http://45.40.137.37:88/sensor', {info:"Zone 1"}
    print (s.text)
    
def parkInfo():
    global dispPlaces
    global touchCounter
    global buttonCounter
    
    lcdDisplay.write('Disp parks: ' + str(dispPlaces))
    if touchSensor.isPressed():
        touchCounter += 1
        if touchCounter == 2:
            if dispPlaces > 0:
                dispPlaces -= 1
                touchCounter = 0
                updateInfo("A place has been taken in")
                
    if button.value() == 1:
        buttonCounter += 1
        if buttonCounter == 2:
            if dispPlaces < 20:
                dispPlaces += 1
                buttonCounter = 0
                updateInfo("A place has been disoccupied in")
    time.sleep(0.1)
    lcdDisplay.clear()

while True:
    parkInfo()
    

