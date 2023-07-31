# https://leetcode.com/problems/the-number-of-rich-customers/description/

# Write your MySQL query statement below

SELECT COUNT(DISTINCT(customer_id)) AS rich_count FROM STORE WHERE amount > 500
