# https://leetcode.com/problems/count-number-of-distinct-integers-after-reverse-operations/


class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        
        for i in range(0, len(nums)):
            nums.append(int(str(nums[i])[::-1]))
            
        
        dictx = {}
        count = 0
        
        for each in nums:
            if each not in dictx:
                dictx[each] = 1
                count += 1
                
        return count
            
        
