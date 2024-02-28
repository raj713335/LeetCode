# Write your MySQL query statement below

SELECT candidate_id FROM 
(SELECT candidate_id, COUNT(*) as countx FROM Candidates WHERE skill LIKE 'Python' OR skill LIKE 'Tableau' OR skill LIKE 'PostgreSQL'
GROUP BY candidate_id) as filler
WHERE countx = 3
ORDER BY candidate_id ASC
