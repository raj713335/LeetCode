# https://leetcode.com/problems/select-data/description/


import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    students = students[students['student_id'] == 101] 
    students = students[['name','age']]
    return students
    
