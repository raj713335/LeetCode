# https://leetcode.com/problems/find-the-maximum-divisibility-score/description/


class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:

        divisors = sorted(divisors)

        hightest = 0
        max_div = divisors[0]

        for div in divisors:
            temp = 0
            for each in nums:
                if each % div == 0:
                    temp += 1

            if temp > hightest:
                hightest = temp
                max_div = div

        return max_div
