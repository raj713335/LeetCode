# https://leetcode.com/problems/uncrossed-lines/description/

class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:

        n1 =  len(nums1) - 1
        n2 =  len(nums2) - 1

        dp = {}

        def dfs(nums1, nums2, index_1, index_2):

            if (index_1 == -1 or index_2 == -1):
                return 0
            if (index_1, index_2) in dp:
                return dp[(index_1, index_2)]

            ways = 0

            if nums1[index_1] == nums2[index_2]:
                ways = max(ways, 1 + dfs(nums1, nums2, index_1 - 1, index_2 - 1))
            else:
                ways = max(ways, dfs(nums1, nums2, index_1 - 1, index_2), dfs(nums1, nums2, index_1, index_2 - 1))

            dp[(index_1, index_2)] = ways
            return dp[(index_1, index_2)]

        return dfs(nums1, nums2, n1, n2)
        
