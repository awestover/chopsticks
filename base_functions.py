# functions used by all v0 and v1s

import pandas as pd
import random
import sys
from universal_functions import *

strategyFile = "strategy.csv"

# gameplay

# get a state from the user
# note must invert state when reading in and writing out for the computer
# but this is done elsewhere
def inputState(state, strategyFile, mod=5):
    nextMove = [-1, -1, -1, -1]
    while not validMove(state, nextMove, mod=mod):
        nextMove = conform(parseState(input("input move values, space seperated\t")))
    addLookupEntry(state, nextMove, strategyFile, mod=mod)
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

# computer move
def advanceState(state, strategyFile, mod=5):
    lookUp = lookUpNextMove(state, strategyFile, mod=mod)
    if lookUp != []:
        return parseState(random.choice(lookUp))
    else:
        return randomState(state, mod=mod)

# csv i/o

# here is how to add to the table
def addLookupEntry(state1, state2, strategyFile, mod=5):
    s1 = listToString(state1)
    s2 = listToString(state2)

    stratCsv = pd.read_csv(modFileName(strategyFile, mod=mod))
    nextStrat = {
        "Previous": s1,
        "Next": s2
    }

    stratCsv = stratCsv.append(nextStrat, ignore_index=True)
    stratCsv = stratCsv[["Previous", "Next"]]
    stratCsv.to_csv(modFileName(strategyFile), index=False)

# looks up a move in the table, returns all recorded next moves
def lookUpNextMove(lastMove, strategyFile, mod=5):
    stratCsv = pd.read_csv(modFileName(strategyFile, mod=mod))
    nexts = []
    for i in range(0, len(stratCsv["Previous"])):
        # real eqaulity check
        if stratCsv["Previous"][i] == listToString(lastMove):
            nexts.append(stratCsv["Next"][i])
    return nexts
