# https://leetcode.com/problems/equal-score-substrings/description/

class Solution:
    def scoreBalance(self, s: str) -> bool:

        dictx = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11,  
        'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 
        'w': 23, 'x': 24, 'y': 25, 'z': 26}

        sumx = 0

        for each in s:
            sumx += dictx[each]

        left = 0
        right = sumx

        for i in range(0, len(s)):
            right -= dictx[s[i]]
            left += dictx[s[i]]

            if left == right:
                return True
        
        return False
        
