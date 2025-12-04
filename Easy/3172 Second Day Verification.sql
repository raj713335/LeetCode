# https://leetcode.com/problems/second-day-verification/description/

# Write your MySQL query statement below

select user_id
from emails e join texts t
on e.email_id = t.email_id 
and date_add(date(signup_date), interval 1 day) = date(action_date)
and signup_action = 'Verified'
order by 1
