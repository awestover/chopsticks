import pandas as pd
import os
strategyFile = "strategy.csv"
strat = {
    "Previous": ["11112341", "asdfasdf23422"],
    "Next": ["22123422", "331234433"]
}
df = pd.DataFrame(strat)
df.to_csv(strategyFile, index=False)
