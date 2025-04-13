# https://leetcode.com/problems/russian-doll-envelopes/description/

import bisect

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:

        envelopes.sort(key=lambda x: (x[0], -x[1]))
        heights = [h for _, h in envelopes]
        lis = []

        for h in heights:
            idx = bisect.bisect_left(lis, h)
            if idx == len(lis):
                lis.append(h)
            else:
                lis[idx] = h

        return len(lis)

import bisect

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:

        nums = []

        dictx = {}

        for each in envelopes:
            if tuple(each) not in dictx:
                nums.append(each)
                dictx[tuple(each)] = 1

        nums.sort()

        n = len(nums)

        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[i][0] > nums[j][0] and nums[i][1] > nums[j][1]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
