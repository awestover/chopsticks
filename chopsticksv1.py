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
shift = np.random.randint(0, 1)  # who goes first?


while gameOver(state) == -1:
    if (turn + shift) % 2 == 0:  # computer move
        state = advanceState(state)
    else:
        state = inputState(state)




#___
