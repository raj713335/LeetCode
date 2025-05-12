# https://leetcode.com/problems/find-followers-count/description/

# Write your MySQL query statement below

SELECT user_id, COUNT(DISTINCT follower_id) as followers_count
FROM Followers 
GROUP BY user_id 
