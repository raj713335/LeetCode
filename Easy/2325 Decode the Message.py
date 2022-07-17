# https://leetcode.com/problems/decode-the-message/



class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        
        listx = ["a", "b","c","d","e","f","g", "h","i","j","k", "l","m", "n", "o", "p",
                "q", "r", "s", "t", "u", "v", "w", "x", "y","z"]
        
        print(len(listx), len(key))
        
        dictx = {}
        iterx = 0
        
        for i in range(0, len(key)):
            if key[i] not in dictx and key[i]!=" ":
                dictx[key[i]] = listx[iterx]
                iterx += 1
            
        output = ""
        
        for i in range(0, len(message)):
            if message[i] == " ":
                output += " "
            else:
                output += dictx[message[i]]
            
        return output
            
            
        
            
        
