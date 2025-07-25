# https://leetcode.com/problems/queries-quality-and-percentage/description/

# Write your MySQL query statement below

SELECT query_name, ROUND(SUM(rating / position )/ COUNT(query_name), 2) as quality, 
ROUND(AVG(case 
             WHEN rating < 3 THEN 1 
             ELSE 0 end
            )*100, 2) as poor_query_percentage
FROM Queries 
GROUP BY query_name 


