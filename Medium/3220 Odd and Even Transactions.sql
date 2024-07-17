# https://leetcode.com/problems/odd-and-even-transactions/description/

# Write your MySQL query statement below


SELECT transaction_date, 
SUM(CASE WHEN amount%2<>0 then amount else 0 end) as odd_sum,  
SUM(CASE WHEN amount%2=0 then amount else 0 end) as even_sum
FROM transactions 
GROUP BY transaction_date
ORDER BY transaction_date
