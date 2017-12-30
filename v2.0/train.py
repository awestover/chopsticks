"""
Probably should get a better function for fighting (not random opponents)
track growth

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
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
from functions import *
import random
import os


scorePicFile = "scoresPicture.png"
scoreFile = "scores.csv"
bestScores = []
averageScores = []
if os.path.exists(scoreFile):
    os.system("rm " + scoreFile)

red_patch = mpatches.Patch(color='red', label='Best Score')
blue_patch = mpatches.Patch(color='blue', label='Average score')
plt.legend(handles=[red_patch, blue_patch])
plt.title("Score versus generation")
plt.xlabel("Generation")
plt.ylabel("Scores")

# these hyperparameters could stand to be tuned
# Note: you play every oponent twice
POPULATION_SIZE = 3
NUM_GENERATIONS = 1000

MUTATE_RATE = 0.3

POINTS = {
    "win": 1,
    "tie": 0.2,
    "loss": -0.5
}

POPULATION_INITIAL = {
    "survived": 0,
    "mutated": 0,
    "random": 3
}

POPULATION = {
    "survived": 1,
    "mutated": 1,
    "random": 1
}


# the learning loop
for generation in range (0, NUM_GENERATIONS):
    print("Generation " + str(generation))
    if generation == 0:
        brains = nextGen(None, None, POPULATION_INITIAL, None)
        with open(scoreFile, "a+") as f:
            f.write("Best Score,Average Score\n")
    else:
        brains = nextGen(brains, scores, POPULATION, MUTATE_RATE)
        with open(scoreFile, "a+") as f:
            cMax = max(scores)
            bestScores.append(cMax)
            cAvg = sum(scores) / len(scores)
            averageScores.append(cAvg)
            f.write(str( round(cMax,3) ) + "," + str( round(cAvg,3) ) + "\n")
            plt.scatter(list(range(0, generation)), bestScores, c='r')
            plt.scatter(list(range(0, generation)), averageScores, c='b')
            plt.savefig(scorePicFile)

    scores = [0 for i in range(0, POPULATION_SIZE)]
    for brain in range(0, POPULATION_SIZE):
        for match in range(0, POPULATION_SIZE):
            if match != brain:
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
bestStrategy = bestBrain(brains, scores)
writeStrategy(bestStrategy)
