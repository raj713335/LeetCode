# https://leetcode.com/problems/managers-with-at-least-5-direct-reports/description/

# Write your MySQL query statement below

SELECT EE.name as name FROM Employee E
INNER JOIN Employee EE
ON E.managerId = EE.id
GROUP BY EE.name, EE.id
HAVING COUNT(EE.name) >= 5
