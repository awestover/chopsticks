from functions import *
import pandas as pd
import os

strategyFile = "strategyv1.csv"

if not os.path.exists(strategyFile):
    with open(strategyFile, "w") as f:
        f.write("Previous,Next")

print("Let's begin")


state = [1, 1, 1, 1]







#___
