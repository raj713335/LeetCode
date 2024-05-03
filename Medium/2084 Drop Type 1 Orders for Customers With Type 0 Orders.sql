# https://leetcode.com/problems/drop-type-1-orders-for-customers-with-type-0-orders/description/


# Write your MySQL query statement below

SELECT *
FROM Orders
WHERE customer_id NOT IN (
  SELECT DISTINCT customer_id
  FROM Orders
  WHERE order_type = 0
) OR order_type = 0
ORDER BY order_id;
