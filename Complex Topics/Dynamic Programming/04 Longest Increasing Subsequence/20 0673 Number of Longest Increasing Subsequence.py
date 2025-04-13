# https://leetcode.com/problems/number-of-longest-increasing-subsequence/description/

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:

        n = len(nums)

        LIS = [[1, 1] for _ in range(n)]

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if LIS[j][0] + 1 > LIS[i][0]:
                        LIS[i][0] = LIS[j][0] + 1
                        LIS[i][1] = LIS[j][1]
                    elif LIS[j][0] + 1 == LIS[i][0]:
                        LIS[i][1] += LIS[j][1]

        max_LIS = 0
        count = 0

        for each in LIS:
            if each[0] > max_LIS:
                max_LIS = each[0]
                count = each[1]
            elif each[0] == max_LIS:
                count += each[1]

        return count
