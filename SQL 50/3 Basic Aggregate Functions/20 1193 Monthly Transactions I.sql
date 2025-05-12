# https://leetcode.com/problems/monthly-transactions-i/description/

# Write your MySQL query statement below

SELECT SUBSTRING(trans_date, 1 , LENGTH(trans_date)-3) as month, country, COUNT(*) AS trans_count, 
SUM(CASE WHEN state = 'approved' then 1 else 0 END) AS approved_count, 
SUM(amount) AS trans_total_amount, 
SUM(CASE WHEN state = 'approved' then amount else 0 END) AS approved_total_amount
FROM 
Transactions
GROUP BY month, country
