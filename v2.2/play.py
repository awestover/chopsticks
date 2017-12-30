import sys
sys.path.insert(0, "..")
from universal_functions import *


gameOverPointConversion = {
    -1: 0,
    2: -1,
    1: 1,
    0: 0
}

def scoreMoves(state, maxDepth, mod=5):
    ps = possibleNextMoves(state, mod=mod)
    scores = [0 for i in range(0, len(ps))]
    if maxDepth == 0:
        return gameOverPointConversion[gameOver(state)]
    for p in range(0, len(ps)):
        cur = evaluateMove(p, maxDepth - 1, mod=mod)
        scores[p] = sum(cur) / len(cur)
    return scores

print(scoreMove())
