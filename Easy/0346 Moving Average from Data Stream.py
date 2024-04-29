# https://leetcode.com/problems/moving-average-from-data-stream/description/

class MovingAverage:

    def __init__(self, size: int):
        self.a = []
        self.size = size
        

    def next(self, val: int) -> float:
        self.a.append(val)

        return sum(self.a[-self.size:])/min(len(self.a), self.size)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
