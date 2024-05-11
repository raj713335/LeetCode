# https://leetcode.com/problems/find-the-k-th-lucky-number/description/


class Solution:
    def kthLuckyNumber(self, k: int) -> str:

        return bin(k+1)[3:].replace('0','4').replace('1','7')
        
