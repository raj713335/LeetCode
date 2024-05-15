# https://leetcode.com/problems/invalid-tweets-ii/description/

# Write your MySQL query statement below

SELECT tweet_id
FROM Tweets
WHERE CHAR_LENGTH(content) > 140 OR
      LENGTH(content)- LENGTH(REPLACE(content, '@', '')) > 3 OR
      LENGTH(content)- LENGTH(REPLACE(content, '#', '')) > 3
ORDER BY tweet_id ASC
