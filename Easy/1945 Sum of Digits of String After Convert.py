# https://leetcode.com/problems/sum-of-digits-of-string-after-convert/


class Solution:
    def getLucky(self, s: str, k: int) -> int:
        
        dictx = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9 ,
                 "j": 10,"k":11,"l":12, "m": 13, "n":14, "o":15 , "p":16 , "q":17 , "r" :18 ,
                 "s":19 , "t":20 , "u" : 21, "v" :22 ,"w": 23, "x":24 , "y" :25 , "z" :26}
        
        strx = ""
        temp = 0
        
        for each in s:
            strx += str(dictx[each])
            
        while k > 0:
            print(strx)
            for each in strx:
                temp += int(each)
            strx = str(temp)
            temp = 0
            k -= 1
            
        return int(strx)
        
