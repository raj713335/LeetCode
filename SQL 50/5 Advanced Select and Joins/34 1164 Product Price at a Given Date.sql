# https://leetcode.com/problems/product-price-at-a-given-date/description/

# Write your MySQL query statement below

SELECT p.product_id, COALESCE(latest.new_price, 10) AS price
FROM (SELECT DISTINCT product_id FROM Products) p
LEFT JOIN Products latest
ON p.product_id = latest.product_id
AND latest.change_date = (
    SELECT MAX(change_date)
    FROM Products
    WHERE product_id = p.product_id AND change_date <= '2019-08-16'
);
