# https://leetcode.com/problems/k-th-symbol-in-grammar/description/


class Solution:
    def kthGrammar(self, n: int, k: int) -> int:

        if n == 1 and k == 1:
            return 0 

        mid = (2 ** (n - 1)) // 2  # Find the midpoint of the row

        if k <= mid:
            return self.kthGrammar(n - 1, k)  # First half, same as parent
        else:
            return 1 - self.kthGrammar(n - 1, k - mid)  # Second half, flipped

        
