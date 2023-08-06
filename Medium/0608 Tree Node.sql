# https://leetcode.com/problems/tree-node/description/

# Write your MySQL query statement below


SELECT id, 
    (CASE
        WHEN p_id  is NULL then 'Root'
        WHEN p_id in (SELECT id from Tree) AND id in (SELECT P_id from Tree) THEN 'Inner'
        ELSE 'Leaf'
    END)
    AS type
FROM Tree
