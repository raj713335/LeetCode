# https://leetcode.com/problems/class-performance/description/


# Write your MySQL query statement below


SELECT (SC1.total1-SC2.total2) AS difference_in_score FROM 

(SELECT (S1.assignment1 + S1.assignment2 + S1.assignment3) AS total1 FROM
Scores S1
ORDER BY total1 DESC
LIMIT 1) AS SC1,
(SELECT (S2.assignment1 + S2.assignment2 + S2.assignment3) AS total2 FROM
Scores S2
ORDER BY total2
LIMIT 1) AS SC2
