# https://leetcode.com/problems/employee-importance/description/

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:

        def dfs(id):
            sumx = emps[id].importance
        
            for each in emps[id].subordinates:
                sumx += dfs(each)

            return sumx

        emps = {emp.id: emp for emp in employees}

        return dfs(id)
