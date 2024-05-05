# https://leetcode.com/problems/the-users-that-are-eligible-for-discount/description/


CREATE PROCEDURE getUserIDs(startDate DATE, endDate DATE, minAmount INT)
BEGIN
	# Write your MySQL query statement below.

    SELECT DISTINCT user_id
    FROM purchases
    WHERE time_stamp >= startDate AND time_stamp <= endDate
    AND amount >= minAmount
    ORDER BY user_id;
	
END
