# useful functions for the program

import random
from drawState import *

# is this a valid state transition?
def validMove(lastState, nextState, mod=5):
    switch = False
    hit = False

    # nothing changed, not valid move
    if lastState == nextState:
        return False

    # move arround hands
    if lastState[0] + lastState[1] == nextState[0] + nextState[1]:
        # you didn't just switch the hand locations...
        # that is not a real move...
        if lastState[0] != nextState[1]:
            switch = True

    # check for a hit, using the modulus


    if switch and not hit:
        return True
    elif not switch and hit:
        return True
    else:
        return False

# get a state from the user
def inputState(state, mod=5):
    drawState(state)
    nextMove = input("input a move values are space seperated\t")
    nextMove = nextMove.split(" ").strip()
    if validMove()


# computer move
def advanceState(state):
    return [random.randint(0, 4) for i in range(0, 4)]

# flips the reference frame
def invertState(state):
    return [state[2], state[3], state[0], state[1]]

# is the game over?
def gameOver(state):
    p1 = ( state[0] == 0 and state[1] == 0 )
    p2 = ( state[2] == 0 and state[3] == 0 )
    if p1:
        return 1
    elif p2:
        return 2
    # elif tie:
    #     return 0
    else:
        return -1
    # note the slight bias towards player 1
    # is irrelevant except in mod 1 where p1 will
    # lose by this algorithm, when it should really be a tie

    # tie criteria (0) (ie detect infinite loop)
    # may be nessecary.... later








#_____
