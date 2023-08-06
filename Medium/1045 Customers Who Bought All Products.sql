# https://leetcode.com/problems/customers-who-bought-all-products/description/

# Write your MySQL query statement below

SELECT customer_id FROM (
  SELECT *, COUNT(DISTINCT(product_key)) as total FROM Customer 
  GROUP BY customer_id
) AS c
WHERE total = (SELECT COUNT(DISTINCT(product_key)) FROM Product)
