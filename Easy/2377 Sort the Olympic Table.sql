# https://leetcode.com/problems/sort-the-olympic-table/description/


# Write your MySQL query statement below

SELECT *
FROM Olympic
ORDER BY gold_medals DESC, silver_medals DESC, bronze_medals DESC, country
