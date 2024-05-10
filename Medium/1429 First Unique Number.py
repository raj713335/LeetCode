# https://leetcode.com/problems/first-unique-number/description/


class FirstUnique:
    def __init__(self, nums: List[int]):
        self.dictx = {}

        for each in nums:
            if each not in self.dictx:
                self.dictx[each] = 1
            else:
                self.dictx[each] += 1
        

    def showFirstUnique(self) -> int:
        for key, value in self.dictx.items():
            if value == 1:
                return key
        return -1
        

    def add(self, value: int) -> None:
        if value not in self.dictx:
            self.dictx[value] = 1
        else:
            self.dictx[value] += 1
        


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
