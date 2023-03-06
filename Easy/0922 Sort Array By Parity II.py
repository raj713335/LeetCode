# https://leetcode.com/problems/sort-array-by-parity-ii/description/


class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:

        even = []
        odd = []

        res = []

        for i in range(0, len(nums)):
            if nums[i] % 2 == 0:
                even.append(nums[i])
            else:
                odd.append(nums[i])

        even[:] = even[::-1]
        odd[:] = odd[::-1]


        for i in range(0, len(nums)):
            if i % 2 == 0:
                x = even.pop()
                res.append(x)
            else:
                x = odd.pop()
                res.append(x)


        return res
        
