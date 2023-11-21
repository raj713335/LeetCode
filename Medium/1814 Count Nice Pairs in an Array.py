# https://leetcode.com/problems/count-nice-pairs-in-an-array/description/


class Solution:
    def countNicePairs(self, nums: List[int]) -> int:

        freq = {} 
        nicePairs = 0  


        for num in nums:
            revNum = int(str(num)[::-1])
            diff = num - revNum
            freq[diff] = freq.get(diff, 0) + 1

 
        for count in freq.values():
            nicePairs += count * (count - 1) // 2

        return nicePairs % (10**9 + 7)



       
        
