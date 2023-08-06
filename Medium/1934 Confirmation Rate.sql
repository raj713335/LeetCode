# https://leetcode.com/problems/confirmation-rate/description/

# Write your MySQL query statement below

SELECT S.user_ID, ROUND(AVG(IF(C.action="confirmed", 1, 0)),2) AS confirmation_rate FROM Signups S
LEFT JOIN Confirmations C
ON S.user_id = C.user_id
GROUP BY S.user_id
