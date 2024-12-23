# https://leetcode.com/problems/design-skiplist/description/


class Skiplist:

    def __init__(self):
        self.dictx = {}
        

    def search(self, target: int) -> bool:
        if target in self.dictx:
            return True
        else:
            return False
        

    def add(self, num: int) -> None:
        if num in self.dictx:
            self.dictx[num] += 1
        else:
            self.dictx[num] = 1
        

    def erase(self, num: int) -> bool:
        if num in self.dictx:
            if self.dictx[num] == 1:
                del self.dictx[num]
            else:
                self.dictx[num] -= 1
            return True
        else:
            return False
        


# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)
