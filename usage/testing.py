# code written by manuel aguinaga

# make sure to look at the readme n stuff

import time # get the time library for the sleep function
import smbus # smbus library so it can communicate w/ the gpio board or something
from RPLCD.i2c import CharLCD # import the lcd libraries
bus = smbus.SMBus(1) # smbus 
lcd = CharLCD("PCF8574", 0x27) # the memory address
lcd.cursor_pos(1, 0) # set the cursor position (aka the blinking underscore or whatever)

lcd.clear() # clear lcd screen

lcd.write_string("hello world test") # write to the lcd
time.sleep(0) # function to make the program wait b4 proceeding

# test code

barcodeinput = input("input test: ")
lcd.write_string("checked in") 
