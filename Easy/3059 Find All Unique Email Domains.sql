# Write your MySQL query statement below

SELECT RIGHT(email, LENGTH(email) - INSTR(email, '@')) AS email_domain, COUNT(DISTINCT id) AS count
FROM Emails
WHERE email LIKE '%.com'
GROUP BY email_domain;
