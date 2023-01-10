# https://leetcode.com/problems/reformat-the-string/description/

class Solution:
    def reformat(self, s: str) -> str:

        nums = []
        chars = []

        res = ""

        for each in s:
            try:
                temp = int(each)
                nums.append(each)
            except:
                chars.append(each)


        if abs(len(nums)-len(chars)) >1:
            return ""

        if len(nums) > len(chars):
            for i in range(len(chars)):
                res += (nums[i]+chars[i])
            res += nums[-1]
        elif len(nums) < len(chars):
            for i in range(len(nums)):
                res += (chars[i]+nums[i])
            res += chars[-1]
        else:
            for i in range(len(chars)):
                res += (nums[i]+chars[i])


        return res

        
        
