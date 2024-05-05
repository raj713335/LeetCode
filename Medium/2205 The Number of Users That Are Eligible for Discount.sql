# https://leetcode.com/problems/the-number-of-users-that-are-eligible-for-discount/description/



CREATE FUNCTION getUserIDs(startDate DATE, endDate DATE, minAmount INT) RETURNS INT
BEGIN
  RETURN (
      SELECT COUNT(DISTINCT user_id) AS usr_cnt
      FROM purchases
      WHERE time_stamp >= startDate AND time_stamp <= endDate
      AND amount >= minAmount  
  );
END
