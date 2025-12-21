# https://leetcode.com/problems/calculate-trapping-rain-water/

import pandas as pd

def calculate_trapped_rain_water(heights: pd.DataFrame) -> pd.DataFrame:
    
    df = heights.assign(ones = heights["height"].apply(lambda x: x*[1]))["ones"].apply(pd.Series)
    df2 = (df.ffill() == 1) & (df.bfill() == 1)
    return pd.DataFrame({"total_trapped_water": [((df == 1)^(df2 == 1)).sum().sum()]})
