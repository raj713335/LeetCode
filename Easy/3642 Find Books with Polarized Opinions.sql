# https://leetcode.com/problems/find-books-with-polarized-opinions/description/

  
# Write your MySQL query statement below

SELECT  r.book_id, b.title, b.author, b.genre, b.pages, MAX(r.session_rating) - MIN(r.session_rating) rating_spread, 
round( (SUM( CASE WHEN r.session_rating < 3 THEN 1 ELSE 0 END + CASE WHEN r.session_rating > 3 THEN 1 ELSE 0 END)) / COUNT(r.session_id) , 2) polarization_score
FROM reading_sessions r
INNER JOIN books b USING(book_id)
GROUP BY r.book_id, b.title, b.author, b.genre, b.pages
HAVING COUNT(r.session_id) > 4 AND MAX(r.session_rating) > 3 AND MIN(r.session_rating) < 3 AND
polarization_score >= 0.6
ORDER BY polarization_score DESC, b.title DESC
