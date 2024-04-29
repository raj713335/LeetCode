# https://leetcode.com/problems/bikes-last-time-used/description/

# Write your MySQL query statement below

SELECT bike_number , MAX(end_time) AS end_time
FROM 
Bikes
GROUP BY bike_number
ORDER BY MAX(end_time) DESC


