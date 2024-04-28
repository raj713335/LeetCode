# https://leetcode.com/problems/find-customers-with-positive-revenue-this-year/description/

/* Write your PL/SQL query statement below */

SELECT customer_id
FROM customers
WHERE year = '2021'
GROUP BY customer_id
HAVING SUM(revenue) > 0;
