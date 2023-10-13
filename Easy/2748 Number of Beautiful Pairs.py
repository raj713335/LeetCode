# https://leetcode.com/problems/number-of-beautiful-pairs/description/


class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:

        count = 0

        def gcd(num1, num2):
            for i in range(2, int(min(num1, num2))+1):
                if num1%i == 0 and num2%i == 0:
                    return True
            return False


        for i in range(0, len(nums)-1):
            for j in range(i+1, len(nums)):
                if gcd(int(str(nums[i])[0]), int(str(nums[j])[-1])) == False:
                    count += 1

        return count
