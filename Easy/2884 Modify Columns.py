# https://leetcode.com/problems/modify-columns/description/

import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:

    employees['salary'] = employees['salary'] * 2
    
    return employees
    
