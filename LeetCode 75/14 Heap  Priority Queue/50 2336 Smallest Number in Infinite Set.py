# https://leetcode.com/problems/smallest-number-in-infinite-set/description/

class SmallestInfiniteSet:

    def __init__(self):
        self.counter = 1
        self.arr = set()
        

    def popSmallest(self) -> int:
        
        if len(self.arr) > 0 and self.counter > min(self.arr):
            popx = min(self.arr)
            self.arr.remove(popx)
            
        else:
            popx = self.counter
            self.counter += 1
            
        return popx
        

    def addBack(self, num: int) -> None:
        
        if num < self.counter:
            self.arr.add(num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
