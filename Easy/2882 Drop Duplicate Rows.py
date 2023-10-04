# https://leetcode.com/problems/drop-duplicate-rows/description/


import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:

    return customers.drop_duplicates(subset=['email'])
    
