# https://leetcode.com/problems/longest-nice-substring/description/


class Solution:
    def longestNiceSubstring(self, s: str) -> str:

        max_string = ""

        for i in range(0, len(s)-1):
            for j in range(i+1, len(s)):
                temp = s[i:j+1]
                if len(max_string) < len(temp):
                    if len(set(temp)) % 2 == 0:
                        flag = True
                        for j in range(0, len(temp)):
                            if temp[j].upper() not in temp:
                                flag = False
                            if temp[j].lower() not in temp:
                                flag = False
                        
                        if flag:
                            max_string = temp

        return max_string
        
