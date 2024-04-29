# https://leetcode.com/problems/sales-analysis-ii/description/

# Write your MySQL query statement below

SELECT buyer_id FROM 
sales S 
JOIN 
product P
ON S.product_id = P.product_id
GROUP BY buyer_id having SUM(product_name = "S8") > 0 and SUM(product_name = "iPhone") = 0
