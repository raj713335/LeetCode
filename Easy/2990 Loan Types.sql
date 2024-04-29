# https://leetcode.com/problems/loan-types/description/

# Write your MySQL query statement below

SELECT M.user_id  FROM
(
    SELECT * FROM 
    Loans 
    WHERE loan_type = "Mortgage"
) AS M
INNER JOIN
(
    SELECT * FROM 
Loans 
WHERE loan_type = "Refinance"
) AS R
ON M.user_id = R.user_id
GROUP BY M.user_id
ORDER BY M.user_id
