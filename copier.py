import time
import pyautogui

def maskin():
        
    for i in range (260):
        pyautogui.moveTo(463, 289)
        pyautogui.click()
        time.sleep(0.2)
        pyautogui.keyDown("ctrl")
        pyautogui.press("a")
        time.sleep(0.2)
        pyautogui.press("c")
        time.sleep(0.2)



        pyautogui.moveTo(1387, 755)
        pyautogui.click()
        time.sleep(0.2)
        pyautogui.keyDown("ctrl")
        pyautogui.press("v")
        time.sleep(0.2)


        pyautogui.moveTo(722, 846)
        pyautogui.click()
        time.sleep(3)
        



maskin()