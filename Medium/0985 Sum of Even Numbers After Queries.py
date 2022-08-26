# https://leetcode.com/problems/sum-of-even-numbers-after-queries/


class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        
        output = []
        
        sumx = 0
        
        for i in range(0, len(nums)):
            if nums[i] % 2 == 0:
                sumx += nums[i]
                
        #print(sumx)
        
        for value, idx in queries:
            temp = nums[idx]
            sumxx = nums[idx] + value
            nums[idx] = sumxx
            #print(sumxx)
            if sumxx % 2 == 0:
                if temp % 2 == 0:
                    sumx -= temp
                sumx += sumxx
            else:
                if temp % 2 == 0:
                    sumx -= temp
                
            output.append(sumx)
            
        #print(nums)    
        return output
                
            
            
        
