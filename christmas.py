from pyautogui import*
import pyautogui
import time
import keyboard
import random
import win32api,win32con

time.sleep(2)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


while keyboard.is_pressed('q') == False:
    flag = 0
    pic = pyautogui.screenshot(region=(82,134,698,449))

    width,height = pic.size

    for x in range(0,width,5):
        for y in range(0,height,5):

            r,g,b = pic.getpixel((x,y))

            if r == 74 and g == 74 and b == 74:
                flag = 1
                click(x+82, y+134)
                time.sleep(0.5)
                break

            if flag == 1:
                break
