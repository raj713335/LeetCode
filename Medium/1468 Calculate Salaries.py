# https://leetcode.com/problems/calculate-salaries/description/

import pandas as pd

def calculate_salaries(salaries: pd.DataFrame) -> pd.DataFrame:

    # Find max salary for all companies 
    salaries['max_sal'] = salaries.groupby('company_id')['salary'].transform('max')

    # Create a tax rate column (1 - tax rate)
    salaries['tax_rate'] = salaries['max_sal'].apply(lambda x: 1 if x < 1000 else(.76 if x <= 10000 else (.51)))

    # Multiply salary by tax_rate 
    salaries['post_tax'] = (salaries['salary'] * salaries['tax_rate']).apply(lambda x: round(x) if x % 1 != 0.5 else (np.ceil(x)))

    salaries = salaries.drop(columns=['salary','max_sal','tax_rate']).rename(columns={'post_tax':'salary'})

    return salaries
    
    
