# https://leetcode.com/problems/find-the-team-size/description/

/* Write your PL/SQL query statement below */


WITH team_size_tbl AS(
    SELECT e2.team_id, COUNT(e2.employee_id) AS team_count
    FROM employee e2
    GROUP BY e2.team_id
)
SELECT e1.employee_id, tst.team_count AS team_size
FROM employee e1, team_size_tbl tst
WHERE e1.team_id = tst.team_id
