#light_sensor.py
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
import pyupm_grove as grove

# Create the light sensor object using AIO pin 0
light = grove.GroveLight(0)

# Read the input and print both the raw value and a rough lux value,
# waiting one second between readings

while 1:
    print light.name() + " raw value is %d" % light.raw_value() + ", which is roughly %d" % light.value() + " lux";
    time.sleep(1)

# Delete the light sensor object
del light
