# https://leetcode.com/problems/sellers-with-no-sales/description/

# Write your MySQL query statement below

SELECT S.seller_name FROM 
Seller S
LEFT JOIN 
Orders O
ON 
S.seller_id = O.seller_id AND O.sale_date LIKE "2020%"
WHERE O.seller_id IS NULL
GROUP BY S.seller_id
ORDER BY S.seller_name
