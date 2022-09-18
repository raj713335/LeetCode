# https://leetcode.com/problems/random-pick-index/


import random

class Solution:

    def __init__(self, nums: List[int]):
        
        self.picks = {}
        
        for i in range(0, len(nums)):
            if nums[i] in self.picks:
                self.picks[nums[i]].append(i)
            else:
                self.picks[nums[i]]= [i]
        

    def pick(self, target: int) -> int:
        
        rendx = random.randint(0,len(self.picks[target])-1)       
        return self.picks[target][rendx]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
