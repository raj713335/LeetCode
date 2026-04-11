# https://leetcode.com/problems/tasks-count-in-the-weekend/description/

import pandas as pd

def count_tasks(tasks: pd.DataFrame) -> pd.DataFrame:

    weekend_days = tasks.submit_date.dt.dayofweek.isin({5,6}).sum()

    return pd.DataFrame({'weekend_cnt':[weekend_days],
                         'working_cnt':[tasks.shape[0] - weekend_days]})
    
