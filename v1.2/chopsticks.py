from updatePicture import updatePicture
from speak_functions import *
import time
import sys
import os
from tkinter import *
import sys
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

root = Tk()
movePending = True
def pic(file):
    for ele in root.winfo_children():
        ele.destroy()
    photo = PhotoImage(file=file)
    photo_label = Label(image=photo)
    photo_label.grid()
    photo_label.image = photo

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
                state = advanceState(state, strategyFile, mod=mod)
                time.sleep(0.5)
            else:
                print("Player turn")
                state = conform(s_inputState(state, strategyFile, mod=mod, mic=mic))
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
        pic("arenaCurrent.png")
        sayState(state)
    else:
        print("Nice game")
        root.quit()




root.after(2000, tryMove)
root.mainloop()
