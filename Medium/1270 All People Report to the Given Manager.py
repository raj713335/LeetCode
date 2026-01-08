# https://leetcode.com/problems/all-people-report-to-the-given-manager/description/

import pandas as pd

def find_reporting_people(employees: pd.DataFrame) -> pd.DataFrame:

    # Employees who directly report to head (1)
    level1 = employees[
        (employees["manager_id"] == 1) &
        (employees["employee_id"] != employees["manager_id"])
    ]["employee_id"]

    # Employees whose manager reports to head
    level2 = employees[employees["manager_id"].isin(level1)]["employee_id"]

    # Employees whose manager's manager reports to head
    level3 = employees[employees["manager_id"].isin(level2)]["employee_id"]

    # Combine all levels and remove duplicates
    result = pd.concat([level1, level2, level3]).drop_duplicates()

    result = pd.DataFrame({"employee_id": result})
    result = result.sort_values(by="employee_id")

    return result
    
