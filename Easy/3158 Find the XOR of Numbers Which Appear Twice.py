# https://leetcode.com/problems/find-the-xor-of-numbers-which-appear-twice/description/


class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:

        dictx  = {}
        res = []

        for each in nums:
            if each not in dictx:
                dictx[each] = 1
            else:
                dictx[each] += 1
        
        for key, value in dictx.items():
            if value > 1:
                res.append(key)
        try:
            ans = res[0]
        except:
            ans = 0

        for i in range(1, len(res)):
            ans = ans ^ res[i]

        return ans
        
