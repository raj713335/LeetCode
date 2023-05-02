# https://leetcode.com/problems/maximum-sum-with-exactly-k-elements/description/


class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:

        maxi = max(nums)

        sumx = 0

        for i in range(0, k):
            sumx += maxi
            maxi += 1

        return sumx
