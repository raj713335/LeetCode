# https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/


from itertools import combinations

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        max_values = 0
        
        for i in range(len(arr), 0, -1):
            values = combinations(arr, i)
            
            for each in values:
                temp = "".join(each)
                lengthx = len(temp)
                if lengthx == len(set(temp)):
                    if max_values < lengthx:
                        max_values = lengthx
                        

        return max_values
            
            
        
        
