# https://leetcode.com/problems/users-that-actively-request-confirmation-messages/description/

# Write your MySQL query statement below


SELECT DISTINCT a.user_id FROM Confirmations a, Confirmations b
WHERE a.user_id = b.user_id AND b.time_stamp - a.time_stamp <= 1000000 AND b.time_stamp > a.time_stamp 
