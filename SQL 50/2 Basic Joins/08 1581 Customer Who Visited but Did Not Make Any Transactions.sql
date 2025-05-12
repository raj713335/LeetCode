# https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/description/

# Write your MySQL query statement below

SELECT DISTINCT V.customer_id  as customer_id, COUNT(*) AS count_no_trans 
FROM Visits V
LEFT JOIN 
Transactions T
ON V.visit_id = T.visit_id 
WHERE T.amount IS NULL
GROUP BY V.customer_id
