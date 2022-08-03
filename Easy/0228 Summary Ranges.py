# https://leetcode.com/problems/summary-ranges/


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        output = []
        
        if len(nums) == 0:
            return output
        
        temp_list = [nums[0]]
        
        for each in nums[1:]:
            if temp_list[-1]+1 == each:
                temp_list.append(each)
            else:
                if len(temp_list) >1:
                    strx = str(temp_list[0])+"->"+str(temp_list[-1])
                    output.append(strx)
                else:
                    output.append(str(temp_list[0]))
                
                temp_list = [each]
                
        if len(temp_list) >1:
            strx = str(temp_list[0])+"->"+str(temp_list[-1])
            output.append(strx)
        else:
            output.append(str(temp_list[0]))
                
        return output
        
