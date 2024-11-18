# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        counter = 0

        dictx = {}

        for i in range(0, len(nums)):
            if nums[i] not in dictx.keys():
                nums[counter] = nums[i]
                counter += 1
                dictx[nums[i]] = 1
                
        return counter


        
