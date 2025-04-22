# https://leetcode.com/problems/combination-sum-iii/description/

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        res = []

        candidates = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        def backtracking(index, sub_arr, current_sum, k):
            if current_sum == n and k == 0:
                res.append(sub_arr[:])
                return

            if  index >= 9 or current_sum > n or k < 0:
                return 
            

            for i in range(index, 9):
                sub_arr.append(candidates[i])
                backtracking(i+1, sub_arr , current_sum + candidates[i], k-1)
                sub_arr.pop()
 

        backtracking(0, [], 0, k)
        return res
        
