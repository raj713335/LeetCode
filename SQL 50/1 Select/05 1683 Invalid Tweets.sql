# https://leetcode.com/problems/invalid-tweets/description/

# Write your MySQL query statement below


SELECT tweet_id FROM 
(
SELECT tweet_id, LENGTH(content) FROM 
Tweets as T
WHERE LENGTH(content) > 15) T
