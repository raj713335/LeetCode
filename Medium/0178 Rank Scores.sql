# https://leetcode.com/problems/rank-scores/description/

# Write your MySQL query statement below

SELECT score, DENSE_RANK() OVER (ORDER BY score DESC) AS 'rank' FROM Scores
