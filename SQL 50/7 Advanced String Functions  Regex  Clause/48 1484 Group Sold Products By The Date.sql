# https://leetcode.com/problems/group-sold-products-by-the-date/description/


# Write your MySQL query statement below


SELECT sell_date,
		COUNT(DISTINCT(product)) AS num_sold, 
		GROUP_CONCAT(DISTINCT product ORDER BY product ASC SEPARATOR ',') AS products
FROM Activities
GROUP BY sell_date
ORDER BY sell_date ASC
