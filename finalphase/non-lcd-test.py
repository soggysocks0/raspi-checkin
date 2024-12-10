# Import the necessary libraries
from datetime import datetime  # For the timestamps
import time  # Used for the sleep() function
import pygsheets  # Library to communicate with the service account, then to GSheets
import pandas as pd  # For the data structure, ie columns & rows for the GSheet

def Initialize():
    print("Initializing...")

    # Authorize with the Google Sheets API & Service Account
    auth = pygsheets.authorize(service_account_file='/Users/Manuel/Desktop/python/lcd-barcode-sign-in-a7130cdf7e76.json')

    # Set time
    global current_time
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Open the GSheet and select the first sheet
    global wks
    wks = auth.open("TimeClock").sheet1

    # Prepare for data manip
    df = pd.DataFrame(columns=["ID", "Action", "Timestamp"])
    wks.set_dataframe(df, (1, 1))

    print("Initialized!")

Initialize()

# Global/Static variables
signedin = []

def main():
    while True:
        barcodeinput = input("Enter ID: ")

        # Get ID Input
        try:
            barcodeinput = int(barcodeinput)
        except ValueError:
            print("Invalid Input. Input must be an integer.")
            continue

        # Get the time
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Check and sort
        if barcodeinput not in signedin:
            signedin.append(barcodeinput)
            action = "Signed in."
            print("Signed In")
        else:
            signedin.remove(barcodeinput)
            action = "Signed out."
            print("Signed Out")

        # Prepare the data to be added to the sheet
        new_entry = [barcodeinput, action, current_time]

        # Update Sheet
        wks.append_table(new_entry)

        time.sleep(0.5)

main()
