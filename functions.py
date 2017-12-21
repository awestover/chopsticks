# useful functions for the program

def validMove(lastState, nextState, mod=5):
    switch = 1
    hit = 1

def invertState(state):
    return [state[2], state[3], state[0], state[1]]

def gameOver(state):
    p1 = state[0] == 0 and state[1] == 0
    p2 = state[2] == 0 and state[3] == 0
    if p1:
        return 1
    elif p2:
        return 2
    else:
        return 0
    # note the slight bias towards player 1
    # is irrelevant except in mod 1 where p1 will
    # lose by this algorithm, when it should really be a tie

    # tie criteria (ie detect infinite loop)
    # may be nessecary.... later




#_____
