# https://leetcode.com/problems/classifying-triangles-by-lengths/description/

  
# Write your MySQL query statement below

Select CASE
    WHEN (A=B AND A=C) THEN 'Equilateral'
    WHEN (A+B<=C OR B+C<=A OR A+C<=B) THEN 'Not A Triangle'
    WHEN (A=B AND A!=C) OR (A=C AND A!=B) OR(B=C AND A!=C) THEN 'Isosceles'
    ELSE 'Scalene'
END
AS 'triangle_type' FROM Triangles
