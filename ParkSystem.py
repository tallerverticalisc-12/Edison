import requests
import time
import pyupm_grove as grove
import pyupm_i2clcd as lcd
import pyupm_servo as servo
import pyupm_ttp223 as ttp223

light_sensor = grove.GroveLight(0)
touchSensor = ttp223.TTP223(2)
button = grove.GroveButton(3)
gServo = servo.ES08A(5)

lcdDisplay = lcd.Jhd1313m1(0, 0x3E, 0x62)
lcdDisplay.setCursor(0,0)

touchCounter = 0
buttonCounter = 0

dispPlaces = 10

def updateInfo(info):
    global dispPlaces
    s = requests.post('http://45.40.137.37:88/sensor', {"zone":1,"parkID":1,"status":info})
    print (s.text)
    print dispPlaces
    
def parkInfo():
    global dispPlaces
    global touchCounter
    global buttonCounter

    lcdDisplay.write('Disp parks: ' + str(dispPlaces))
    if(light_sensor.value() <= 2):
        gServo.setAngle(90)
        time.sleep(3)
    else:
        gServo.setAngle(0)
    
    if touchSensor.isPressed():
        if dispPlaces < 20:
            disPlaces += 1
            updateInfo(0)
                
    if button.value() == 1:
        if dispPlaces > 0:
            dispPlaces += 1
            updateInfo(1)
        
    time.sleep(0.1)
    lcdDisplay.clear()


 


while True:
    parkInfo()
    

