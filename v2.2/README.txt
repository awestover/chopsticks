THIS IS THE RECURSION DELVER
IT IS PURE
IT NEEDS NO STRATEGY.csv file


i think that there is a big probelm in the universal_functions

add this line to possibleNextMoves()
if conform(cur) not in lc:
  lc.append(conform(cur))
Basically we get duplicates if you could hit to the same state multiple ways.
                    
