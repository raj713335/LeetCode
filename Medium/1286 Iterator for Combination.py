# https://leetcode.com/problems/iterator-for-combination/description/

from itertools import combinations
class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.listx = list(combinations(characters, combinationLength))
        self.i = 0
        

    def next(self) -> str:
        val = "".join(self.listx[self.i])
        self.i += 1
        return val
        

    def hasNext(self) -> bool:
        if self.i < len(self.listx):
            return True
        else:
            return False
        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
