# https://leetcode.com/problems/highest-salaries-difference/description/

# Write your MySQL query statement below

SELECT ABS(E.salary_difference - M.salary_difference) AS salary_difference FROM
(
SELECT MAX(salary) AS salary_difference
FROM Salaries
GROUP BY department
HAVING department = "Engineering"
) AS E
JOIN
(
SELECT MAX(salary) AS salary_difference
FROM Salaries
GROUP BY department
HAVING department = "Marketing"
) AS M
