# https://leetcode.com/problems/user-activity-for-the-past-30-days-i/

# Write your MySQL query statement below

SELECT activity_date as day, COUNT(DISTINCT(user_id)) AS active_users
FROM Activity 
WHERE (activity_date > "2019-06-27" AND activity_date <= "2019-07-27")
GROUP BY activity_date 
