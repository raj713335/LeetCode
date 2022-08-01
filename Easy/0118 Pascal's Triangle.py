# https://leetcode.com/problems/pascals-triangle/

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        output = []
        
        for i in range(0, numRows):
            temp_list = []
            last_value = 0
            if len(output) > 0:
                for each in output[-1]:
                    temp_list.append(each+last_value)
                    last_value = each
            temp_list.append(1)
            output.append(temp_list)
            
        return output
                
                
                
        
