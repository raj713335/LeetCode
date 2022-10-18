# https://leetcode.com/problems/validate-stack-sequences/


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        stack = []
        
        while pushed:
            
            stack.append(pushed.pop(0))
            
            
            flag = True
            
            while flag and stack:

                if stack[-1] == popped[0]:
                    stack.pop()
                    del popped[0]
                else:
                    flag = False
       
        if stack:
            return False
        else:
            return True
                
        
        
