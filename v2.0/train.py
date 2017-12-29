# initially random AIs evolve over time
# clean and comment in a later verision

POPULATION_SIZE = 10
MATCHES_PER_GENERATION = 2

MUTATE_RATE = 0.2

POINTS = {
    "win": 1,
    "tie": 0.2,
    "loss": -0.5
}

POPULATION_INITIAL =
{
    "random": 10
}

POPULATION =
{
    "survived": 2,
    "mutated": 2
    "random": 6
}

# random initialization
# brain stucture is as follows
"""
brains = [ Look up tables for all of the computers that will be competing  ]
brains[i] = {"Previous":[Previous], "Nexts":[Nexts] }
"""
brains = []
for i in range(0, POPULATION_INITIAL["random"]):
    brains.append( {"Previous":[], "Nexts":[]} )
# you could add more categories, like inheriting brain initialization from humans

# this determines which brains should survive
scores = [0 for i in range(0, POPULATION_SIZE)]

# turn a list into a string
def listToString(l):
    le = [str(e) for e in l]
    return " ".join(le)

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
                if lastState[i] != 0 and lastState[j] != 0: # 0 hit is not allowed
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
        if nextState[i] < 0 or nextState[i] >= mod:
            return False

    # nothing changed, not valid move
    if lastState == nextState:
        return False

    # you can only hit one hand...
    if nextState[3] != lastState[3] and nextState[2] != lastState[2]:
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

# checks if 2 states are identical
def sameState(state1, state2):
    return state2 in permHands(state1)

# turns a string of numbers with no spaces in between them to a list of integers
def parseNoSpaceString(s):
    s = list(s)
    return [int(i) for i in s]

# parse a string of space seperated values to an array
def parseState(state):
    try:
        state = state.strip().split(" ")
        state = [int(s) for s in state]
    except:
        state = [-1, -1, -1, -1]
    return state

# generates a random state, not neccecarily valid
def randomState(mod=5):
    return [random.randint(0, mod - 1) for i in range(0, 4)]

# computer move
def advanceState(state):
    lookUp = lookUpNextMove(state)
    if lookUp != []:
        return parseState(random.choice(lookUp))
    else:
        r = randomState()
        while gameOver(r) == 1 or not validMove(state, r):
            r = randomState()
        return r

# looks up a move in the table, returns all recorder next moves
def lookUpNextMove(lastMove, brain):
    nexts = [] # this should really only have 1 or zero entries, fix this waste later...
    for i in range(0, len(brain["Previous"])):
        # real eqaulity check
        if sameState(listToString(brain["Previous"][i]), listToString(lastMove)):
            nexts.append(brain["Next"][i])
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
    elif depth > 1000:
        return 0
    else:
        return -1

# simulate a match between brains 1 and 2 and submit the result
def playMatch(brain0, brain1):
    turn = 0
    shift = random.randint(0, 1)  # who goes first?
    state = [1, 1, 1, 1]
    while gameOver(state, depth=turn) == -1:
        if (turn + shift) % 2 == 0:  # brain0
            state = advanceState(state)
        else: # brain1
            state = invertState(state)
            # make the choice
            state =  advanceState(state)
            # we must flip twice
            state = invertState(state)
        turn += 1
    return gameOver(state, depth=turn)

# get the next generation from the last  generation
def nextGen(brains, scores):
    nextBrains = []

    # get some good ones
    topIndices = []
    while len(topIndices) < POPULATION["survived"]:
        nextBest = min(scores)
        achieved = -1
        for idx in range(0, len(brains)):
            if scores[idx] >= nextBest:
                if idx not in topIndices:
                    achieved = idx
                    nextBest = scores[idx]
        topIndices.append(achieved)

    for ti in topIndices:
        nextBrains.append(ti)

    cycle = 0
    for j in range(0, POPULATION["mutated"]):
        nextBrains.append(mutate(brains[topIndices[cycle]]))
        cycle = (cycle + 1) % POPULATION["survived"]

    for k in range(0, POPULATION["random"]):
        nextBrains.append({"Previous":[], "Nexts":[]})

    return nextBrains

def mutate(brain):
    # lose some of your strategy, it will be randomly replaced on a as needed basis
    mutated = []
    for b in brain():
        if random.random() > MUTATE_RATE:
            mutated.append(b)
    return mutated

def writeStrategy(strategy):
    s1 = listToString(state1)
    s2 = listToString(state2)

    nextStrat = {
        "Previous": s1,
        "Next": s2
    }

    stratCsv = stratCsv.append(nextStrat, ignore_index=True)
    stratCsv = stratCsv[["Previous", "Next"]]
    stratCsv.to_csv(strategyFile, index=False)


NUM_GENERATIONS = 10

for generation in range (0, NUM_GENERATIONS):
    for brain in range(0, len(brains)):
        for matches in range(0, MATCHES_PER_GENERATION):
            match = random.randint(0, POPULATION_SIZE)
            while match == brain:
                match = random.randint(0, POPULATION_SIZE)
            result = playMatch(brains[brain], brains[match])
            # UPDATE SCORE
            if result == 1:
                scores[match] += POINTS["loss"]
                scores[brain] += POINTS["win"]
            elif result == 2:
                scores[match] += POINTS["win"]
                scores[brain] += POINTS["loss"]
            elif result == 0: # tie
                scores[match] += POINTS["tie"]
                scores[brain] += POINTS["tie"]
            # no other possibilities, the game can't end with -1 gameOver

    brains = nextGen(brains)
    scores = [0 for i in range(0, POPULATION_SIZE)]

bestStrategy = brains[0]

prevs = []
nexts = []
for s in bestStrategy:
    prevs.append(listToString(s[0]))
    nexts.append(listToString(s[1]))

import pandas as pd
import os
strategyFile = "strategy.csv"
strat = {
    "Previous": prevs,
    "Next": nexts
}
df = pd.DataFrame(strat)
df.to_csv(strategyFile, index=False)
