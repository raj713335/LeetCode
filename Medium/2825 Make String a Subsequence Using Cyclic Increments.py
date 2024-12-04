# https://leetcode.com/problems/make-string-a-subsequence-using-cyclic-increments/description/

class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:

        dictx = {'a': 'b', 'b': 'c', 'c': 'd', 'd': 'e', 'e': 'f', 'f': 'g', 'g': 'h', 'h': 'i', 'i': 'j', 'j': 'k', 'k': 'l', 'l': 'm', 'm': 'n', 'n': 'o', 'o': 'p', 'p': 'q', 'q': 'r', 'r': 's', 's': 't', 't': 'u', 'u': 'v', 'v': 'w', 'w': 'x', 'x': 'y', 'y': 'z', 'z': 'a'}

        n1 = len(str1)
        n2 = len(str2)

        if n1 == 0:
            return True

        i = 0
        j = 0

        while j < n2 and i < n1:
            if dictx[str1[i]] == str2[j] or str1[i] == str2[j]:
                i += 1
                j += 1
            else:
                i += 1

        if j == n2:
            return True
        else:
            return False

        
