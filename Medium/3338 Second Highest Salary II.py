# https://leetcode.com/problems/second-highest-salary-ii/

import pandas as pd

def find_second_highest_salary(employees: pd.DataFrame) -> pd.DataFrame:

    # Rank salaries per department (dense rank → distinct salaries)
    employees['rank'] = (
        employees
        .groupby('dept')['salary']
        .rank(method='dense', ascending=False)
    )

    # Select second-highest salary per department
    result = employees[employees['rank'] == 2][['emp_id', 'dept']]

    # Order by emp_id
    result = result.sort_values('emp_id')

    return result
