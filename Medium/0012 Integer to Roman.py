# https://leetcode.com/problems/integer-to-roman/

class Solution:
    def intToRoman(self, num: int) -> str:
        a={
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
        c=[]
        for k,v in reversed(a.items()):
            while num>0:
                if v<=num:
                    c.append(k)
                    num-=v
                else:
                    break
        return "".join(c)
        
