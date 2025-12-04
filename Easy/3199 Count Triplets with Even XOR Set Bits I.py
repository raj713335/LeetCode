# https://leetcode.com/problems/count-triplets-with-even-xor-set-bits-i/description/

class Solution:
    def tripletCount(self, a: List[int], b: List[int], c: List[int]) -> int:
        
        count = 0

        for i in range(0, len(a)):
            for j in range(0, len(b)):
                for k in range(0, len(c)):
                    temp = bin(a[i] ^ b[j] ^ c[k]).count("1")
                    if temp % 2 == 0:
                        count += 1

        return count
        
