# https://leetcode.com/problems/all-valid-triplets-that-can-represent-a-country/description/


# Write your MySQL query statement below

SELECT A.student_name AS member_A, B.student_name AS member_B, C.student_name AS member_C
FROM SchoolA A
JOIN SchoolB B
JOIN SchoolC C
WHERE A.student_id != B.student_id AND B.student_id != C.student_id AND C.student_id != A.student_id
AND A.student_name != B.student_name AND B.student_name != C.student_name AND C.student_name != A.student_name
