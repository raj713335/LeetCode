# https://leetcode.com/problems/adding-spaces-to-a-string/description/?envType=daily-question&envId=2024-12-03

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:

        res_string = ""

        for i in range(0, len(s)):
            try:
                if i == spaces[0]:
                    res_string += " "
                    del spaces[0]
            except:
                pass
            
            res_string += s[i]

        return res_string
