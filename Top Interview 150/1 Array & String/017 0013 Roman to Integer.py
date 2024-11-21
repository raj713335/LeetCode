# https://leetcode.com/problems/roman-to-integer/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        
        res = 0
        flag = False
        
        for i in range(0, len(s)):

            if i+1 < len(s) and roman[s[i]] < roman[s[i+1]]:
                flag = True
                continue

            if flag == True:
                res += (roman[s[i]] - roman[s[i-1]])
                flag = False
                continue
            if not flag:
                res += roman[s[i]]
            
        return res
            
        
