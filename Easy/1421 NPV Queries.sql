# https://leetcode.com/problems/npv-queries/description/

# Write your MySQL query statement below

SELECT Q.id, Q.year, IFNULL(N.NPV,0) AS NPV FROM 
Queries Q
LEFT JOIN
NPV N
ON Q.id = N.id AND Q.year = N.year

