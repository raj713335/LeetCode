# https://leetcode.com/problems/count-apples-and-oranges/description/

import pandas as pd

def count_apples_and_oranges(boxes: pd.DataFrame, chests: pd.DataFrame) -> pd.DataFrame:

    df = pd.merge(boxes, chests, on='chest_id', how='left')
    df = df.fillna(0)

    apple = 0
    oranges = 0

    for index, row in df.iterrows():
        apple += row['apple_count_x'] + row['apple_count_y']
        oranges += row['orange_count_x'] + row['orange_count_y']

    return pd.DataFrame({
        'apple_count': [apple],
        'orange_count': [oranges]
    })

   
