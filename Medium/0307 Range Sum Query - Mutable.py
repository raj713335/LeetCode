# https://leetcode.com/problems/range-sum-query-mutable/description/


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.sumx = sum(self.nums)
        

    def update(self, index: int, val: int) -> None:
        self.sumx = (self.sumx + val - self.nums[index])
        self.nums[index] = val
        

    def sumRange(self, left: int, right: int) -> int:
        return (self.sumx - sum(self.nums[:left:]) - sum(self.nums[right+1:]))
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
