 https://leetcode.com/problems/longest-substring-without-repeating-characters/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        j = 0

        max_subseq = 0
        dictx = {}

        for i in range(0, len(s)):
            
            while s[i] in dictx.keys():
                del dictx[s[j]]
                j += 1

            max_subseq = max(i-j+1, max_subseq) 
            dictx[s[i]] = 1

        return max_subseq   
