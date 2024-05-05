# https://leetcode.com/problems/sales-analysis-i/description/

# Write your MySQL query statement below

SELECT  seller_id  
FROM sales 
GROUP BY seller_id 
HAVING SUM(price)=(select MAX(A) 
FROM (SELECT SUM(price) AS A FROM sales GROUP BY seller_id) A)
