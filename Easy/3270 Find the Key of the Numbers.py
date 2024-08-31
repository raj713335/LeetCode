# https://leetcode.com/contest/biweekly-contest-138/problems/find-the-key-of-the-numbers/


class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        
        num1 = (["0", "0", "0", "0"] + list(str(num1)))[-4:]
        num2 = (["0", "0", "0", "0"] + list(str(num2)))[-4:]
        num3 = (["0", "0", "0", "0"] + list(str(num3)))[-4:]
        
        numx = [min(num1[0], num2[0], num3[0]), min(num1[1], num2[1], num3[1]), min(num1[2], num2[2], num3[2]), min(num1[3], num2[3], num3[3])]
        
        return int("".join(numx))
        
