# useful functions for the program

import random
from drawState import *
import pdb

# is this a valid state transition?
def validMove(lastState, nextState, mod=5):

    pdb.set_trace()
    hit = False
    switch = False

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

    # check for a hit, using the modulus
    # you didnt change your hands, so I hope you changed the other persons...
    count = 0
    for i in range(0, 2):
        for j in range(2, 4):
            if (lastState[i] + lastState[j]) % mod == nextState[j]:
                if lastState[i] != 0 and lastState[0] != 0: # 0 hit is not allowed
                    count += 1
    if lastState[0] == lastState[1]:  # cause we double count when there is ambigous hand hit data...
        count -= 1
    if count == 1:
        hit = True

    # move arround hands
    # you did not change your hands
    if lastState[0] != nextState[0] and lastState[1] != nextState[1]:
        # the sum must be the same though...
        if lastState[0] + lastState[1] == nextState[0] + nextState[1]:
            # you didn't just switch the hand locations...
            # that is not a real move...
            if lastState[0] != nextState[1]:
                switch = True

    return False  # default


# parse a string of space seperated values to an array
def parseState(state):
    try:
        state = state.strip().split(" ")
        state = [int(s) for s in state]
    except:
        state = [-1, -1, -1, -1]
    return state

# get a state from the user
# note must invert state when reading in and writing out for the computer
def inputState(s, mod=5):
    state = invertState(s)
    drawState(state)
    nextMove = [-1, -1, -1, -1]
    while not validMove(state, nextMove):
        nextMove = parseState(input("input move values, space seperated\t"))
    drawState(nextMove)
    return invertState(nextMove)

# generates a random state, not neccecarily valid
def randomState(mod=5):
    return [random.randint(0, 4) for i in range(0, 4)]

# computer move
def stupidAdvanceState(state):
    r = randomState()
    while gameOver(r) == 1 or not validMove(state, r):
        r = randomState()
        drawState(r)
    return r

# computer move
def advanceState(state):
    r = randomState()
    while gameOver(r) == 1 or not validMove(state, r):
        r = randomState()
        drawState(r)
    return r

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
