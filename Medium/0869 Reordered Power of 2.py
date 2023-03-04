# https://leetcode.com/problems/reordered-power-of-2/description/


class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:

        occurrence = Counter(str(n))

        for i in range(30):
            if (occurrence == Counter(str(2**i))):
                return True
        return False
        
