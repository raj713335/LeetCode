# https://leetcode.com/problems/flatten-2d-vector/description/


class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.listx = []

        for each in vec:
            self.listx.extend(each)

        self.listx = self.listx[::-1]
        

    def next(self) -> int:
        return self.listx.pop()
        

    def hasNext(self) -> bool:
        if self.listx:
            return True
        else:
            return False
        


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()
