# https://leetcode.com/problems/4sum-ii/description/


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:

        hmap = defaultdict(int)
        count = 0
        for i in nums1:
            for j in nums2:
                hmap[i+j] += 1
        
        for k in nums3:
            for l in nums4:
                count += hmap[-(k+l)]
        return count
        
