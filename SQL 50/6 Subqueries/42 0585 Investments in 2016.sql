# https://leetcode.com/problems/investments-in-2016/description/

# Write your MySQL query statement below

SELECT ROUND(SUM(tiv_2016), 2) as tiv_2016 
FROM Insurance I1
WHERE tiv_2015 IN (SELECT tiv_2015 FROM INSURANCE I2
    WHERE I1.pid != I2.pid)
AND
(lat, lon) NOT IN (SELECT lat, lon FROM INSURANCE I3
    WHERE I1.pid != I3.pid)
