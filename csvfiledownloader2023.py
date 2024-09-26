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
        pyautogui.moveTo(213, 360) # Remove the date pane
        pyautogui.click()

        pyautogui.moveTo(133, 455)  # Generate report
        pyautogui.click()
        time.sleep(1)
        pyautogui.moveTo(1765, 291) # Download report CSV
        pyautogui.click()
        time.sleep(1)
        
# Set the start and end date for all weekdays in 2023
start_date = '2023-01-01'
end_date = '2023-12-31'

# Generate weekdays from January 1, 2023, to December 31, 2023
weekdays_list = generate_weekdays(start_date, end_date)

# Coordinates for the location where the mouse will click (adjust these values)
x, y = 117, 400

# Call the function to start the typing automation
automate_typing(weekdays_list, x, y)