#TouchSensor.py
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
import pyupm_ttp223 as ttp223
# Create the TTP223 touch sensor object using GPIO pin 0
touch = ttp223.TTP223(3)
# Check whether or not a finger is near the touch sensor and
# print accordingly, waiting one second between readings
while 1:
    if touch.isPressed():
        print touch.name(), 'is pressed'
    else:
        print touch.name(), 'is not pressed'
    time.sleep(1)
# Delete the touch sensor object
del touch
