# https://leetcode.com/problems/consecutive-numbers/description/

# Write your MySQL query statement below

SELECT DISTINCT i1.num AS ConsecutiveNums 
FROM logs i1, logs i2, logs i3
WHERE 
    i1.id = i2.id + 1 
    AND i2.id = i3.id + 1 
    AND i1.num = i2.num 
    AND i2.num = i3.num;
