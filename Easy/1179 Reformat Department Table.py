# https://leetcode.com/problems/reformat-department-table/

# Write your MySQL query statement below


select id,
sum(case when month = 'Jan' then revenue end) 'Jan_Revenue',
sum(case when month = 'Feb' then revenue end) 'Feb_Revenue',
sum(case when month = 'Mar' then revenue end) 'Mar_Revenue',
sum(case when month = 'Apr' then revenue end) 'Apr_Revenue',
sum(case when month = 'May' then revenue end) 'May_Revenue',
sum(case when month = 'Jun' then revenue end) 'Jun_Revenue',
sum(case when month = 'Jul' then revenue end) 'Jul_Revenue',
sum(case when month = 'Aug' then revenue end) 'Aug_Revenue',
sum(case when month = 'Sep' then revenue end) 'Sep_Revenue',
sum(case when month = 'Oct' then revenue end) 'Oct_Revenue',
sum(case when month = 'Nov' then revenue end) 'Nov_Revenue',
sum(case when month = 'Dec' then revenue end) 'Dec_Revenue'
from department
group by id
