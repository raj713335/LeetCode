# https://leetcode.com/problems/combination-sum-ii/submissions/

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        n = len(candidates)


        candidates = sorted(candidates)

        def backtracking(index, sub_arr, current_sum):
            if current_sum == target:
                res.append(sub_arr[:])
                return

            if  current_sum > target:
                return 
            
            prev = -1
            for i in range(index, n):
                if candidates[i] == prev:
                    continue
                sub_arr.append(candidates[i])
                backtracking(i+1, sub_arr , current_sum + candidates[i])
                sub_arr.pop()
                prev = candidates[i]


        backtracking(0, [], 0)
        return res
