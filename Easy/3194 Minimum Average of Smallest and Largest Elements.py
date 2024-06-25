# https://leetcode.com/problems/minimum-average-of-smallest-and-largest-elements/description/

class Solution:
    def minimumAverage(self, nums: List[int]) -> float:

        nums = sorted(nums)

        i, j = 0, len(nums) - 1

        listx = []

        while i < j:
            listx.append((nums[i]+ nums[j])/2)
            i += 1
            j -= 1

        return min(listx)

        
