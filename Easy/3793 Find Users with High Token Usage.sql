# https://leetcode.com/problems/find-users-with-high-token-usage/description/

# Write your MySQL query statement below

SELECT user_id, COUNT(prompt) AS prompt_count, ROUND(AVG(tokens),2) AS avg_tokens FROM 
prompts 
GROUP BY user_id
HAVING prompt_count >= 3 AND MAX(tokens) > avg_tokens
ORDER BY avg_tokens DESC

