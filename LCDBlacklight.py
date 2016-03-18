#LCDBlacklight.py
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

import pyupm_i2clcd as lcd
import time
# Initialize Jhd1313m1 at 0x3E (LCD_ADDRESS) and 0x62 (RGB_ADDRESS)
myLcd = lcd.Jhd1313m1(0, 0x3E, 0x62)
myLcd.setCursor(0,0)
# RGB Blue
#myLcd.setColor(53, 39, 249)
# RGB Red
myLcd.setColor(255, 100, 50)
myLcd.write('Fierro')
myLcd.setCursor(1,2)
myLcd.write('Pariente')
time.sleep(10);
