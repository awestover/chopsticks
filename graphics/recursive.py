# try to play it good


# might want to give slight weight to the strategies that take longer to lose...
# doesn't really work. Might need to "work backwards" from the tree

from universal_functions import *
import pdb

gameOverPointConversion = {
    -1: 0,
    2: 1,
    1: -1,
    0: 0
}

# def scoreMoves(state, traversed=[], mod=5):
#     ps = possibleNextMoves(state, mod=mod)
#     scores = [0 for i in range(0, len(ps))]

#     if gameOver(state) != -1:
#         return [gameOverPointConversion[gameOver(state)]], ps
#     for p in range(0, len(ps)):
#         notYet = True
#         for j in range(0, len(traversed)):
#             if j % 2 == len(traversed) % 2:  # same player...
#                 if traversed[j] == ps[p]:
#                     notYet = False
#                     break
#         if notYet:
#             cur = propogate_invert_scores(scoreMoves(invertState(ps[p]), traversed+[ps[p]], mod=mod)[0])
#             scores[p] = sum(cur) / len(cur)

#     return scores, ps


def adversarial(state, traversed=[], mod=5):
    print(state)
    ps = possibleNextMoves(state, mod=mod)
    scores = [0 for i in range(0, len(ps))]

    if gameOver(state) != -1:
        return [gameOverPointConversion[gameOver(state)]], ps, state
    for p in range(0, len(ps)):
        notYet = True
        for j in range(0, len(traversed)):
            if j % 2 == len(traversed) % 2:  # same player...
                if traversed[j] == ps[p]:
                    notYet = False
                    break
        if notYet:
            cur = propogate_invert_scores(adversarial(invertState(ps[p]), traversed+[ps[p]], mod=mod)[0])
            scores[p] = max(cur)

    if len(traversed)>10:
        pdb.set_trace()

    return scores, ps, ps[scores.index(max(scores))]


def propogate_invert_scores(array):
    out = []
    for a in array:
        out.append(-1*a)
    return out


state = [1, 1, 1, 1]

while gameOver(state) == -1:
    print(state)
    state = adversarial(state, mod=3)[2]

    print(adversarial(state, mod=3))
    state = invertState(state)
    pdb.set_trace()

