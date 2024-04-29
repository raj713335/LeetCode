# https://leetcode.com/problems/unique-orders-and-customers-per-month/

# Write your MySQL query statement below

SELECT  LEFT(order_date, 7) month,
        COUNT(DISTINCT order_id) order_count,
        COUNT(DISTINCT customer_id) customer_count
FROM orders
WHERE invoice > 20
GROUP BY month;
