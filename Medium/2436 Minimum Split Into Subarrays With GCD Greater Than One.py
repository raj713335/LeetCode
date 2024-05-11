# https://leetcode.com/problems/minimum-split-into-subarrays-with-gcd-greater-than-one/description/


class Solution:
    def minimumSplits(self, nums: List[int]) -> int:

        count = 0
        curr = 1

        for num in nums:
            curr = math.gcd(curr, num)
            if curr == 1:
                count += 1
                curr = num
                
        return count
        
