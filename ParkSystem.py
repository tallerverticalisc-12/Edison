import requests
import time
import json
import pyupm_grove as grove
import pyupm_i2clcd as lcd
import pyupm_ttp223 as ttp223

#Grove Touch Sensor variable
touchSensor = ttp223.TTP223(2)

#Grove Button variable
button = grove.GroveButton(3)

#Grove LCD Blacklight display variable
lcdDisplay = lcd.Jhd1313m1(0, 0x3E, 0x62)
lcdDisplay.setCursor(0,0)

#Variable to store the json from the server
r = requests.get('http://45.40.137.37:88/bestZone')
parsedJSON = json.loads(r.text)

#Variable to store a formatted json to print
global zone
zone =  parsedJSON['zone']

#Requests the best place to parking
def requestPlace():
    r = requests.get('http://45.40.137.37:88/bestZone')
    print (r.text)
    parsedJSON = json.loads(r.text)

#Request to the server that has the information about the parking zones
def updateInfo(info):
    global dispPlaces
    s = requests.post('http://45.40.137.37:88/sensor', {"zone":1,"parkID":1,"status":info})
    print (s.text)

#Updates if a car leaves or enters to a parking zone    
def parkInfo():
    global dispPlaces
    
    #Detects when a car is in the a determinate spot
    if touchSensor.isPressed():
        updateInfo(1)
    
    #Detects when a car enters to the parking lot             
    if button.value() == 1:
        lcdDisplay.write('Welcome!!!')
        time.sleep(2)
        lcdDisplay.clear()
        lcdDisplay.write('Go to: ' + str(zone))
        updateInfo(0)
        time.sleep(5)
        requestPlace()    
        lcdDisplay.clear()

while True:
    parkInfo()
    

