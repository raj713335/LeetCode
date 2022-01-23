class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        res = 0
        flag = False

        for i in range(0, len(s)):
            try:
                if roman[s[i]] < roman[s[i + 1]]:
                    flag = True
                    continue
            except:
                pass
            if flag == True:
                res += (roman[s[i]] - roman[s[i-1]])
                flag = False
                continue
            if flag != True:
                res += roman[s[i]]

        return res

        
