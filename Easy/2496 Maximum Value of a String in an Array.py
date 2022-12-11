# https://leetcode.com/problems/maximum-value-of-a-string-in-an-array/description/


class Solution:
    def maximumValue(self, strs: List[str]) -> int:

        maxi = 0

        for each in strs:
            try:
                lenx = int(each)
            except: 
                lenx= len(each)
            if lenx > maxi:
                maxi = lenx

        return maxi
