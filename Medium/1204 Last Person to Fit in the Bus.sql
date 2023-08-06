# https://leetcode.com/problems/last-person-to-fit-in-the-bus/description/


# Write your MySQL query statement below

SELECT person_name FROM (
  SELECT *, SUM(weight) OVER (order by turn) as cum_sum from queue
) AS sub
WHERE cum_sum <= 1000 
ORDER BY cum_sum DESC
LIMIT 1
