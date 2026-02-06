# https://leetcode.com/problems/count-monobit-integers/description/

class Solution:
    def countMonobit(self, n: int) -> int:
        
        count = 0

        for i in range(0, n + 1):
            mono = bin(i)[2:]
            if len(set(mono)) == 1:
                count += 1

        return count
