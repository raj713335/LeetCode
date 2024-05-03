# https://leetcode.com/problems/running-total-for-different-genders/description/


# Write your MySQL query statement below


SELECT s1.gender,
s1.day,
sum(s2.score_points) as total
FROM Scores s1
LEFT JOIN Scores s2 on s1.gender = s2.gender and s1.day >= s2.day
GROUP BY 1,2
ORDER BY 1,2
