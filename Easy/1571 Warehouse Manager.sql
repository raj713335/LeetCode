# https://leetcode.com/problems/warehouse-manager/description/

# Write your MySQL query statement below

SELECT
W.name AS warehouse_name,
SUM(P.width*P.length*P.height*W.units) AS volume
FROM warehouse W JOIN products P 
ON W.product_id=P.product_id
GROUP BY W.name
