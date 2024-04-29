# https://leetcode.com/problems/products-worth-over-invoices/description/


# Write your MySQL query statement below

SELECT P.name AS name, IFNULL(SUM(I.rest),0) AS rest, IFNULL(SUM(I.paid),0) AS paid, 
IFNULL(SUM(I.canceled),0) AS canceled, IFNULL(SUM(I.refunded),0) AS refunded   FROM 
Product P
LEFT JOIN 
INVOICE I
ON P.product_id = I.product_id
GROUP BY P.product_id
ORDER BY P.name
