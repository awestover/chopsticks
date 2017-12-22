from functions import *
import os

strategyFile = "strategyv1.csv"

if not os.path.exists(strategyFile):
    headDf = pd.DataFrame(columns=["Previous", "Next"])
    headDf.to_csv(strategyFile, index=False)

print("Let's begin")


state = [1, 1, 1, 1]
turn = 0
shift = random.randint(0, 1)  # who goes first?
player = input("Would you like to play against me?\n\
If not you can play against a human. (y/n)\t")
if player == "y":
    player = "computer"
else:
    player = "human"

# game loop
while gameOver(state) == -1:
    if (turn + shift) % 2 == 0:  # computer move
        if player == "computer":
            print("My turn")
            state = advanceState(state)
        else:
            print("Player turn")
            state = inputState(state)
    else:
        print("Player turn")
        state = inputState(state)
    turn += 1

print("Nice game")


#___
