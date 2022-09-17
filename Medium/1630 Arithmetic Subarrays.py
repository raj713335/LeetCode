# https://leetcode.com/problems/arithmetic-subarrays/


class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        
        
        output = []
        
        for i in range(0, len(l)):
            flag = True
            temp = sorted(nums[l[i]: r[i]+1])
            print(temp)
            
            if len(temp) < 2:
                flag = False
                output.append(flag)
                break
            
            diff = temp[1] - temp[0]
            
            for i in range(1, len(temp)-1):
                if diff != (temp[i+1]-temp[i]):
                    flag = False
                    break
            
            output.append(flag)
            
        return output
                    
        
