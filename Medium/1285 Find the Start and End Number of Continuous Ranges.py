# https://leetcode.com/problems/find-the-start-and-end-number-of-continuous-ranges/description/

import pandas as pd

def find_continuous_ranges(logs: pd.DataFrame) -> pd.DataFrame:

    start = logs.loc[0, 'log_id']
    end = logs.loc[0, 'log_id'] - 1

    res = []

    for index, row in logs.iterrows():
        if row['log_id'] == end + 1:
            end = row['log_id']
        else:
            res.append([start, end])
            start = row['log_id']
            end = row['log_id']

    res.append([start, end])

    return pd.DataFrame(res, columns=['start_id', 'end_id'])
    
