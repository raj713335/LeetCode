# https://leetcode.com/problems/premier-league-table-ranking/description/

# Write your MySQL query statement below

select team_id,
          team_name,
          3 * wins + draws points,
          Rank() over (order by  3 * wins + draws desc) position   
     from TeamStats
 order by points desc,
          team_name asc 
