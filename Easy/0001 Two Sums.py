class Solution:
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}
        for index, value in enumerate(nums): 
            differ = target - value
            if value in diff:
                return(index, diff[value])
            else:
                diff[differ] = index
            
            

