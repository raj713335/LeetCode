# https://leetcode.com/problems/friendly-movies-streamed-last-month/description/

# Write your MySQL query statement below

SELECT DISTINCT C.title
FROM 
Content C
INNER JOIN 
TVProgram T
ON
C.content_id = T.content_id
WHERE T.program_date LIKE "2020-06%" AND C.content_type LIKE "Movies" AND C.Kids_content = "Y"
