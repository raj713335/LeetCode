# https://leetcode.com/problems/top-travellers/


# Write your MySQL query statement below


SELECT U.name as name, IFNULL(SUM(R.distance),0) as travelled_distance
FROM Users U 
LEFT JOIN 
Rides R
ON U.id = R.user_id
GROUP BY U.name,R.user_id
ORDER BY travelled_distance DESC, U.name ASC
