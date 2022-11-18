import time
import pyautogui
# in terminal before start 
# pip install PyAutoGUI
# pip install Pillow
def locate_image():
    time.sleep(5) #the time you would like to wait 
    #pyautogui.click('minimize.PNG')
    cords_image = pyautogui.locateOnScreen('a1.PNG') #The image details
    cords_center = pyautogui.center(cords_image)
    pyautogui.click(cords_center[0]+110, cords_center[1])
    print(cords_image, cords_center)
    exit()

locate_image()
