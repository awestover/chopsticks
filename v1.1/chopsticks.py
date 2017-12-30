from updatePicture import updatePicture
from drawState import drawState
from speak_functions import *
import time
import sys
import os
sys.path.insert(0, "..")
from base_functions import *
from universal_functions import *

# what modulus is the game played in?
mod = 5
try:
    mod = int(input("what modulus would you like to play in? (answer an integer between 2 and 9 inclusive)\t"))
except:
    pass
if not os.path.exists(modFileName(strategyFile, mod=mod)):
    headDf = pd.DataFrame(columns=["Previous", "Next"])
    headDf.to_csv(modFileName(strategyFile, mod=mod), index=False)

print("Let's begin")

state = [1, 1, 1, 1]
updatePicture(state)
drawState(first=True)
turn = 0
shift = random.randint(0, 1)  # who goes first?
player = input("Would you like to play against me?\n\
Yes-play against computer, No-play against human(y/n)\t")
if "n" in player.lower():
    player = "human"
else:
    player = "computer"

mic = True
micAns = input("Would you like to use the microphone for your speech input?(y/n)\t")
if len(micAns) > 0:
    if micAns[0].lower() == 'n':
        mic = False

# game loop
while gameOver(state) == -1:
    if (turn + shift) % 2 == 0:  # computer move
        if player == "computer":
            print("My turn")
            time.sleep(0.5)
            state = advanceState(state, strategyFile, mod=mod)
            time.sleep(0.5)
        else:
            print("Player turn")
            state = conform(inputState(state, strategyFile, mod=mod))
    else:
        print("Player turn")
        promptMove()
        # note the state assumes the current player is listed first
        state = invertState(state)
        # make the choice
        state = conform(s_inputState(state, strategyFile, mod=mod, mic=mic))
        # we must flip twice
        state = invertState(state)
    turn += 1
    updatePicture(state)
    drawState()
    sayState(state)

print("Nice game")
