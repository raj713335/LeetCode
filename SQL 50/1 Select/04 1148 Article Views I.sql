# https://leetcode.com/problems/article-views-i/description/

# Write your MySQL query statement below

SELECT DISTINCT(author_id) as id
FROM Views
WHERE author_id = viewer_id
ORDER BY author_id ASC
