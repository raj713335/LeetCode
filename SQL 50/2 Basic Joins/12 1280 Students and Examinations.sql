# https://leetcode.com/problems/students-and-examinations/description/

# Write your MySQL query statement below

SELECT student.student_id,student.student_name,subject.subject_name,COUNT(exam.subject_name) as attended_exams
FROM Students as student
JOIN Subjects as subject
LEFT JOIN Examinations as exam
ON student.student_id=exam.student_id AND subject.subject_name=exam.subject_name
GROUP BY student.student_id,subject.subject_name
ORDER BY student_id,subject_name;
