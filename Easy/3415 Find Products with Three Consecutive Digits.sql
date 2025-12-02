# https://leetcode.com/problems/find-products-with-three-consecutive-digits/description/

# Write your MySQL query statement below


SELECT product_id, name
FROM Products
WHERE name REGEXP '[^0-9][0-9]{3}[^0-9]'
   OR name REGEXP '^[0-9]{3}[^0-9]'
   OR name REGEXP '[^0-9][0-9]{3}$'
ORDER BY product_id;
