# https://leetcode.com/problems/project-employees-ii/description/


# Write your MySQL query statement below

SELECT project_id
FROM project
GROUP BY project_id
HAVING count(*) = (SELECT count(*)
FROM project
GROUP BY project_Id
ORDER BY count(*) DESC LIMIT 1)
