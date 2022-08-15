# https://leetcode.com/problems/sort-even-and-odd-indices-independently/


class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        
        odd = []
        even = []
        output =[]
        
        for i in range(0, len(nums)):
            if i%2==0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
        
        even = sorted(even)
        odd = sorted(odd, reverse=True)
        
        
        
        for i in range(0, max(len(even), len(odd))):
            try:
                output.append(even[i])
                output.append(odd[i])
                
            except:
                pass
            
        return output
        
