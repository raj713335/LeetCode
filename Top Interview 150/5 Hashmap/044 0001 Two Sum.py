# https://leetcode.com/problems/two-sum/description/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dictx = {}
        
        for i in range(0, len(nums)):
            temp = target - nums[i]
            if temp in dictx:
                return [i, dictx[temp]]
            else:
                dictx[nums[i]] = i
            
