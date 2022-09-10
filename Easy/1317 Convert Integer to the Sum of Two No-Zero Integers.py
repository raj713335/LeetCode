# https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/


class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        
        for i in range(1, n):
            if str(i).count("0") == 0 and str(n-i).count("0") == 0:
                return [i, n-i]
        
