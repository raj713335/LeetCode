# https://leetcode.com/problems/categorize-box-according-to-criteria/description/


class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:

        bulky = False
        heavy = False
        if max(length, width, height, mass) >= 10**4 or ((length*width*height)>= 10**9):
            bulky = True
        if mass >= 100 :
            heavy = True


        if bulky and heavy:
            return "Both"
        elif not(bulky) and not(heavy):
            return "Neither"
        if bulky and not(heavy):
            return "Bulky"
        else:
            return "Heavy"
        
