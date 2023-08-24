# https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/description/

class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:

        ans = set()
        for i, num in enumerate(nums):
            if num == key:
                ans.update(range(max(0, i-k), min(i+k+1, len(nums))))
        return sorted(list(ans))
        
