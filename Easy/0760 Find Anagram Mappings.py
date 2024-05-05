# https://leetcode.com/problems/find-anagram-mappings/description/


class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:

        ans = []

        for i in range(0, len(nums1)):
            for j in range(len(nums2)-1, -1, -1):
                if nums1[i] == nums2[j]:
                    ans.append(j)
                    nums2[j] = "X"
                    break


        return ans
        
