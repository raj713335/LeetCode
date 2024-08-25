# https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-i/description/


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:


        for k in range(0, k):
            length = len(nums)

            sm, ind = math.inf, 0

            for i in range(0, length):
                if nums[i] < sm:
                    sm = nums[i]
                    ind = i
            
            nums[ind] = nums[ind] * multiplier

        return nums
