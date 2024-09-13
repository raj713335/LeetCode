# https://leetcode.com/problems/xor-queries-of-a-subarray/description/

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        
        output = []

        xor_arr = [0]

        for each in arr:
            xor_arr.append(xor_arr[-1] ^ each)
        
        for L,R in queries:
            output.append(xor_arr[L]^xor_arr[R+1])
            
        return output
        
