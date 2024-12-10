'''
This is the final draft of the code
Manuel Aguinaga - 12/6/2024
'''

# Import the neccesary libraries
from RPLCD.i2c import CharLCD 
import smbus # SMBus library so it can communicate with the GPIO board on the RaspberryPi
from datetime import datetime # For the timestamps
import time # Used for the sleep() function
import pygsheets #Library to communicate with the service account, then to GSheets
import pandas as pd # For the data structure, ie columns & rows for the GSheet
bus = smbus.SMBus(1) # SMBus variable
lcd = CharLCD("PCF8574", 0x27) # The memory address the RaspberryPi uses, and the variable to call to the LCD
lcd.cursor_pos(1, 0) # The position of the little blinking underscore on the LCD

# Clear the LCD beforehand and set up the prerequisites

def Initialize():

    lcd.write_string("Initializing...")

    # Authorize with the Google Sheets API & Service Account
    auth = pygsheets.authorize(service_account_file='')
    # Set time
    global current_time
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Set up the Gsheet
    df = pd.DataFrame()
    global wks
    wks = auth.open("TimeClockSignin").sheet1
    wks.set_dataframe(df,(1,1))

    lcd.write_string("Initialized!")
    lcd.clear()
    
Initialize()

def update_sheet(user_id, action, time_stamp):
    
    # Find the next empty row
    row = len(wks.get_all_values()) + 1
    
    # Append data to the sheet
    wks.update_value(f'A{row}', user_id)  # Column A: User ID
    wks.update_value(f'B{row}', action)   # Column B: Action (Signed In/Out)
    wks.update_value(f'C{row}', time_stamp)  # Column C: Timestamp

# Global/Static variables
signedin = []
signedout = []

def main():
    while True:
        
        barcodeinput = int(input('Enter ID: '))
        try:
            if barcodeinput not in signedin:
                signedin.append(barcodeinput)
                action = "Signed in."
                lcd.write_string("Signed in")
                update_sheet(barcodeinput, action, current_time)
        except ValueError:
            print("Invalid Input. Input must be an integer.")
        
        try: 
            if barcodeinput in signedout:
                signedout.remove(barcodeinput)
                action = "Signed out."
                lcd.write_string("Signed out")
        except ValueError:
            print("Invalid Input. Input must be an integer.")

        

        break
