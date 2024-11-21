# https://leetcode.com/problems/integer-to-roman/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def intToRoman(self, num: int) -> str:

        roman = {
            'I':1,
            'IV':4,
            'V':5,
            'IX':9,
            'X':10,
            'XL':40,
            'L':50,
            'XC':90,
            'C':100,
            'CD':400,
            'D':500,
            'CM':900,
            'M':1000
        }

        res = []
        
        for key, value in reversed(roman.items()):
            while num > 0:
                if value <= num:
                    res.append(key)
                    num -= value
                else:
                    break

        return "".join(res)

                

        
