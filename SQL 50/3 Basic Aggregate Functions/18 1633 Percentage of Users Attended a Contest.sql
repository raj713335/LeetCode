# https://leetcode.com/problems/percentage-of-users-attended-a-contest/description/

# Write your MySQL query statement below
  
select contest_id, round(count(distinct user_id) /(select count(user_id) from Users)*100,2) as percentage
from Register
group by contest_id
order by percentage desc , contest_id
