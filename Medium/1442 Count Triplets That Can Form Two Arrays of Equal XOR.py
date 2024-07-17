# https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/description/


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        
        dictx = {}
        res = 0

        N = len(arr)
        
        for i in range(0, N-1):
            a = 0
            for j in range(i+1, N):
                a ^= arr[j-1]
                b = 0
                for k in range(j, N):
                    b ^= arr[k]
                    if a == b:
                        res += 1
                        
        return res
