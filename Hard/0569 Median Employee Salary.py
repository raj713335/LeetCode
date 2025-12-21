# https://leetcode.com/problems/median-employee-salary/description/

import pandas as pd

def median_employee_salary(employee: pd.DataFrame) -> pd.DataFrame:
    
    employee['rank_asc'] = employee.sort_values(['salary','id'], ascending = [True,True]).groupby('company')['salary'].rank(method='first',ascending=True) 
    employee['rank_des'] = employee.sort_values(['salary','id'], ascending = [False,False]).groupby('company')['salary'].rank(method='first',ascending=False)
    
    df = employee[abs(employee.rank_asc - employee.rank_des) <=1]

    return df[['id','company','salary']]
