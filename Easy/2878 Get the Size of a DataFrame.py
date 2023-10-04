# https://leetcode.com/problems/get-the-size-of-a-dataframe/description/


import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return [players.shape[0], players.shape[1]]
    
