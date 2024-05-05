# https://leetcode.com/problems/user-activity-for-the-past-30-days-ii/description/

# Write your MySQL query statement below


SELECT ROUND(IFNULL(AVG(SESSIONS), 0.00),2) AS AVERAGE_SESSIONS_PER_USER
FROM  
(
    SELECT 
    USER_ID,
    COUNT(DISTINCT SESSION_ID) AS SESSIONS
    FROM ACTIVITY 
    WHERE ACTIVITY_DATE BETWEEN '2019-06-28' AND '2019-07-27'
    GROUP BY USER_ID
)
AS T1
