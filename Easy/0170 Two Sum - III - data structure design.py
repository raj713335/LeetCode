# https://leetcode.com/problems/two-sum-iii-data-structure-design/

class TwoSum:

    def __init__(self):
        self.arr = []
        

    def add(self, number: int) -> None:
        self.arr.append(number)
        

    def find(self, value: int) -> bool:

        seen={}
        for i in range(len(self.arr)):
            diff = value - self.arr[i]
            if diff in seen:
                return True
            else:
                seen[self.arr[i]] = i
        return False
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
