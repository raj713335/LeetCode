# https://leetcode.com/problems/maximum-length-substring-with-two-occurrences/description/

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:

        dictx = {}

        count = 0

        for i in range(0, len(s)-1):
            for j in range(i+1, len(s)):
                temp = s[i:j+1]
                dictz = {}
                flag = True
                if temp not in dictx:
                    if len(temp) != len(set(temp)):
                        for each in temp:
                            if each not in dictz:
                                dictz[each] = 1
                            else:
                                dictz[each] += 1
                                if dictz[each] > 2:
                                    flag = False
                                    break
                        if len(temp) > count and flag:
                            count = len(temp)
                    dictx[temp] = 1
        
        if count == 0:
            return len(s)
        return count
        
