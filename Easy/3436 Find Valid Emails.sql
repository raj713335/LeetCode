# https://leetcode.com/problems/find-valid-emails/description/
  

# Write your MySQL query statement below

SELECT *
FROM Users 
WHERE email  REGEXP '^[0-9a-zA-Z_]*@[0-9a-zA-Z_]*.com$';
