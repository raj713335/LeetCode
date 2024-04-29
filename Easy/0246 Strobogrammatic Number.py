# https://leetcode.com/problems/strobogrammatic-number/

class Solution:
    def isStrobogrammatic(self, num: str) -> bool:

        map = {
                '0': '0',
                '1': '1',
                '2': '|',
                '3': '|',
                '4': '|',
                '5': '|',
                '6': '9',
                '7': '|',
                '8': '8',
                '9': '6',
              }
        
        rotatedNum = ""
        for i in num:
            rotatedNum += map[i]
            
        return(num == rotatedNum[::-1])
        
