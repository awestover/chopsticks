from functions import *
import time
import sys
import os

strategyFile = "strategy.csv"

if not os.path.exists(strategyFile):
    headDf = pd.DataFrame(columns=["Previous", "Next"])
    headDf.to_csv(strategyFile, index=False)

print("Let's begin")

state = [1, 1, 1, 1]
turn = 0
shift = random.randint(0, 1)  # who goes first?
player = input("Would you like to play against me?\n\
Yes-play against computer, No-play against human(y/n)\t")
if "n" in player.lower():
    player = "human"
else:
    player = "computer"
# what modulus is the game played in?
mod = 6

# game loop
while gameOver(state, mod=mod) == -1:
    if (turn + shift) % 2 == 0:  # computer move
        if player == "computer":
            print("My turn")
            time.sleep(0.5)
            state = conform(advanceState(state, mod=mod))
            time.sleep(1)
        else:
            print("Player turn")
            state = conform(inputState(state, mod=mod))
    else:
        print("Player turn")
        print(invertState(state))
        # note the state assumes the current player is listed first
        state = invertState(state)
        # make the choice
        state = conform(inputState(state, mod=mod))
        # we must flip twice
        state = invertState(state)
    turn += 1

print("Nice game")
