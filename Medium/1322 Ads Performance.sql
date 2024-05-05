# https://leetcode.com/problems/ads-performance/description/

# Write your MySQL query statement below

SELECT
    ad_id,
    IFNULL(ROUND(SUM(action="Clicked") / SUM(action <> "Ignored") * 100, 2), 0.00) AS ctr
FROM Ads
GROUP BY ad_id
ORDER BY ctr DESC, ad_id ASC;
