# https://leetcode.com/problems/richest-customer-wealth/submissions/

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        
        for each in accounts:
            temp = sum(each)
            if temp > max_wealth:
                max_wealth = temp
                
        return max_wealth
            
        
