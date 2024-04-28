# https://leetcode.com/problems/largest-unique-number/description/

class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:

        dictx = {}

        for each in nums:
            if each not in dictx:
                dictx[each] = 1
            else:
                dictx[each] += 1

        ans = []

        for key, value in dictx.items():
            if value == 1:
                ans.append(key)

        if len(ans) == 0:
            return -1
        else:
            return max(ans)
        
