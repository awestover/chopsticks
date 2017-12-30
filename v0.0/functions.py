# useful functions for the program

import pandas as pd
import random

# variables
strategyFile = "strategy.csv"

# gameplay

# get a state from the user
# note must invert state when reading in and writing out for the computer
# but this is done elsewhere
def inputState(state, mod=5):
    nextMove = [-1, -1, -1, -1]
    while not validMove(state, nextMove, mod=mod):
        nextMove = conform(parseState(input("input move values, space seperated\t")))
    addLookupEntry(state, nextMove)
    return nextMove

# checks if a move is allowed
def validMove(state, nextState, mod=5):
    return nextState in possibleNextMoves(state, mod=mod)

# parse a string of space seperated values to an array
def parseState(state):
    try:
        state = state.strip().split(" ")
        state = [int(s) for s in state]
        if len(state) != 4:
            state = [-1, -1, -1, -1]
    except:
        state = [-1, -1, -1, -1]
    return state

# gets a move from moves that we know are good
def randomState(previousState, mod=5):
    return random.choice(possibleNextMoves(previousState, mod=mod))

# random state, does every possible hit and every possible switch not every possible state, only valid moves allowed
def possibleNextMoves(p, mod=5):
    lc = []  # probably legit hits, still pass it through validMove checker though
    # hits
    for i in range(0, 2):
        for j in range(2, 4):
            if p[i] != 0 and p[j] != 0: # 0 hit is not allowed
                cur = p[:]
                cur[j] = (cur[i] + cur[j]) % mod
                lc.append(conform(cur))
    # switches
    # note these are already conformed
    cc = p[:]
    cc[1] = cc[0] + cc[1]
    cc[0] = 0
    while cc[1] >= cc[0]:
        if cc[1] < mod:
            if cc[0] != p[0]:  # can not be the same strategy you already have
                lc.append(cc[:])
        cc[0] += 1
        cc[1] -= 1
    return lc

# computer move
def advanceState(state, mod=5):
    lookUp = lookUpNextMove(state)
    if lookUp != []:
        return parseState(random.choice(lookUp))
    else:
        return randomState(state, mod=mod)


# is the game over?
def gameOver(state, depth=0):
    p1 = ( state[0] == 0 and state[1] == 0 )
    p2 = ( state[2] == 0 and state[3] == 0 )
    if p1:
        return 1
    elif p2:
        return 2
    elif depth > 100:
        return 0
    else:
        return -1

# csv i/o

# turn a list into a string
def listToString(l):
    return " ".join([str(e) for e in l])

# here is how to add to the table
def addLookupEntry(state1, state2):
    s1 = listToString(state1)
    s2 = listToString(state2)

    stratCsv = pd.read_csv(strategyFile)
    nextStrat = {
        "Previous": s1,
        "Next": s2
    }

    stratCsv = stratCsv.append(nextStrat, ignore_index=True)
    stratCsv = stratCsv[["Previous", "Next"]]
    stratCsv.to_csv(strategyFile, index=False)

# looks up a move in the table, returns all recorded next moves
def lookUpNextMove(lastMove):
    stratCsv = pd.read_csv(strategyFile)
    nexts = []
    for i in range(0, len(stratCsv["Previous"])):
        # real eqaulity check
        if stratCsv["Previous"][i] == listToString(lastMove):
            nexts.append(stratCsv["Next"][i])
    return nexts


# change hands format

# makes it so that all identical hand states are treated as the same
def conform(state):
    """
    new format is
    [ small big small big]
    without loss of generality
    """
    return [min(state[0], state[1]), max(state[0], state[1]), min(state[2], state[3]), max(state[2], state[3])]

# flips the reference frame
def invertState(state):
    return [state[2], state[3], state[0], state[1]]
