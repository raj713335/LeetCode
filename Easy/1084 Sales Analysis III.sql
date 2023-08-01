# https://leetcode.com/problems/sales-analysis-iii/

# Write your MySQL query statement below

SELECT DISTINCT(P.product_id) , P.product_name FROM Product P
INNER JOIN Sales S
ON P.product_id = S.product_id 
WHERE S.sale_date BETWEEN '2019-01-01' AND '2019-03-31'
AND P.product_id NOT IN 
(SELECT DISTINCT(P.product_id) FROM Product P
INNER JOIN Sales S
ON P.product_id = S.product_id 
WHERE S.sale_date NOT BETWEEN '2019-01-01' AND '2019-03-31')
