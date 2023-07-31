# https://leetcode.com/problems/immediate-food-delivery-i/description/

# Write your MySQL query statement below

SELECT ROUND((COUNT(*) / (SELECT COUNT(*) FROM Delivery) * 100 ),2) AS  immediate_percentage  FROM Delivery WHERE order_date = customer_pref_delivery_date  
