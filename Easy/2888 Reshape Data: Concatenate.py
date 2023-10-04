# https://leetcode.com/problems/reshape-data-concatenate/description/


import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:

    frames = [df1, df2]
    result = pd.concat(frames)
    return result
    
