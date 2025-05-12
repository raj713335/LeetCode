# https://leetcode.com/problems/average-selling-price/description/

# Write your MySQL query statement below


SELECT P.product_id, ROUND(SUM(US.units * P.Price)/ SUM(US.units),2) as average_price 
FROM UnitsSold US
INNER JOIN 
Prices P
ON US.product_id = P.product_id 
WHERE US.purchase_date BETWEEN P.start_date AND P.end_date   
GROUP BY P.product_id
