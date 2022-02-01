# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        max_count = 0
        
        for i in range(0, len(s)):
            count = 0
            dict ={}
            for j in range(i, len(s)):
                if s[j] not in dict:
                    dict[s[j]] = 1
                    count += 1
                else:
                    if count > max_count:
                        max_count = count
                    break
            if count > max_count:
                max_count = count
        return max_count
        
        
        
