# https://leetcode.com/problems/find-total-time-spent-by-each-employee/


# Write your MySQL query statement below


SELECT event_day as day,  emp_id, sum(out_time - in_time ) as total_time  from Employees 
GROUP BY event_day  ,emp_id
