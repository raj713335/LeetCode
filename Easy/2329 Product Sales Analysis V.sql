# https://leetcode.com/problems/product-sales-analysis-v/


# Write your MySQL query statement below

SELECT S.user_id, SUM(S.quantity * P.price) AS spending
FROM 
Sales S
INNER JOIN 
Product P
ON
S.product_id = P.product_id
GROUP BY S.user_id
ORDER BY spending DESC
