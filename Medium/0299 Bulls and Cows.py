# https://leetcode.com/problems/bulls-and-cows/


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        
        bulls = 0
        cows  = 0
        dictx = {}
        
        
        for i in range(0, len(secret)):
            if secret[i] not in dictx:
                dictx[secret[i]] = 1
            else:
                dictx[secret[i]] += 1
        
        
        for i in range(0, len(secret)):
            if secret[i] == guess[i]:
                dictx[guess[i]] -= 1
                bulls += 1
                
   
                    
        for i in range(0, len(secret)):
            if secret[i] != guess[i]: 
                if guess[i] in dictx:
                    if dictx[guess[i]] > 0:
                        dictx[guess[i]] -= 1
                        cows +=1
                
                      
                    
        return str(bulls)+"A"+str(cows)+"B"
        
        
