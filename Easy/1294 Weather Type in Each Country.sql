# https://leetcode.com/problems/weather-type-in-each-country/description/


# Write your MySQL query statement below

SELECT c.country_name, avg_weather.weather_type
FROM Countries as c
JOIN
(SELECT country_id, AVG(weather_state) as "avg_weather",
CASE 
    WHEN AVG(weather_state) <= 15 THEN "Cold"
    WHEN AVG(weather_state) >= 25 THEN "Hot"
    ELSE "Warm"
END as weather_type
FROM Weather
WHERE day BETWEEN "2019-11-01" AND "2019-11-30"
GROUP BY country_id) as avg_weather
ON c.country_id = avg_weather.country_id;
