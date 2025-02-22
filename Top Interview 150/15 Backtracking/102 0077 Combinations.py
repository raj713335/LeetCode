# https://leetcode.com/problems/combinations/description/


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        res = []

        def backtracking(index, sublist):
            if len(sublist) == k:
                res.append(sublist[:])
                return

            for i in range(index, n + 1):
                sublist.append(i)
                backtracking(i + 1, sublist)
                sublist.pop()  # Backtrack

        backtracking(1, [])
        return res
        
