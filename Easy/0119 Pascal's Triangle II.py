# https://leetcode.com/problems/pascals-triangle-ii/

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        output = []

        for i in range(0, rowIndex+1):
            temp_list = []
            last_value = 0
            if len(output) > 0:
                for each in output[-1]:
                    temp_list.append(each+last_value)
                    last_value = each
            temp_list.append(1)
            output.append(temp_list)

        return output[-1]
        
