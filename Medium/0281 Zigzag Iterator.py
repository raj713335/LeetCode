# https://leetcode.com/problems/zigzag-iterator/description/

class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.v1 = v1[::-1]
        self.v2 = v2[::-1]
        self.chance = True
        

    def next(self) -> int:
        if self.chance and self.v1:
            self.chance = False
            return self.v1.pop()
        elif not self.chance and self.v2:
            self.chance = True
            return self.v2.pop()
        elif self.v1:
            return self.v1.pop()
        else:
            return self.v2.pop()

        

    def hasNext(self) -> bool:
        if self.v1 or self.v2:
            return True
        else:
            return False
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
