# https://leetcode.com/problems/market-analysis-i/description/

# Write your MySQL query statement below

SELECT U.user_id AS buyer_id, U.join_date, SUM(
  CASE 
    WHEN SUBSTRING(O.order_date, 1, 4) = '2019' THEN 1
    ELSE 0
    END
) AS orders_in_2019 FROM Users U
LEFT JOIN Orders O
ON U.user_id = O.buyer_id
GROUP BY U.user_id
ORDER BY O.buyer_id ASC
