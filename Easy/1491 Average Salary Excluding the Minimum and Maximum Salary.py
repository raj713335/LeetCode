# https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/


import math

class Solution:
    def average(self, salary: List[int]) -> float:
               
        maxi = -math.inf
        mini = math.inf
        
        count = 0
        
        sumx = 0
        
        for each in salary:
            sumx += each
            
            if each > maxi:
                maxi = each
            if each < mini:
                mini = each
                
            count += 1
            
            
        return (sumx-maxi-mini)/(count-2)
            
        
