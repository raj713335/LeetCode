# https://leetcode.com/problems/find-the-child-who-has-the-ball-after-k-seconds/description/


class Solution:
    def numberOfChild(self, n: int, k: int) -> int:

        n -= 1
        rounds = k //n
        rem = k % n

        if rounds % 2 == 0:
            return rem
        else:
            return n - rem
        
