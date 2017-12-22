import pyautogui
import os
import time

def say(string):
    pyautogui.typewrite(list(string))

def enter():
    pyautogui.press("enter")

def command(string):
    say(string)
    enter()

time.sleep(3)
os.system("rm strategy.csv")
command("python chopsticks.py")
command("n")
command("2 0 1 1")
# command("clear")
# command("clear")
