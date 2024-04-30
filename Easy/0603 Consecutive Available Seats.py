# https://leetcode.com/problems/consecutive-available-seats/description/


# Write your MySQL query statement below

SELECT DISTINCT b.seat_id
FROM Cinema A, Cinema B
  WHERE abs(A.seat_id - B.seat_id) = 1
  AND A.free = true AND B.free = true
