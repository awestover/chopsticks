# useful functions for the program

from chopsticksIn import *
try:
    import pyttsx3 as pyttsx
except:
    import pyttsx
import pandas as pd
import random
import sys
sys.path.insert(0, "..")
from universal_functions import *
from base_functions import *


# variables
strategyFile = "strategy.csv"
engine = pyttsx.init()

# speaking interaction functions

# says something
def speak(text):
    engine.say(text)
    engine.runAndWait()


# abstraction of speach
def promptMove():
    speak("Please take a move esteemed user")

# say the state
def sayState(state):
    s = [str(si) for si in state]
    s = " ".join(s)
    speak("The state is currently " + s)

# get a state from the user
# note must invert state when reading in and writing out for the computer
# but this is done elsewhere
def s_inputState(state, strategyFile, mod=5, mic=True):
    nextMove = [-1, -1, -1, -1]
    while not validMove(state, nextMove):
        if mic:
            print("-"*1000)
            print(nextMove, state)
            nextMove = conform(parseGetIn(state, mod))
        else:
            nextMove = parseState(input("input move values, space seperated\t"))
    addLookupEntry(state, nextMove, strategyFile=strategyFile)
    return nextMove
