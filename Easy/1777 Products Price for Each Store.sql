# https://leetcode.com/problems/products-price-for-each-store/description/


# Write your MySQL query statement below


SELECT 
PRODUCT_ID,
MAX(CASE WHEN STORE = 'store1' THEN PRICE ELSE NULL END) AS STORE1,
MAX(CASE WHEN STORE = 'store2' THEN PRICE ELSE NULL END) AS STORE2,
MAX(CASE WHEN STORE = 'store3' THEN PRICE ELSE NULL END) AS STORE3
FROM PRODUCTS 
GROUP BY PRODUCT_ID
