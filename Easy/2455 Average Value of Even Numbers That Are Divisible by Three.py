# https://leetcode.com/problems/average-value-of-even-numbers-that-are-divisible-by-three/description/


class Solution:
    def averageValue(self, nums: List[int]) -> int:

        count = 0
        sumx = 0

        for each in nums:
            if each % 2 == 0 and each % 3 == 0:
                sumx += each
                count += 1
        if count == 0:
            return count
        else:
            return sumx//count
