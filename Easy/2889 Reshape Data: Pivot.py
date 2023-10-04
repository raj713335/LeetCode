# https://leetcode.com/problems/reshape-data-pivot/description/


import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    
    return weather.pivot_table(index='month',columns='city',values='temperature',aggfunc='max')
    
