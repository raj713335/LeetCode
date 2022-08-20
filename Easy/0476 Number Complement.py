# https://leetcode.com/problems/number-complement/submissions/


class Solution:
    def findComplement(self, num: int) -> int:
        
        nums = bin(num)[2:][::-1]
        
        output = 0
        
        for i in range(0, len(nums)):
            if nums[i] == "0":
                output += (2**i)
                print(i, output)
                
        return output
            
        
