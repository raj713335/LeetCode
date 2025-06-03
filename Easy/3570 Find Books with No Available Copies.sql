# https://leetcode.com/problems/find-books-with-no-available-copies/

# Write your MySQL query statement below

SELECT l.book_id, l.title, l.author, l.genre, l.publication_year , l.total_copies as current_borrowers
FROM library_books l
JOIN borrowing_records b
ON l.book_id = b.book_id 
    AND b.return_date IS NULL
GROUP BY l.book_id
HAVING COUNT(*) = l.total_copies
ORDER BY l.total_copies DESC, l.title 
