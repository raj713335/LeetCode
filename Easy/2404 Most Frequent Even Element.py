# https://leetcode.com/problems/most-frequent-even-element/


class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        
        dictx = {}
        
        
        for i in range(0, len(nums)):
            if nums[i] % 2 == 0:
                if nums[i] not in dictx:
                    dictx[nums[i]] = 1
                else:
                    dictx[nums[i]] += 1
                    
                    
        max_rep = 0
        min_value = -1
        
        
        for key, value in dictx.items():
            if value > max_rep:
                max_rep = value
                min_value = key
            elif value == max_rep:
                if min_value > key:
                    min_value = key
                    
        return min_value
        
