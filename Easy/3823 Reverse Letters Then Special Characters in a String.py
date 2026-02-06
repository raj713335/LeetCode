# https://leetcode.com/problems/reverse-letters-then-special-characters-in-a-string/description/

class Solution:
    def reverseByType(self, s: str) -> str:

        res = []

        letter = []
        special = []

        for word in s:
            if word.isalpha() == True:
                letter.append(word)
                res.append(1)
            else:
                special.append(word)
                res.append(0)


        for i in range(0, len(res)):
            if res[i] == 1:
                word = letter.pop()
                res[i] = word
            else:
                word = special.pop()
                res[i] = word

        return "".join(res)


        
        
