# functions that are used by every version and do not change
import random

# gameplay

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


# csv i/o

# add the modulus to the filename
def modFileName(fileName, mod=5):
    smf = fileName.split(".")
    smf[0] += str(mod)
    smf = ".".join(smf)
    return smf

# turn a list into a string
def listToString(l):
    return " ".join([str(e) for e in l])


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
