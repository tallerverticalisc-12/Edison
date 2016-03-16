import requests
import time
import pyupm_grove as groove
import pyupm_i2clcd as lcd
import pyupm_ttp223 as ttp223

touchSensor = ttp223.TTP223(2)

button = grove.GroveButton(3)

lcdDisplay = lcd.Jhd1313m1(0, 0x3E, 0x62)
lcdDisplay.setCursor(0,0)


dispPlaces = 20

while True:   
    if touchSensor.isPresses()
        dispPlaces -= 1
    if button.value() == 1
        dispPlaces += 1
    lcdDisplay.write('Disponible parks: ' + dispPlaces)
    
    time.sleep(1)

