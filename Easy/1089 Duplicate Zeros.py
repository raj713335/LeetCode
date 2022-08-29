# https://leetcode.com/problems/duplicate-zeros/


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        
        length = len(arr)
        
        iterx = 0
        count = 0
        
        while iterx < length:
            if arr[iterx] == 0:
                arr.insert(iterx, 0)
                iterx += 2
                count += 1
            else: 
                iterx += 1
                
        while count > 0:
            del arr[-1]
            count -= 1
        
