# https://leetcode.com/problems/count-occurrences-in-text/description/

import pandas as pd

def count_occurrences(files: pd.DataFrame) -> pd.DataFrame:

    bull_cnt = files[files.content.str.contains(' bull ') ].shape[0]
    bear_cnt = files[files.content.str.contains(' bear ') ].shape[0]
    return pd.DataFrame( {'word': ['bull', 'bear'], 
                         'count': [bull_cnt, bear_cnt]})
    
