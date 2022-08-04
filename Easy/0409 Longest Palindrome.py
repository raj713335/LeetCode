# https://leetcode.com/problems/longest-palindrome/

class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        dictx = {}
        
        longest = 0
        
        if len(set(s)) == 1:
            return len(s)
        
        for each in s:
            if each not in dictx:
                dictx[each] = 1
            else:
                dictx[each] += 1
        flag = True     
        for each in dictx.values():
            longest += ((each//2)*2)
            if (each%2!=0):
                flag = False
                
        if flag:
            return longest
        return longest+1
        
