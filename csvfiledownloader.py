import pyautogui
from datetime import datetime, timedelta
import time

def generate_weekdays(start_date, end_date):
    # Convert start_date and end_date to datetime objects
    current_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')
    
    weekdays = []
    
    # Loop through each day from start_date to end_date
    while current_date <= end_date:
        # Check if it's a weekday (Monday to Friday)
        if current_date.weekday() < 5:  # 0 = Monday, 4 = Friday
            weekdays.append(current_date.strftime('%Y-%m-%d'))
        # Move to the next day
        current_date += timedelta(days=1)
    
    return weekdays

def automate_typing(weekdays_list, x, y):
    # Introduce a small delay to give time to focus on the desired window
    time.sleep(5)  # Time to switch to the application where you want to type
    
    # Loop through each date and perform the actions
    for day in weekdays_list:
        pyautogui.moveTo(x, y)      # Move the mouse to the specified coordinates
        pyautogui.click()           # Perform the first click
        pyautogui.click()  
        pyautogui.click()          
        pyautogui.typewrite(day)
        pyautogui.moveTo(213, 360) #remove the date pane 
        pyautogui.click()

        pyautogui.moveTo(133, 455) #generate report 
        pyautogui.click()
        time.sleep(1)
        pyautogui.moveTo(1765, 291)
        pyautogui.click() #download report csv
        time.sleep(1)
        


# Get yesterday's date
yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')

# Generate weekdays from 1st January 2024 to yesterday
start_date = '2024-01-01'
weekdays_list = generate_weekdays(start_date, yesterday)

# Coordinates for the location where the mouse will click (adjust these values)
x, y = 117, 400

# Call the function to start the typing automation
automate_typing(weekdays_list, x, y)