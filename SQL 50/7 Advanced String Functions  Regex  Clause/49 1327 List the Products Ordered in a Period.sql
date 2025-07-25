# https://leetcode.com/problems/list-the-products-ordered-in-a-period/description/

# Write your MySQL query statement below

SELECT P.product_name, A.n_of_sales AS unit
FROM
(SELECT product_id, sum(UNIT) as n_of_sales
FROM Orders
WHERE year(order_date) = 2020 AND month(order_date) = 2
GROUP by product_id) A
INNER JOIN Products p ON a.product_id = p.product_id
WHERE A.n_of_sales >= 100
