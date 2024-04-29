# https://leetcode.com/problems/valid-word-square/description/

class Solution:
    def validWordSquare(self, words: List[str]) -> bool:

        row = []
        col = []

        
        for i in range(0, len(words)):
            temp = ""
            for j in range(0, len(words)):

                try:
                    temp += words[j][i]
                except:
                    pass

            row.append(temp)

            if temp != words[i]:
                return False

        return True
                
        
