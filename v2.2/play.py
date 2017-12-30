import sys
sys.path.insert(0, "..")
from universal_functions import *


gameOverPointConversion = {
    -1: 0,
    2: -1,
    1: 1,
    0: 0
}

invertScores = {
    0: 0,
    -1: 1,
    1: -1
}

def scoreMoves(state, maxDepth, mod=5):
    ps = possibleNextMoves(state, mod=mod)
    scores = [0 for i in range(0, len(ps))]
    if maxDepth == 0:
        return gameOverPointConversion[gameOver(state)]
    for p in range(0, len(ps)):
        cur = propogate_invert_scores(scoreMoves(invertState(p), maxDepth - 1, mod=mod))
        scores[p] = sum(cur) / len(cur)
    return scores

def propogate_invert_scores(array):
    out = []
    for a in array:
        out.append(invertScores[a])
    return out

print(scoreMoves([1,1,1,1], 3))
