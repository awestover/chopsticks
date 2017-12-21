from functions import *
import pandas as pd
import os

strategyFile = "strategyv1.csv"

if not os.path.exists(strategyFile):
    with open(strategyFile, "w") as f:
        f.write("Previous,Next")

print("Let's begin")


state = [1, 1, 1, 1]
turn = 0
shift = random.randint(0, 1)  # who goes first?


while gameOver(state) == -1:
    if (turn + shift) % 2 == 0:  # computer move
        print("My turn")
        state = advanceState(state)
    else:
        print("Your turn")
        state = inputState(state)
    turn += 1

print("Nice game")


#___
