# https://leetcode.com/problems/wiggle-sort-ii/description/


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)
        
        # Step 2: Fill odd indices first with larger values
        n = len(nums)
        for i in range(1, n, 2):  # Odd indices
            nums[i] = -heapq.heappop(max_heap)
        
        # Step 3: Fill even indices with remaining smaller values
        for i in range(0, n, 2):  # Even indices
            nums[i] = -heapq.heappop(max_heap)
