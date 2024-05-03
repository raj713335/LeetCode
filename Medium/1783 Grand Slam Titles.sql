# https://leetcode.com/problems/grand-slam-titles/description/

# Write your MySQL query statement below

SELECT player_id, player_name, SUM(Wimbledon = player_id) + SUM(Fr_open = player_id) + SUM(US_open = player_id) + SUM(Au_open = player_id) AS grand_slams_count FROM Players, Championships
GROUP BY player_id
HAVING grand_slams_count != 0
