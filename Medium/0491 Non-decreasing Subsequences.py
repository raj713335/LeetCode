# https://leetcode.com/problems/non-decreasing-subsequences/description/


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)

        res = set()

        def backtrack(index, prev, sub_array):
            if index == n:
                if len(sub_array) >= 2:
                    res.add(tuple(sub_array[:]))
                return 

            sub_array.append(nums[index])

            if nums[index] >= prev:
                backtrack(index+1, nums[index], sub_array)
            
            sub_array.pop()
            backtrack(index+1, prev, sub_array)

        backtrack(0, float("-inf"), [])

        return [list(seq) for seq in res]
        
