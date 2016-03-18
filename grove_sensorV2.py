
#gorve_sensorV2.py
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
    
import time
import pyupm_servo as servo
import pyupm_grove as grove

# Create the servo object using D5
gServo = servo.ES08A(5)
light_sensor = grove.GroveLight(0)

while True:
	if(light_sensor.value() <= 2):
		gServo.setAngle(90)
		time.sleep(3)
	else:
		gServo.setAngle(0)
		
del gServo
del light_sensor
