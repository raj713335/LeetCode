# https://leetcode.com/problems/triangle-judgement/description/

# Write your MySQL query statement below

SELECT x, y, z,CASE WHEN (
                    ((y+z) > x) and 
                    ((x+z) > y) and 
                    ((x+y) > z) 
                ) THEN 'Yes' 
                  ELSE 'No' 
                  END AS triangle
FROM triangle
