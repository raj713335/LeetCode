# https://leetcode.com/problems/drop-missing-data/description/

import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:

    return students.dropna()
    
