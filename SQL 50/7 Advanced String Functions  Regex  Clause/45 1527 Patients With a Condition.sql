# https://leetcode.com/problems/patients-with-a-condition/description/

# Write your MySQL query statement below


SELECT * 
FROM Patients
WHERE conditions LIKE '% DIAB1%' OR conditions LIKE 'DIAB1%'
