"""
initially random AIs evolve over time
clean and comment in a later verision
Notes:
scores is the array that determines who shall live and who shall die
it is just a point value (reset every generation) indicating how good you are

brains is the list of look up tables for each competitor
brains = [ Look up tables for all of the computers that will be competing  ]
brains[i] = {"Previous":[Previous], "Next":[Next] }

population dictionaries specify the makeup of a population
later add more categories like inheriting brain initialization from humans later

"""

import pdb
import random

# these hyperparameters could stand to be tuned
POPULATION_SIZE = 10
MATCHES_PER_GENERATION = 2

MUTATE_RATE = 0.2

POINTS = {
    "win": 1,
    "tie": 0.2,
    "loss": -0.5
}

POPULATION_INITIAL = {
    "survived": 0,
    "mutated": 0,
    "random": 10
}

POPULATION = {
    "survived": 2,
    "mutated": 2,
    "random": 6
}


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
def advanceState(state, brain):
    lookUp = lookUpNextMove(state, brain)
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
            prevState = state[:]
            state = advanceState(state, brain0)
            brain0 = addEntry(brain0, prevState, state)
        else: # brain1
            state = invertState(state)
            # copy the old state
            prevState = state[:]
            # make the choice
            state =  advanceState(state, brain1)
            brain1 = addEntry(brain1, prevState, state)
            # we must flip twice
            state = invertState(state)
        turn += 1
    return gameOver(state, depth=turn), brain0, brain1

# add an entry to the look up table
def addEntry(brain, prevState, state):
    brain["Previous"].append(prevState)
    brain["Next"].append(state)
    return brain

# get the next generation from the last  generation
def nextGen(brains, scores, population_makeup):
    nextBrains = []

    # get some good ones
    topIndices = []
    while len(topIndices) < population_makeup["survived"]:
        nextBest = min(scores)
        achieved = -1
        for idx in range(0, len(brains)):
            if scores[idx] >= nextBest:
                if idx not in topIndices:
                    achieved = idx
                    nextBest = scores[idx]
        topIndices.append(achieved)

    for ti in topIndices:
        nextBrains.append(brains[ti])

    cycle = 0
    for j in range(0, population_makeup["mutated"]):
        nextBrains.append(mutate(brains[topIndices[cycle]]))
        cycle = (cycle + 1) % population_makeup["survived"]

    for k in range(0, population_makeup["random"]):
        nextBrains.append( {"Previous":[], "Next":[]} )

    return nextBrains

def mutate(brain):
    # lose some of your strategy, it will be randomly replaced on a as needed basis
    mutated = {"Previous": [], "Next": []}
    for b in range(0, len(brain["Previous"])):
        if random.random() > MUTATE_RATE:  #not a mutation
            mutated["Previous"].append(brain["Previous"][b])
            mutated["Next"].append(brain["Next"][b])
    return mutated

# outputs the final strategy brain to a csv for use against human opponents or something
def writeStrategy(strategy):
    for s in range(0, len(strategy["Previous"])):
        strategy["Previous"][s] = listToString(strategy["Previous"][s])
        strategy["Next"][s] = listToString(strategy["Next"][s])
    stratCsv = pd.DataFrame(strategy)
    stratCsv = stratCsv[["Previous", "Next"]]
    stratCsv.to_csv(strategyFile, index=False)


NUM_GENERATIONS = 10

for generation in range (0, NUM_GENERATIONS):
    if generation == 0:
        brains = nextGen(None, None, POPULATION_INITIAL)
    else:
        brains = nextGen(brains, scores, POPULATION)
    scores = [0 for i in range(0, POPULATION_SIZE)]
    for brain in range(0, POPULATION_SIZE):
        for matches in range(0, MATCHES_PER_GENERATION):
            match = brain  # initialize to fail case just cause
            while match == brain:
                match = random.randint(0, POPULATION_SIZE - 1)
            res = playMatch(brains[brain], brains[match])
            brains[brain] = res[1]
            brains[match] = res[2]
            result = res[0]
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


# this is not correct, we want the best brain, fix later
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
