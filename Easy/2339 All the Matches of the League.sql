# https://leetcode.com/problems/all-the-matches-of-the-league/description/

# Write your MySQL query statement below

SELECT T1.team_name as home_team, T2.team_name as  away_team FROM 
Teams T1
INNER JOIN 
Teams T2
ON T1.team_name != T2.team_name
