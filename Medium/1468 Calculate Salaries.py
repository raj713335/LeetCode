# https://leetcode.com/problems/calculate-salaries/description/

import pandas as pd

def calculate_salaries(salaries: pd.DataFrame) -> pd.DataFrame:

    # Step 1: find max salary per company
    max_salary = salaries.groupby('company_id')['salary'].transform('max')

    # Step 2: determine tax rate per row (based on company max)
    tax_rate = pd.Series(0.0, index=salaries.index)

    tax_rate[(max_salary >= 1000) & (max_salary <= 10000)] = 0.24
    tax_rate[max_salary > 10000] = 0.49

    # Step 3: apply tax and round
    salaries['salary'] = (salaries['salary'] * (1 - tax_rate)).round().astype(int)

    return salaries
    
