# useful functions for the program

import pandas as pd
import random

# variables
strategyFile = "strategy.csv"


# get a state from the user
# note must invert state when reading in and writing out for the computer
# but this is done elsewhere
def inputState(state, mod=5):
    nextMove = [-1, -1, -1, -1]
    while not validMove(state, nextMove):
        nextMove = conform(parseState(input("input move values, space seperated\t")))
    addLookupEntry(state, nextMove)
    return nextMove

def validMove(state, nextState, mod=5):
    return nextState in possibleNextMoves(state, mod=mod)

#
# # doesn't care where the hands are
# # (ie 1343 and 3134 and 3143 and 1334 are considered)
# # all the same
# def validMove(lastState, nextState, mod=5):
#     nextState = fixMod(nextState, mod=mod)
#
#     hit = False
#     switch = False
#
#     # check for a hit, using the modulus
#     # you didnt change your hands, so I hope you changed the other persons...
#     count = 0
#     for i in range(0, 2):
#         for j in range(2, 4):
#             if (lastState[i] + lastState[j]) % mod == nextState[j]:
#                 if lastState[i] != 0 and lastState[j] != 0: # 0 hit is not allowed
#                     count += 1
#     if lastState[0] == lastState[1]:  # cause we double count when there is ambigous hand hit data...
#         count -= 1
#     if count == 1:
#         hit = True
#         # you can not hit and mess with hands, even if it is invalid hand messing
#         if lastState[0] != nextState[0] or lastState[1] != nextState[1]:
#             # flip counts too
#             if lastState[0] != nextState[1] or lastState[1] != nextState[0]:
#                 return False
#
#     # move arround hands
#     # you did not change your hands
#     if lastState[0] != nextState[0] and lastState[1] != nextState[1]:
#         # the sum must be the same though...
#         if lastState[0] + lastState[1] == nextState[0] + nextState[1]:
#             # you didn't just switch the hand locations...
#             # that is not a real move...
#             if lastState[0] != nextState[1]:
#                 switch = True
#                 # you can not switch and mess with hands, even if it is invalid hand messing
#                 if lastState[2] != nextState[2] or lastState[3] != nextState[3]:
#                     return False
#
#
#     if hit and not switch:
#         return True
#     elif not hit and switch:
#         return True
#     return False


# fixes numbers so that they lie within the modulus
# def fixMod(array, mod=5):
#     out = []
#     for a in array:
#         out.append(a % mod)
#     return out
#
# # all reorderings of a hand
# def permHands(state):
#     out = []
#     perms = ["0123", "0132", "1023", "1032"]
#     for i in perms:
#         cur = []
#         c = parseNoSpaceString(i)
#         for el in c:
#             cur.append(state[el])
#         out.append(cur)
#     return out
#
# # checks if 2 states are identical
# def sameState(state1, state2):
#     return state2 in permHands(state1)
#
# # turns a string of numbers with no spaces in between them to a list of integers
# def parseNoSpaceString(s):
#     s = list(s)
#     return [int(i) for i in s]

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
#
# # generates a random state, not neccecarily valid
# def randomState(mod=5):
#     return [random.randint(0, mod - 1) for i in range(0, 4)]

# gets a move from moves that we know are good
def smartRandomState(previousState, mod=5):
    return random.choice(possibleNextMoves(previousState, mod=mod))

# smarter random state, does every possible hit and every possible switch not every possible state
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
        return smartRandomState(state, mod=mod)

# looks up a move in the table, returns all recorder next moves
def lookUpNextMove(lastMove):
    stratCsv = pd.read_csv(strategyFile)
    nexts = []
    for i in range(0, len(stratCsv["Previous"])):
        # real eqaulity check
        if stratCsv["Previous"][i] == listToString(lastMove):
            nexts.append(stratCsv["Next"][i])
    return nexts

# flips the reference frame
def invertState(state):
    return [state[2], state[3], state[0], state[1]]

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


# makes it so that all identical hand states are treated as the same
def conform(state):
    """
    new format is
    [ small big small big]
    without loss of generality
    """
    return [min(state[0], state[1]), max(state[0], state[1]), min(state[2], state[3]), max(state[2], state[3])]
