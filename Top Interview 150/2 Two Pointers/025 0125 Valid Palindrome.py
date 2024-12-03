# https://leetcode.com/problems/valid-palindrome/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.lower()
        n = len(s)

        i, j = 0, n-1

        while i <= j:

            while i < j and not s[i].isalnum():
                i += 1

            while i < j and not s[j].isalnum():
                j -= 1

            if s[i] != s[j]:
                return False
            
            i += 1
            j -= 1

        return True
