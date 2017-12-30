from chopsticksIn import *
import win32com.client as wincl
import sys
sys.path.insert(0, "..")
from universal_functions import *
from base_functions import *

# variables
strategyFile = "strategy.csv"
speak = wincl.Dispatch("SAPI.SpVoice")

# speaking interaction functions

# abstraction of speach
def promptMove():
    speak.Speak("Please take a move esteemed user")

# say the state
def sayState(state):
    s = [str(si) for si in state]
    s = " ".join(s)
    speak.Speak("The state is currently " + s)

# get a state from the user
# note must invert state when reading in and writing out for the computer
# but this is done elsewhere
def s_inputState(state, strategyFile, mod=5, mic=True):
    nextMove = [-1, -1, -1, -1]
    while not validMove(state, nextMove):
        if mic:
            print("-"*1000)
            print(nextMove, state)
            nextMove = parseGetIn(state, mod)
        else:
            nextMove = parseState(input("input move values, space seperated\t"))
    addLookupEntry(state, nextMove, strategyFile=strategyFile)
    return nextMove
