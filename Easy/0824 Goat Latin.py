# https://leetcode.com/problems/goat-latin/


class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        
        dictx = {"a": 1 , "e" : 1, "i" : 1, "o" : 1, "u" : 1, "A": 1 , "E" : 1, "I" : 1, "O" : 1, "U" : 1}
        
        sentence = sentence.split(" ")
        output= []
        
        for i in range(0, len(sentence)):
            if sentence[i][0] in dictx:
                temp = sentence[i] + "ma" + "a"*(i+1)
            else:
                temp = sentence[i][1:] + sentence[i][0] + "ma" + "a"*(i+1)
            output.append(temp)
        return " ".join(output)
        
