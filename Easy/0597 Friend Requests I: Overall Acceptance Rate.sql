# https://leetcode.com/problems/friend-requests-i-overall-acceptance-rate/description/

# Write your MySQL query statement below

SELECT IFNULL(ROUND(a.v1 / b.v2, 2), 0) AS accept_rate
FROM 
(
    SELECT COUNT(*) AS v1 
    FROM 
    (
        SELECT DISTINCT requester_id, accepter_id 
        FROM RequestAccepted
    ) AS suba
) AS a,
(
    SELECT COUNT(*) AS v2 
    FROM 
    (
        SELECT DISTINCT sender_id, send_to_id 
        FROM FriendRequest 
        #UNION 
        #SELECT requester_id, accepter_id 
        #FROM RequestAccepted
    ) AS subb
) AS b;
