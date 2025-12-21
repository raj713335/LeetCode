# https://leetcode.com/problems/get-the-second-most-recent-activity/description/

import pandas as pd

def second_most_recent(user_activity: pd.DataFrame) -> pd.DataFrame:

    return (user_activity.sort_values('endDate')
                         .groupby('username').tail(2)
                         .groupby('username').head(1))
    
