# https://leetcode.com/problems/friend-requests-ii-who-has-the-most-friends/description/

# Write your MySQL query statement below


WITH 
cte1 AS (
    SELECT requester_id AS id, COUNT(*) AS num
    FROM RequestAccepted
    GROUP BY requester_id
),
cte2 AS (
    SELECT accepter_id AS id, COUNT(*) AS num
    FROM RequestAccepted
    GROUP BY accepter_id
),
cte3 AS (
    SELECT id, num FROM cte1
    UNION ALL
    SELECT id, num FROM cte2
)

SELECT id, SUM(num) AS num
FROM cte3
GROUP BY id
ORDER BY num DESC
LIMIT 1;
