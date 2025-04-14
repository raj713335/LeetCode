# https://leetcode.com/problems/longest-palindromic-substring/description/

# Time Complexity: O(n × n)
# Space Complexity: O(n × n) (for the dp table)

class Solution:
    def longestPalindrome(self, s: str) -> str:

        n = len(s)

        # Edge case: empty or single character string
        if n < 2:
            return s

        dp = [[False] * (n) for s in range(n)]

        start = 0           # Start index of the longest palindrome
        max_length = 1      # Length of the longest palindrome

        # All substrings of length 1 are palindromes
        for i in range(n):
            dp[i][i] = 1

        # Check for substrings of length 2
        for i in range(0, n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = 1 
                start = i
                max_length = 2


        # Check for substrings of length 3 and more
        for length in range(3, n + 1): # length of substring
            for i in range(n - length + 1):
                j = i + length -1 # ending index of substring

                # Check if the current substring is a palindrome
                if s[i] == s[j] and dp[i+1][j-1] == 1:
                    dp[i][j] = True
                    start = i
                    max_length = length
                    
        # Return the longest palindromic substring
        return s[start:start+max_length]
        
