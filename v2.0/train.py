# have a lot of initially random AIs evolve over time

# by convention brains[0] is the current best if a best exists

POPULATION_SIZE = 10
MATCHES_PER_GENERATION = 2

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
brains = []
braind.append([[] for i in range(0, POPULATION_INITIAL["random"])])
# you could add more categories, like inheriting brain initialization from humans

# turn a list into a string
def listToString(l):
    le = [str(e) for e in l]
    return " ".join(le)

# simulate a match between brains 1 and 2 and submit the edits
def playMatch(brain1, brain2):
    pass

# get the next generation from the last  generation
def nextGen(brains):
    pass

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
            brains = playMatch(brains, brain, match)
    brains = nextGen(brains)

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
