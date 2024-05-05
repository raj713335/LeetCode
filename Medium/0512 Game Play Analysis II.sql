# https://leetcode.com/problems/the-users-that-are-eligible-for-discount/description/


# Write your MySQL query statement below

SELECT player_id, device_id FROM Activity a1
WHERE event_date = (SELECT MIN(event_date) FROM Activity a2 WHERE a1.player_id = a2.player_id)

