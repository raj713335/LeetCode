# https://leetcode.com/problems/ad-free-sessions/description/

# Write your MySQL query statement below

SELECT session_id FROM Playback WHERE session_id NOT IN (
SELECT DISTINCT a.session_id FROM (
    SELECT t1.session_id, t2.ad_id, t1.customer_id, t2.timestamp, t1.start_time, t1.end_time FROM Playback t1 LEFT JOIN
    Ads t2 ON t1.customer_id = t2.customer_id 
)a WHERE a.timestamp >= a.start_time AND a.timestamp <= a.end_time
GROUP BY a.ad_id
)
