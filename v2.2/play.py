import sys
sys.path.insert(0, "..")
from universal_functions import *


gameOverPointConversion = {
    -1: 0,
    2: 1,
    1: -1,
    0: 0
}

def scoreMoves(state, maxDepth, mod=5):
    ps = possibleNextMoves(state, mod=mod)
    scores = [0 for i in range(0, len(ps))]

    if maxDepth == 0 or gameOver(state) != -1:
        return [gameOverPointConversion[gameOver(state)]], ps
    for p in range(0, len(ps)):
        cur = propogate_invert_scores(scoreMoves(invertState(ps[p]), maxDepth - 1, mod=mod)[0])
        scores[p] = sum(cur) / len(cur)

    return scores, ps

def propogate_invert_scores(array):
    out = []
    for a in array:
        out.append(-1*a)
    return out


state = [0, 4, 1, 1]
print(state)
print(scoreMoves(state, 3))
