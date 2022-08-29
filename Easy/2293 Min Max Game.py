# https://leetcode.com/problems/min-max-game/


class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        
        flag = True
        
        output = nums
        
        while len(output) != 1:
            temp = []
            for i in range(0, len(output), 2):
                if flag:
                    temp.append(min(output[i], output[i+1]))
                    flag = False
                else:
                    temp.append(max(output[i], output[i+1]))
                    flag = True
                
            output = temp

        
        return output[0]
                
            
                
        
