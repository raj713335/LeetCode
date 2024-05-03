# https://leetcode.com/problems/calculate-the-influence-of-each-salesperson/description/


# Write your MySQL query statement below

SELECT S.salesperson_id, S.name, IFNULL(SUM(SA.price),0) total FROM 
Salesperson S 
LEFT JOIN 
Customer C
ON S.salesperson_id = C.salesperson_id
LEFT JOIN
Sales SA
ON C.customer_id = SA.customer_id
GROUP BY S.salesperson_id

