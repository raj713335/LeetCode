# https://leetcode.com/problems/find-the-distance-value-between-two-arrays/description/


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:

        n1,n2,c = len(arr1),len(arr2),0
        for i in range(n1):
            c1=0
            for j in range(n2):
                if abs(arr1[i]-arr2[j])>d:
                    c1+=1
                else:
                    break
            if c1==n2:
                c+=1
        return c
        
