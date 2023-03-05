# https://leetcode.com/problems/pass-the-pillow/description/


class Solution:
    def passThePillow(self, n: int, time: int) -> int:

        return n - abs(n - 1 - time % (n * 2 - 2))

        
