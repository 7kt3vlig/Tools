import pyautogui
import time


def scroll():

    pyautogui.moveTo(1000, 700)
    pyautogui.scroll(700)
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'printscreen')
    time.sleep(0.5)
    pyautogui.moveTo(1000, 710)
    time.sleep(0.5)
    pyautogui.click()

    # pyautogui.moveTo(565, 186)
    # time.sleep(0.5)
    # pyautogui.click()
    # pyautogui.click()
    # time.sleep(0.5)
    # pyautogui.click()
    # pyautogui.click()


    pyautogui.moveTo(795, 533)
    time.sleep(1)
    pyautogui.click()



for i in range(1000):

    scroll()

# for i in range(1000):

#     pyautogui.moveTo(1000, 700)
#     pyautogui.scroll(700)
#     time.sleep(1)
#     pyautogui.hotkey('ctrl', 'printscreen')
#     time.sleep(2)
#     pyautogui.moveTo(1000, 730)
#     time.sleep(2)
#     pyautogui.click()