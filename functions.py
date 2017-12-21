# useful functions for the program

import random
from drawState import *
import pdb

# doesn't care where the hands are
# (ie 1343 and 3134 and 3143 and 1334 are considered)
# all the same
def validMove(lastState, nextState, mod=5):
    if not baseValidMove(lastState, nextState, mod):
        return False
    hit = False
    switch = False

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
        # you can not hit and mess with hands, even if it is invalid hand messing
        if lastState[0] != nextState[0] or lastState[1] != nextState[1]:
            # flip counts too
            if lastState[0] != nextState[1] or lastState[1] != nextState[0]:
                return False

    # move arround hands
    # you did not change your hands
    if lastState[0] != nextState[0] and lastState[1] != nextState[1]:
        # the sum must be the same though...
        if lastState[0] + lastState[1] == nextState[0] + nextState[1]:
            # you didn't just switch the hand locations...
            # that is not a real move...
            if lastState[0] != nextState[1]:
                switch = True
                # you can not switch and mess with hands, even if it is invalid hand messing
                if lastState[2] != nextState[2] or lastState[3] != nextState[3]:
                    return False


    if hit and not switch:
        return True
    elif not hit and switch:
        return True
    return False


# the most obvious things which must be true
def baseValidMove(lastState, nextState, mod=5):
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

    return True # submit for more evaluation

# all reorderings of a hand
def permHands(state):
    out = []
    perms = ["0123", "0132", "1023", "1032"]
    for i in perms:
        cur = []
        c = parseNoSpaceString(i)
        for el in c:
            cur.append(state[el])
        out.append(cur)
    return out

# turns a string of numbers with no spaces in between them to a list of integers
def parseNoSpaceString(s):
    s = list(s)
    return [int(i) for i in s]

# is this a valid state transition?
def stupidValidMove(lastState, nextState, mod=5, base=True):
    hit = False
    switch = False

    if base:
        if not baseValidMove(lastState, nextState, mod):
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
        # you can not hit and mess with hands, even if it is invalid hand messing
        if lastState[0] != nextState[0] or lastState[1] != nextState[1]:
            return False


    # move arround hands
    # you did not change your hands
    if lastState[0] != nextState[0] and lastState[1] != nextState[1]:
        # the sum must be the same though...
        if lastState[0] + lastState[1] == nextState[0] + nextState[1]:
            # you didn't just switch the hand locations...
            # that is not a real move...
            if lastState[0] != nextState[1]:
                switch = True
                # you can not switch and mess with hands, even if it is invalid hand messing
                if lastState[2] != nextState[2] or lastState[3] != nextState[3]:
                    return False


    if hit and not switch:
        return True
    elif not hit and switch:
        return True
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
