# https://leetcode.com/problems/product-of-array-except-self/description/?envType=study-plan-v2&envId=top-interview-150


# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
        
#         prefix = [1] * (len(nums)+1)
#         postfix = [1] * (len(nums)+1)

#         for i in range(0, len(nums)):
#             prefix[i+1] = nums[i] * prefix[i]

#         for i in range(len(nums)-1, -1, -1):
#             postfix[i] = nums[i] * postfix[i+1]

#         result = []

#         for i in range(1, len(nums)+1):
#             val = prefix[i-1] * postfix[i]
#             result.append(val)

#         return result


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefix = 1

        for i in range(0, len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1

        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res
