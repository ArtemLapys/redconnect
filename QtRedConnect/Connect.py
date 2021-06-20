import os
import pyautogui
#from fabric import *



def start_sec(ip, machine):
    strr = "vncviewer " + ip + ":" + machine
    os.system(strr)
    screen = pyautogui.screenshoot()
    return screen

