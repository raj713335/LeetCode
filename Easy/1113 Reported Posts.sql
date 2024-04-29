# https://leetcode.com/problems/reported-posts/

# Write your MySQL query statement below

SELECT extra  AS report_reason, COUNT(DISTINCT post_id) AS report_count  FROM 
Actions
WHERE  action = 'report'  AND action_date LIKE "2019-07-04"
GROUP BY extra
