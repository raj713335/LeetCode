# https://leetcode.com/problems/convert-date-format/description/

# Write your MySQL query statement below


SELECT 
date_format(day, '%W, %M %e, %Y') as day
FROM Days
