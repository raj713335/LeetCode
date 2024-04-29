# https://leetcode.com/problems/shortest-distance-in-a-line/description/

# Write your MySQL query statement below

select MIN(NULLIF(ABS(P1.x - P2.x), 0)) shortest
FROM point P1, point P2
