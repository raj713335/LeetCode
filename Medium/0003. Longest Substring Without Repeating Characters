# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # if s == " ":
        #     return 1
        dictx = {}
        
        max_count = 0
        
        count = 0
        
        for each in s:
            if each not in dictx:
                dictx[each] = 1
                count += 1
            else:
                if count > max_count:
                    max_count = count
                count = 1
        if count > max_count:
            max_count = count
                
        return max_count
        
