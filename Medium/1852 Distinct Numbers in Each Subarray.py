# https://leetcode.com/problems/distinct-numbers-in-each-subarray/description/


class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:

        dictx = {}

        for i in range(0, k):
            if nums[i] not in dictx:
                dictx[nums[i]] = 1
            else:
                dictx[nums[i]] += 1

        ans = [len(dictx.keys())]
        res = ans[0]

        for i in range(k, len(nums)):
            dictx[nums[i-k]] -= 1
            if dictx[nums[i-k]] == 0:
                res -= 1
            if nums[i] not in dictx:
                dictx[nums[i]] = 1
            else:
                dictx[nums[i]] += 1

            if dictx[nums[i]] == 1:
                res += 1

            ans.append(res)

        return ans
