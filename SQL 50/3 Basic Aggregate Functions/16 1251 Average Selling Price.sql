# https://leetcode.com/problems/average-selling-price/description/

# Write your MySQL query statement below


SELECT P.product_id, IFNULL(ROUND(SUM(US.units * P.Price)/ SUM(US.units),2),0) as average_price 
FROM Prices P
LEFT JOIN 
UnitsSold US
ON US.product_id = P.product_id 
AND US.purchase_date BETWEEN P.start_date AND P.end_date   
GROUP BY P.product_id
