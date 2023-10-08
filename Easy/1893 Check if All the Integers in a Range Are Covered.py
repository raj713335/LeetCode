# https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/description/


class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:

        ans = 0

        for i in range(left, right+1):
            for x,y in ranges:
                if i in [x for x in range(x,y+1)]:
                    ans += 1
                    break
                    
        return ans == right-left+1
