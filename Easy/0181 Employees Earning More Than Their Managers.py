# https://leetcode.com/problems/employees-earning-more-than-their-managers/

# Write your MySQL query statement below


SELECT E.name as Employee FROM 
Employee E 
INNER JOIN Employee Em 
ON E.managerId = Em.id
WHERE E.salary > Em.salary
