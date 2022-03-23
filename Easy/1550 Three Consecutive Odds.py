# https://leetcode.com/problems/three-consecutive-odds/

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        
        for i in range(0, len(arr)-3+1):
            count = 0
            for each in arr[i:i+3]:
                if each % 2 != 0:
                    count += 1
            if count ==3:
                return True
        return False
        
