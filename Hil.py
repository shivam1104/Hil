import pyautogui
import time


pyautogui.FAILSAFE = False
pyautogui.moveTo(100, 150)
print("Script starting")
while(1==1):
	
	if(pyautogui.position()!=(100,150)):
		break
	else:
		pyautogui.moveTo(100, 150)
		time.sleep(0.2)
		pyautogui.moveTo(200, 250)
		time.sleep(0.2)
		pyautogui.moveTo(100, 150)
		pyautogui.FAILSAFE = False
print("Terminiating")
pyautogui.FAILSAFE = False