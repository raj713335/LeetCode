# https://leetcode.com/problems/form-a-chemical-bond/description/

# Write your MySQL query statement below

SELECT
    a.symbol AS metal,
    b.symbol AS nonmetal
FROM
    Elements as a,
    Elements as b
WHERE
    a.type = "Metal" and b.type = "Nonmetal";
