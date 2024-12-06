# code written by manuel aguinaga

'''
the code is a very rough test of how it would function, it doesn't properly display signouts, nor does it actually commmunicate with the lcd
'''

# make sure to look at the readme n stuff
import pygsheets
import pandas as pd
from datetime import datetime
#import time # get the time library for the sleep function
#import smbus # smbus library so it can communicate w/ the gpio board or something
#from RPLCD.i2c import CharLCD # import the lcd libraries
#bus = smbus.SMBus(1) # smbus 
#lcd = CharLCD("PCF8574", 0x27) # the memory address
#lcd.cursor_pos(1, 0) # set the cursor position (aka the blinking underscore or whatever)

#lcd.clear() # clear lcd screen

#lcd.write_string("hello world test") # write to the lcd
#time.sleep(0) # function to make the program wait b4 proceeding

# test code

#barcodeinput = input("input test: ")
#lcd.write_string("checked in")

  gc = pygsheets.authorize(service_file='lalalalalala') # ur service account key thing

# Create empty dataframe
df = pd.DataFrame()

signedin = [] # list of the logged ids


# open the spreadsheet, and the name of said spread sheet
wks = gc.open('TimeClockSignin').sheet1

while True:
    #update the first sheet with df, starting at cell B2. 
    wks.set_dataframe(df,(1,1))

    barcodeinput = int(input("Scan ID: ")) # thinking of sanitizing inputs incase someone scans an id that has a string or something, but what are the chances?

    # the time 
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')


    # stuff to check where the id should go
    if barcodeinput in signedin:
        print("Signed Out")
        action = "Signed Out"
        signedin.remove(barcodeinput)
    elif barcodeinput not in signedin:
        print("Signed in")
        action = "Signed In"
        signedin.append(barcodeinput)
        
    else:
        print("Invalid")
        
    print(signedin)

    # whether it was a sign in or out
    actions = [action] * len(signedin)
    
    # write to the sheet

    # Create a column
    df = pd.DataFrame(list(zip(signedin, [current_time] * len(signedin), actions)), columns=['ID', 'Timestamp', 'Action'])

    # where to organize it
    wks.set_dataframe(df, (1, 1), extend=True)

# i couldnt be bothered to rewrite a fat chunk of code so it can display the actions seperately. for now, this works (maybe better)
