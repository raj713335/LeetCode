# https://leetcode.com/problems/highest-grade-for-each-student/description/

import pandas as pd

def highest_grade(enrollments: pd.DataFrame) -> pd.DataFrame:

    enrollments = enrollments.sort_values(
        by=['student_id', 'grade', 'course_id'],
        ascending=[True, False, True]
    )

    # Keep first row per student
    result = enrollments.drop_duplicates(subset=['student_id'], keep='first')

    return result
    
