# https://leetcode.com/problems/count-symmetric-integers/description/


class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:

        count = 0

        for i in range(low, high+1):
            temp = list(map(int, str(i)))
            n = len(temp) // 2
            if len(temp) % 2 == 0:
                if sum(temp[:n]) == sum(temp[n:]):
                    count += 1

        return count
        
