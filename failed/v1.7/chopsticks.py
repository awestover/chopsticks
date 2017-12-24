from updatePicture import updatePicture
from functions import *
import time
import sys
import os
from tkinter import *

root = Tk()
movePending = True
def pic(file):
    for ele in root.winfo_children():
        ele.destroy()
    photo = PhotoImage(file=file)
    photo_label = Label(image=photo)
    photo_label.grid()
    photo_label.image = photo

strategyFile = "strategy.csv"

if not os.path.exists(strategyFile):
    headDf = pd.DataFrame(columns=["Previous", "Next"])
    headDf.to_csv(strategyFile, index=False)

print("Let's begin")

state = [1, 1, 1, 1]
updatePicture(state)
pic("arenaCurrent.png")
turn = 0
shift = random.randint(0, 1)  # who goes first?
player = input("Would you like to play against me?\n\
Yes-play against computer, No-play against human(y/n)\t")
if "n" in player.lower():
    player = "human"
else:
    player = "computer"

mic = True
micAns = input("Would you like to use the microphone for your speech input?(y/n)")
if len(micAns) > 0:
    if micAns[0].lower() == 'n':
        mic = False

def tryMove():
    global mic
    global state
    global turn
    global shift
    
    # game instance
    if gameOver(state) == -1:
        if (turn + shift) % 2 == 0:  # computer move
            if player == "computer":
                print("My turn")
                time.sleep(0.5)
                state = advanceState(state)
                time.sleep(1)
            else:
                print("Player turn")
                state = inputState(state)
        else:
            print("Player turn")
            promptMove()
            # note the state assumes the current player is listed first
            state = invertState(state)
            # make the choice
            state = inputState(state, mic=mic)
            # we must flip twice
            state = invertState(state)
        turn += 1
        updatePicture(state)
        pic("arenaCurrent.png")
        sayState(state)
    else:
        print("Nice game")
        root.quit()




root.after(2000, tryMove)
root.mainloop()
