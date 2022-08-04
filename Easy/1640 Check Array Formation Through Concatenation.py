# https://leetcode.com/problems/check-array-formation-through-concatenation/

class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        
        
        for i in range(0, len(pieces)):
            lex = len(pieces[i])
            flag = True
            for j in range(0, len(arr)):
                #print(arr[j:j+lex] , pieces[i])
                if arr[j:j+lex] == pieces[i]:
                    flag = False
            if flag:
                return False
            
        return True
                
            
