# https://leetcode.com/problems/count-salary-categories/description/

# Write your MySQL query statement below

select "Low Salary" as category, count(*) as accounts_count from accounts
where income<20000
union
select "Average Salary" as category, count(*) as accounts_count from accounts
where income>=20000 and income<=50000
union
select "High Salary" as category, count(*) as accounts_count from accounts
where income>50000
