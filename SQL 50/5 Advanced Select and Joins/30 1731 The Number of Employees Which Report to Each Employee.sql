# https://leetcode.com/problems/the-number-of-employees-which-report-to-each-employee/description/

# Write your MySQL query statement below

SELECT EX.employee_id , EX.name, COUNT(E.reports_to) AS reports_count, ROUND(AVG(E.age)) AS average_age  FROM Employees E
INNER JOIN Employees EX
ON E.reports_to = EX.employee_id 
GROUP BY E.reports_to
ORDER BY EX.employee_id ASC

