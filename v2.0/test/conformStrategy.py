import os

if os.path.exists("strategyConformed.csv"):
    os.remove("strategyConformed.csv")


f = open("strategy0.csv", "r")
f2 = open("strategyConformed.csv", "a+")


# makes it so that all identical hand states are treated as the same
def conform(state):
    """
    new format is
    [ small big small big]
    without loss of generality
    """
    return [min(state[0], state[1]), max(state[0], state[1]), min(state[2], state[3]), max(state[2], state[3])]

# parse a string of space seperated values to an array
def parseState(state):
    try:
        state = state.strip().split(" ")
        state = [int(s) for s in state]
    except:
        state = [-1, -1, -1, -1]
    return state

# turn a list into a string
def listToString(l):
    le = [str(e) for e in l]
    return " ".join(le)

ct = False
for r in f:
    for c in r.replace("\n", "").split(","):
        ct = not ct
        n = listToString(conform(parseState(c)))
        if "-1" in n:
            f2.write(c)
        else:
            f2.write(n)
        if ct:
            f2.write(",")
    f2.write("\n")
