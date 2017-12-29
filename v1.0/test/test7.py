import os

os.system("taskkill /f /im Microsoft.Photos.exe")
os.system("python drawCurrentState.py")

"""
kill task, forcefully

TASKKILL /F /IM notepad.exe

taskkill /f /im Microsoft.Photos.exe
tasklist - what tasks?
"""
