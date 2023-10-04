# https://leetcode.com/problems/rename-columns/description/

import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:

    students.rename(columns = {'id':'student_id'}, inplace = True)
    students.rename(columns = {'first':'first_name'}, inplace = True)
    students.rename(columns = {'last':'last_name'}, inplace = True)
    students.rename(columns = {'age':'age_in_years'}, inplace = True)

    return students
    
