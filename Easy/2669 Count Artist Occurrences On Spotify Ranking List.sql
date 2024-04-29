# https://leetcode.com/problems/count-artist-occurrences-on-spotify-ranking-list/description/

# Write your MySQL query statement below


SELECT artist, COUNT(*) AS occurrences
FROM Spotify
GROUP BY artist
ORDER BY occurrences DESC, artist
