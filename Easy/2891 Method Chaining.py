# https://leetcode.com/problems/method-chaining/description/


import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    
    return animals.query("weight > 100").sort_values(by="weight", ascending=False)[["name"]]
    
