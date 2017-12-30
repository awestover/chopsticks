import pandas as pd
import random

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

# do not make the computer check this, only the human
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


# turns a string of numbers with no spaces in between them to a list of integers
def parseNoSpaceString(s):
    s = list(s)
    return [int(i) for i in s]

# parse a string of space seperated values to an array
# def parseState(state):
#     try:
#         state = state.strip().split(" ")
#         state = [int(s) for s in state]
#     except:
#         state = [-1, -1, -1, -1]
#     return state

# generates a random state, not neccecarily valid
def randomState(mod=5):
    return conform([random.randint(0, mod - 1) for i in range(0, 4)])

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
def advanceState(state, brain, mod=5):
    lookUp = lookUpNextMove(state, brain)
    if lookUp != []:
        return random.choice(lookUp)
    else:
        return smartRandomState(state, mod=5)

# looks up a move in the table, returns all recorder next moves
def lookUpNextMove(lastMove, brain):
    nexts = []
    for i in range(0, len(brain["Previous"])):
        # note that these should be conformed
        if listToString(brain["Previous"][i]) == listToString(lastMove):
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
        print("TIE")
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
            state = advanceState(state, brain1)
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
def nextGen(brains, scores, population_makeup, MUTATE_RATE):
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
        nextBrains.append(mutate(brains[topIndices[cycle]], MUTATE_RATE))
        cycle = (cycle + 1) % population_makeup["survived"]

    for k in range(0, population_makeup["random"]):
        nextBrains.append( {"Previous":[], "Next":[]} )

    return nextBrains

# mutate a strategy
def mutate(brain, MUTATE_RATE):
    # lose some of your strategy, it will be randomly replaced on a as needed basis
    mutated = {"Previous": [], "Next": []}
    for b in range(0, len(brain["Previous"])):
        if random.random() > MUTATE_RATE:  #not a mutation
            mutated["Previous"].append(brain["Previous"][b])
            mutated["Next"].append(brain["Next"][b])
    return mutated

# outputs the final strategy brain to a csv for use against human opponents or something
def writeStrategy(strategy):
    strategyFile = "strategy.csv"
    for s in range(0, len(strategy["Previous"])):
        strategy["Previous"][s] = listToString(strategy["Previous"][s])
        strategy["Next"][s] = listToString(strategy["Next"][s])
    stratCsv = pd.DataFrame(strategy)
    stratCsv = stratCsv[["Previous", "Next"]]
    stratCsv.to_csv(strategyFile, index=False)

# which brain is the best
def bestBrain(brains, scores):
    return brains[scores.index(max(scores))]

# makes it so that all identical hand states are treated as the same
def conform(state):
    """
    new format is
    [ small big small big]
    without loss of generality
    """
    return [min(state[0], state[1]), max(state[0], state[1]), min(state[2], state[3]), max(state[2], state[3])]



#--
