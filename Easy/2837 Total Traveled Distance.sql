# https://leetcode.com/problems/total-traveled-distance/description/

# Write your MySQL query statement below


SELECT U.user_id AS user_id, U.name AS name, IFNULL(SUM(R.distance), 0) AS "traveled distance" FROM 
Users U
LEFT JOIN
Rides R
ON U.user_id = R.user_id
GROUP BY U.user_id
ORDER BY U.user_id
