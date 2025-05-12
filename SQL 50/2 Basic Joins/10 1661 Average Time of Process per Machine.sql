# https://leetcode.com/problems/average-time-of-process-per-machine/description/

# Write your MySQL query statement below

SELECT A.machine_id, ROUND(AVG(AC.timestamp - A.timestamp), 3) as processing_time
FROM Activity A JOIN Activity AC
ON A.machine_id = AC.machine_id
AND A.process_id = AC.process_id 
AND A.activity_type = 'start' AND AC.activity_type = 'end'
GROUP BY A.machine_id 
