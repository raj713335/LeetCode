# https://leetcode.com/problems/fix-names-in-a-table/description/

# Write your MySQL query statement below


SELECT user_id, concat(upper(substring(name,1,1)),lower(substring(name,2,length(name)-1))) as name FROM Users
order by user_id
