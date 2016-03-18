#ParkSystem.py
#Copyright (C) 2016  Smart Parking

#TThis program is free software: you can redistribute it and/or modify
    #it under the terms of the GNU General Public License as published by
    #the Free Software Foundation, either version 3 of the License, or
    #(at your option) any later version.

    ##This program is distributed in the hope that it will be useful,
    #but WITHOUT ANY WARRANTY; without even the implied warranty of
    #MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    #GNU General Public License for more details.

    #You should have received a copy of the GNU General Public License
    #along with this program.  If not, see <http://www.gnu.org/licenses/>.

import requests
import time
import json
import pyupm_grove as grove
import pyupm_i2clcd as lcd
import pyupm_servo as servo
import pyupm_ttp223 as ttp223

#light_sensor = grove.GroveLight(0)
touchSensor = ttp223.TTP223(2)
button = grove.GroveButton(3)
gServo = servo.ES08A(5)

lcdDisplay = lcd.Jhd1313m1(0, 0x3E, 0x62)
lcdDisplay.setCursor(0,0)

touchCounter = 0
buttonCounter = 0

dispPlaces = 20
r = requests.get('http://45.40.137.37:88/bestZone')
parsedJSON = json.loads(r.text)
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
    global touchCounter
    global buttonCounter
    
    if touchSensor.isPressed():
        if dispPlaces > 0:
            dispPlaces += 1
            updateInfo(1)
                
    if button.value() == 1:
        if dispPlaces > 0:
            dispPlaces -= 1
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
    

