# https://leetcode.com/problems/rearrange-words-in-a-sentence/


class Solution:
    def arrangeWords(self, text: str) -> str:
        
        output = []
        outputx= []
        text = text.split(" ")
        
        for each in text:
            output.append([each, len(each)])
            
        output = sorted(output, key = lambda x: x[1])
        
        for i in range(0, len(output)):
            if i == 0:
                outputx.append(output[i][0].capitalize())
            else:
                outputx.append(output[i][0].lower())
            
        return " ".join(outputx)
        
        
        
