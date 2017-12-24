def inverse(a, n):
    t = 0;     newt = 1;    
    r = n;     newr = a;    
    while newr != 0:
        quotient = int(r / newr)
        (t, newt) = (newt, t - quotient * newt) 
        (r, newr) = (newr, r - quotient * newr)
    if t < 0:
         t = t + n
    return t

import pdb
pdb.set_trace()