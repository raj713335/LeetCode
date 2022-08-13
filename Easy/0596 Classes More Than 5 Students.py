# https://leetcode.com/problems/classes-more-than-5-students/


# Write your MySQL query statement below

SELECT class 
FROM
(SELECT class as class, COUNT(*) val
FROM Courses
GROUP BY class
HAVING val>=5) as classx
