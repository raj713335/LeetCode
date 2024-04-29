# https://leetcode.com/problems/product-sales-analysis-ii/description/

# Write your MySQL query statement below

SELECT S.product_id, SUM(quantity) AS total_quantity
FROM Sales S
LEFT JOIN 
Product P
ON P.product_id = S.product_id
GROUP BY S.product_id
