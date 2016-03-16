import requests
import time
import pyupm_grove as grove
import pyupm_i2clcd as lcd
import pyupm_ttp223 as ttp223

touchSensor = ttp223.TTP223(2)

button = grove.GroveButton(3)

lcdDisplay = lcd.Jhd1313m1(0, 0x3E, 0x62)
lcdDisplay.setCursor(0,0)

dispPlaces = 20

def updateInfo():
    s = requests.post('http://45.40.137.37:88/sensor', {"Places available":str(dispPlaces)})
    time.sleep(5)
    
def parkInfo():
    lcdDisplay.write('Disp parks: ' + str(dispPlaces))
    if touchSensor.isPressed():
        if dispPlaces > 0:
            dispPlaces -= 1
    if button.value() == 1:
        if dispPlaces < 20:
            dispPlaces += 1
    time.sleep(0.3)
    lcdDisplay.clear()
    

while True:
    updateInfo()
    parkInfo()
    

