# https://leetcode.com/problems/calculate-compressed-mean/description/

# Write your MySQL query statement below


SELECT ROUND(SUM(order_occurrences*item_count) / SUM(order_occurrences),2) AS average_items_per_order
FROM 
Orders
