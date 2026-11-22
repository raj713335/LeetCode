# https://leetcode.com/problems/count-dominant-elements/


class Solution:
    def countDominantElements(self, nums: list[int]) -> int:

        dominant = 0 

        try: 
            if nums[0] >= nums[1]:
                dominant += 1
            if nums[-1] >= nums[-2]:
                dominant += 1
        except:
            dominant += 1

        for i in range(1, len(nums)-1):
            if nums[i] >= ((nums[i-1] + nums[i+1])/2):
                dominant += 1

        return dominant
        
