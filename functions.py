# useful functions for the program

import random
from drawState import *

# is this a valid state transition?
def validMove(lastState, nextState, mod=5):
    switch = False
    hit = False

    # wrong size!
    if len(nextState) != 4:
        return False

    # no negative hands! (by convention)
    for i in range(0, 4):
        if nextState[i] < 0:
            return False

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
    # you didnt change your hands, so I hope you changed the other persons...
    if lastState[0] == nextState[0] and lastState[1] == nextState[1]:
        count = 0
        for i in range(0, 2):
            for j in range(2, 4):
                if (lastState[i] + lastState[j]) % mod == nextState[j]:
                    count += 1
        if count > 1:
            return False
        elif count == 1:
            hit = True

    if switch and not hit:
        return True
    elif not switch and hit:
        return True
    else:
        return False

# parse a string of space seperated values to an array
def parseState(state):
    try:
        state = state.strip().split(" ")
        state = [int(s) for s in state]
    except:
        state = [-1, -1, -1, -1]
    return state

# get a state from the user
def inputState(state, mod=5):
    drawState(state)
    nextMove = [-1, -1, -1, -1]
    while not validMove(nextMove):
        nextMove = parseState(input("input move values, space seperated\t"))
    drawState(nextMove)
    return nextMove

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
