# https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/description/

# Write your MySQL query statement below

SELECT EU.unique_id, E.name FROM 
Employees E 
LEFT OUTER JOIN 
EmployeeUNI EU
ON E.id = EU.id
