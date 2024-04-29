# https://leetcode.com/problems/create-a-session-bar-chart/description/

import pandas as pd
import pandas as pd

def create_bar_chart(sessions: pd.DataFrame) -> pd.DataFrame:
    labels=['[0-5>','[5-10>','[10-15>','15 or more']
    sessions['duration_bins'] = pd.cut(sessions['duration'],bins=[0,300,600,900,float('inf')],labels=labels)
    columns={'duration_bins':'bin','count':'total'}
    df = pd.DataFrame(sessions.value_counts(subset='duration_bins')).reset_index().rename(columns=columns)
    return df
    
