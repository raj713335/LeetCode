# https://leetcode.com/problems/keyboard-row/

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        
        output = []
        
        keyboard = {"q":1,"w":1,"e":1,"r":1,"t":1,"y":1,"u":1,"i":1,"o":1,"p":1, 
                   "a":2,"s":2,"d":2,"f":2,"g":2,"h":2,"j":2,"k":2,"l":2,
                   "z":3,"x":3,"c":3,"v":3,"b":3,"n":3,"m":3}
        
        for word in words:
            temp_word = list(word.lower())
            temp_value = []
            
            for each in temp_word:
                temp_value.append(keyboard[each])
            
            if len(set(temp_value)) == 1:
                output.append(word)
                
                
        return output
            
        
