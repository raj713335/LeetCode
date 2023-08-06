# https://leetcode.com/problems/department-highest-salary/description/

# Write your MySQL query statement below

SELECT D.name AS Department, E.name AS Employee, E.salary AS Salary  
FROM Employee E, Department D
WHERE E.DepartmentId = D.id AND (DepartmentId,Salary) in 
  (SELECT DepartmentId,max(Salary) as max FROM Employee GROUP BY DepartmentId)
